from pathlib import Path
from urllib.request import urlopen,Request
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import json,re
ROOT=Path(__file__).resolve().parents[1]
rs=json.loads((ROOT/'官方文档元数据.json').read_text(encoding='utf-8'))
targets=[r for r in rs if r['id'] in ['PyTorch_DCP','PyTorch_Elastic','PyTorch_Profiler']]
targets += [dict(id='NVIDIA_FP8_Delayed',group='3a',url='https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/features/low_precision_training/fp8_delayed_scaling/fp8_delayed_scaling.html',reading_note='FP8张量缩放与历史绝对最大值。'),dict(id='vLLM_Prefix_Design',group='3b',url='https://docs.vllm.ai/en/latest/design/prefix_caching/',reading_note='前缀KV缓存的块哈希、复用条件与管理。')]
for r in targets:
 try:
  url=r['url']
  for _ in range(5):
   with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=40) as response:data=response.read();url=response.url
   soup=BeautifulSoup(data,'html.parser');refresh=soup.find('meta',attrs={'http-equiv':re.compile('refresh',re.I)})
   if not refresh:break
   m=re.search(r'url\s*=\s*(.*)',refresh.get('content',''),re.I)
   if not m:break
   url=urljoin(url,m[1].strip(' \"\''))
  if refresh:raise ValueError('Unresolved redirect')
  out=ROOT/'官方工程文档'/(r['id']+'.html');out.write_bytes(data)
  r.update(title=soup.title.get_text() if soup.title else r['id'],status='saved',snapshot=out.relative_to(ROOT).as_posix(),bytes=len(data),final_url=url,kind='official_document',accessed='2026-09-09')
  if not any(x['id']==r['id'] for x in rs):rs.append(r)
  print(r['id']+' '+str(len(data))+' '+url,flush=True)
 except Exception as e:print(r['id']+' ERROR '+str(e),flush=True)
(ROOT/'官方文档元数据.json').write_text(json.dumps(rs,ensure_ascii=False,indent=2),encoding='utf-8')
