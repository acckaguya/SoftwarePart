from pathlib import Path
import json,re,sys
sys.stdout.reconfigure(encoding='utf-8')
from PyPDF2 import PdfReader
ROOT=Path(__file__).resolve().parents[1]
KEYS={'MixedPrecision':'loss scaling','FP8Formats':'E4M3','GPTQ':'Hessian','SmoothQuant':'outlier','AWQ':'activation','FlashAttention':'softmax','TASO':'substitution','Ansor':'search','Orca':'iteration','PagedAttention':'block','SGLang':'RadixAttention','SarathiServe':'chunk','DistServe':'bandwidth','SpeculativeDecoding':'distribution','DPMSolver':'ODE','ProgressiveDistillation':'teacher','DeepCache':'feature','TeaCache':'embedding','FNO':'operator','SmartSim':'database','ColmenaExascale':'workflow','MegaScale':'straggler','SuperBench':'gray','Minder':'metric','Holmes':'profil','CheckFreq':'frequency','CheckNRun':'differential','Gemini':'placement','ByteCheckpoint':'reshard','SWIFT':'replica','Oobleck':'template','TrainMover':'standby','DejaVu':'failure','Llumnix':'migration','ServerlessLLM':'migration','SCORPIO':'SLO','SLOMetrics':'goodput'}
rs={r['id']:r for r in json.loads((ROOT/'文献元数据.json').read_text(encoding='utf-8'))}
out=[]
for alias,key in KEYS.items():
 r=rs[alias]; reader=PdfReader(str(ROOT/r['pdf_file'])); found=[]
 for i,page in enumerate(reader.pages):
  t=re.sub(r'\s+',' ',page.extract_text() or '')
  hit=re.search(re.escape(key),t,re.I)
  if hit:
   found.append({'pdf_page':i+1,'keyword':key,'excerpt':t[max(0,hit.start()-120):hit.end()+650]})
   if len(found)>=2:break
 out.append({'id':alias,'source':r['url'],'passages':found})
(Path(__file__).parent/'来源核读摘录.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
for x in out:print(json.dumps({'id':x['id'],'passage':x['passages'][-1:]},ensure_ascii=False))
