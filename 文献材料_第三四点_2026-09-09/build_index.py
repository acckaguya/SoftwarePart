from collect import ROOT, GROUPS
from pathlib import Path
from PyPDF2 import PdfReader
from collections import Counter
import json,re,hashlib,html

seedlines=[s.split('|') for s in (ROOT/'seeds.txt').read_text(encoding='utf-8').splitlines() if s.strip()]
records=[];checks=[]
for group,alias,source,note,priority in seedlines:
    f=ROOT/GROUPS[group]/(alias+'.metadata.json')
    r=json.loads(f.read_text(encoding='utf-8'))
    r['reading_note']=note;r['priority']=priority
    r['title']=r['title'].replace('{','').replace('}','').replace('Google��s','Google’s').replace("D\\'ej\\`aVu",'DéjàVu')
    if not r.get('date') and r.get('arxiv_id'):r['date']='20'+r['arxiv_id'][:2]
    if alias=='Gemini':r['date']='2023';r['venue']='SOSP 2023'
    if alias=='KunServe':r['reading_note']='以参数为中心的内存管理，处理推理服务内存过载。'
    if r.get('pdf_status')=='downloaded':
        p=ROOT/r['pdf_file'];data=p.read_bytes()
        c={'id':alias,'file':r['pdf_file'],'size':len(data),'sha256':hashlib.sha256(data).hexdigest()}
        try:
            reader=PdfReader(str(p),strict=False)
            c['pages']=len(reader.pages)
            txt=reader.pages[0].extract_text() or ''
            c['first_page_excerpt']=txt[:2200]
            c['status']='ok' if c['pages']>0 and data.startswith(b'%PDF-') else 'failed'
            r['pages']=c['pages']
        except Exception as e:c.update(status='failed',error=str(e))
        checks.append(c)
    records.append(r)
    f.write_text(json.dumps(r,ensure_ascii=False,indent=2),encoding='utf-8')
