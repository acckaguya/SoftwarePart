"""Download public primary sources; preserve metadata and report failures honestly."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.request import Request, urlopen
from urllib.parse import urljoin
import concurrent.futures, json, re, time, hashlib, threading

ROOT = Path(__file__).resolve().parent
GROUPS = {'3a':'3a_低精度_算子_编译优化','3b':'3b_大模型推理加速','3c':'3c_Diffusion与HPC_AI','4a':'4a_监控_故障诊断','4b':'4b_检查点_训练恢复','4c':'4c_推理高可用_SLO'}
class Page(HTMLParser):
    def __init__(self, s):
        super().__init__(); self.meta={}; self.links=[]; self.title=''; self.in_title=False; self.feed(s)
    def handle_starttag(self,t,a):
        d=dict(a)
        if t=='meta': self.meta.setdefault(d.get('name',d.get('property','')).lower(),[]).append(d.get('content',''))
        if t=='a' and 'href' in d: self.links.append(d['href'])
        if t=='title': self.in_title=True
    def handle_endtag(self,t):
        if t=='title': self.in_title=False
    def handle_data(self,d):
        if self.in_title: self.title+=d
    def first(self,k): return next(iter(self.meta.get(k,[])),'')
def get(url):
    for attempt in range(2):
        try:
            with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0 (academic literature collection)'}),timeout=40) as r:
                return r.read(),r.url,r.headers.get('Content-Type','')
        except Exception:
            if attempt: raise
            time.sleep(3)
def collect(item):
    group,alias,source,note,priority=item
    dest=ROOT/GROUPS[group]; dest.mkdir(exist_ok=True)
    rec=dict(id=alias,group=group,reading_note=note,priority=priority,accessed='2026-09-09',kind='paper',title=alias)
    arxiv=bool(re.fullmatch(r'\d{4}\.\d{4,5}',source))
    url='https://arxiv.org/abs/'+source if arxiv else source
    rec['url']=url; rec['arxiv_id']=source if arxiv else ''
    cache=dest/(alias+'.metadata.json')
    if cache.exists():
        old=json.loads(cache.read_text(encoding='utf-8'))
        if old.get('pdf_status')=='downloaded' and old.get('url')==url: return old
    try:
        data,final,ct=get(url); page=Page(data.decode('utf-8',errors='replace'))
        path=dest/(alias+'.source.html'); path.write_bytes(data)
        rec['snapshot']=path.relative_to(ROOT).as_posix()
        rec['title']=page.first('citation_title') or page.first('og:title') or page.title
        rec['title']=re.sub(r'\s*\| USENIX\s*$','',rec['title']).strip()
        rec['authors']=page.meta.get('citation_author',[])
        rec['date']=page.first('citation_date') or page.first('citation_publication_date')
        rec['doi']=page.first('citation_doi')
        rec['venue']=page.first('citation_conference_title') or page.first('citation_journal_title') or ('arXiv（下载版本；会议发表信息另查原始页）' if arxiv else '')
        if not rec['date']:
            m=re.search(r'/conference/([a-z]+)(\d{2})/',url)
            if m: rec['date']='20'+m[2]; rec['venue']=m[1].upper()+' 20'+m[2]
        pdf=page.first('citation_pdf_url')
        if arxiv and not pdf: pdf='https://arxiv.org/pdf/'+source
        if not pdf:
            candidates=[urljoin(final,l) for l in page.links if '.pdf' in l.lower() and 'slides' not in l.lower()]
            if 'usenix.org' in url:
                preferred=[l for l in candidates if '/system/files/' in l and not any(x in l for x in ['proceedings','contents','sponsor'])]
                candidates=preferred or candidates
            pdf=next(iter(candidates),'')
        overrides={
          'TASO':('TASO: Optimizing Deep Learning Computation with Automatic Generation of Graph Substitutions','https://www.cs.cmu.edu/~zhihaoj2/papers/sosp19.pdf','2019',['Zhihao Jia','Oded Padon','James Thomas','Todd Warszawski','Matei Zaharia','Alex Aiken'],'SOSP 2019'),
          'Triton':('Triton: An Intermediate Language and Compiler for Tiled Neural Network Computations','https://www.eecs.harvard.edu/~htk/publication/2019-mapl-tillet-kung-cox.pdf','2019',['Philippe Tillet','H. T. Kung','David Cox'],'MAPL 2019'),
          'Gemini':('Gemini: Fast Failure Recovery in Distributed Training with In-Memory Checkpoints','https://www.cs.rice.edu/~eugeneng/papers/SOSP23.pdf','2023',[],'SOSP 2023')
        }
        if alias in overrides:
            title,pdf,date,authors,venue=overrides[alias]
            rec.update(title=title,date=date,venue=venue)
            if authors: rec['authors']=authors
        rec['metadata_status']='source_page_verified'
        rec['pdf_url']=urljoin(final,pdf) if pdf else ''
        if pdf:
            content,pfinal,pct=get(rec['pdf_url'])
            if not content.startswith(b'%PDF-'): raise ValueError('PDF URL did not return a PDF')
            out=dest/(alias+'.pdf'); out.write_bytes(content)
            rec.update(pdf_status='downloaded',pdf_file=out.relative_to(ROOT).as_posix(),pdf_final_url=pfinal,bytes=len(content),sha256=hashlib.sha256(content).hexdigest())
        else: rec['pdf_status']='no_public_pdf_link_detected'
    except Exception as e:
        rec.setdefault('metadata_status','failed');rec['pdf_status']='failed';rec['error']=str(e)
    cache.write_text(json.dumps(rec,ensure_ascii=False,indent=2),encoding='utf-8')
    print(alias+' '+rec['pdf_status']+' '+rec['title'][:110],flush=True)
    return rec
if __name__=='__main__':
    items=[s.split('|') for s in (ROOT/'seeds.txt').read_text(encoding='utf-8').splitlines() if s.strip()]
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        records=list(pool.map(collect,items))
    (ROOT/'文献元数据.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'total':len(records),'pdfs':sum(r.get('pdf_status')=='downloaded' for r in records),'failures':[r['id'] for r in records if r.get('pdf_status')!='downloaded']},ensure_ascii=False),flush=True)