docs=json.loads((ROOT/'官方文档元数据.json').read_text(encoding='utf-8'))
(ROOT/'文献元数据.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
(ROOT/'下载校验.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2),encoding='utf-8')
counts=Counter(r['group'] for r in records)
size=sum(r['size'] for r in checks)/1024/1024
intro=f'''# 第三、第四点文献资料库

整理日期：2026-09-09。共 **{len(records)} 篇论文PDF、{sum(d['status']=='saved' for d in docs)} 份官方工程文档**，PDF合计约 **{size:.1f} MB**。

对应截图：第三点“计算与模型执行优化”、第四点“大规模集群可靠性与容错”。六个专题分别存放；每篇均保留来源链接、原站网页、中文选读说明和元数据。

- [阅读路线与报告写作建议](阅读路线与报告写作建议.md)：按报告小点安排先读论文与比较维度。
- [网页检索入口](文献索引.html)：可按关键词和专题筛选，并直接打开本地PDF。
- [BibTeX引用文件](references.bib)：用于Zotero、JabRef等文献管理软件。
- [结构化元数据](文献元数据.json)、[下载校验](下载校验.json)、[检索发现记录](检索记录.txt)。

这是检索与归档资料包，中文注释是选读导航，不代表逐篇全文精读或实验复现。arXiv按预印本标识引用；列表日期优先采用原站引用元数据，不将首次提交年份混作会议发表年份。2026年材料可用于跟进前沿，正式引用请核实具体版本与发表状态。

## 数量与覆盖

| 子点 | 论文数 |
|---|---:|
'''
for g,label in GROUPS.items():intro+=f'| {label} | {counts[g]} |\n'
intro+='\n## 论文索引\n'
bib=[];cards=[]
def bval(x):return str(x).replace('&',r'\&').replace('%',r'\%').replace('_',r'\_').replace('#',r'\#')
for group,label in GROUPS.items():
    intro+='\n### '+label+'\n\n'
    for r in [r for r in records if r['group']==group]:
        ident=r['id'];title=r['title'];date=r.get('date','年份待核实')
        venue=r.get('venue','')
        pdf=r.get('pdf_file','');status=r.get('pdf_status','')
        intro+=f"- **{ident}｜{title}**（{date}；{r['priority']}）\n  - 用途：{r['reading_note']}\n  - 来源类型/出处：{venue or '作者/机构原始发布页'}。\n  - [原始页面]({r['url']}) · "+(f"[本地PDF，{r.get('pages','?')}页]({pdf})" if pdf else f'全文状态：{status}')+'\n'
        year=re.search(r'\d{4}',date)
        fields={'title':'{'+bval(title)+'}','author':' and '.join(r.get('authors',[])), 'year':year[0] if year else '', 'url':r['url']}
        if r.get('arxiv_id'):
            typ='misc';fields.update(eprint=r['arxiv_id'],archivePrefix='arXiv',note='Preprint; accessed 2026-09-09')
        else:
            typ='inproceedings' if venue else 'misc'
            if venue:fields['booktitle']=bval(venue)
            fields['note']='Metadata from primary source; accessed 2026-09-09'
        if r.get('doi'):fields['doi']=r['doi']
        bib.append('@'+typ+'{'+ident+',\n'+',\n'.join('  '+k+' = {'+str(v)+'}' for k,v in fields.items() if v)+'\n}')
        esc=html.escape
        hay=esc(' '.join([ident,title,group,r['reading_note'],date,venue]),quote=True)
        cards.append(f'<article data-group="{group}" data-search="{hay}"><small>{group} · {esc(date)} · {r["priority"]}</small><h2>{esc(title)}</h2><p>{esc(r["reading_note"])}</p><p class="meta">{esc(venue)}</p><a href="{esc(pdf)}">打开PDF · {r.get("pages","?")}页</a> <a href="{esc(r["url"])}">原始来源</a><span class="id">{ident}</span></article>')
intro+='\n## 官方工程文档（与研究论文分开）\n\n'
for d in docs:
    intro+=f'- **{d["id"]}**（{d["group"]}）：{d["reading_note"]} [官网]({d["url"]})'+(f' · [网页快照]({d["snapshot"]})' if d.get('snapshot') else ' · 下载未成功')+'\n'
intro+='\n## 下载与核验说明\n\n所有PDF均检查文件标识并解析页数；校验日志保存SHA-256及首页文字摘录，用于题名复核。网页快照可能依赖联网样式。下载脚本仅访问公开原始来源，不包含付费数据库全文。脚本、原始快照及检索记录一并保留，方便后续更新。\n'
(ROOT/'README_文献总索引.md').write_text(intro,encoding='utf-8')
(ROOT/'references.bib').write_text('% Primary-source bibliography. arXiv entries are cited as preprints.\n\n'+'\n\n'.join(bib)+'\n',encoding='utf-8')
page='''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>第三、第四点 · 文献资料库</title><style>body{font:16px/1.65 system-ui,Microsoft YaHei,sans-serif;background:#f3f5f8;color:#182333;max-width:1100px;margin:auto;padding:32px}h1{font-size:30px}header p{color:#526174}nav{display:flex;gap:12px;flex-wrap:wrap;margin:20px 0}input,select{font:inherit;padding:10px;border:1px solid #a9b5c7;border-radius:6px}input{flex:1;min-width:230px}article{background:white;padding:22px;margin:14px 0;border:1px solid #dfe5ed;border-radius:8px}article h2{font-size:20px;margin:5px 0}small,.meta,.id{color:#637188}.meta{font-size:13px}a{color:#145bc2;margin-right:12px}.id{float:right;font-size:12px}article[hidden]{display:none}footer{margin:30px 0}</style><header><h1>计算执行优化与集群可靠性</h1><p>77篇论文 · 11份官方工程文档 · 2026-09-09</p><p><a href="README_文献总索引.md">完整目录与官方文档</a><a href="阅读路线与报告写作建议.md">阅读路线</a><a href="references.bib">BibTeX</a></p></header><nav><input id="q" placeholder="搜索题名、技术、中文用途…"><select id="g"><option value="">全部专题</option>'''
for g,label in GROUPS.items():page+=f'<option value="{g}">{label}</option>'
page+='</select></nav><p id="count"></p><main>'+''.join(cards)+'</main><footer>收集与阅读导航，不代替全文精读。原文版权归作者与出版方所有。网页快照为检索当日版本。</footer><script>const q=document.getElementById("q"),g=document.getElementById("g"),cards=[...document.querySelectorAll("article")];function filter(){let n=0;for(const c of cards){c.hidden=!!((g.value&&c.dataset.group!==g.value)||!c.dataset.search.toLowerCase().includes(q.value.toLowerCase()));if(!c.hidden)n++;}document.getElementById("count").textContent="显示 "+n+" / "+cards.length+" 篇论文";}q.addEventListener("input",filter);g.addEventListener("change",filter);filter();</script></html>'
(ROOT/'文献索引.html').write_text(page,encoding='utf-8')
print(json.dumps({'papers':len(records),'documents':len(docs),'groups':dict(counts),'pdf_MB':round(size,1),'pages':sum(c.get('pages',0) for c in checks),'failed_checks':[c['id'] for c in checks if c['status']!='ok']},ensure_ascii=False))
