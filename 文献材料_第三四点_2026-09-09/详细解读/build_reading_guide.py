from pathlib import Path
from urllib.parse import unquote,urlparse
import json,re,html
import markdown
from markdown.extensions.toc import slugify_unicode

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
chapters=sorted(HERE.glob('0[1-7]_*.md'))
units=[];links=[];broken=[];source_ids=set()
for p in chapters:
 t=p.read_text(encoding='utf-8')
 for code,title in re.findall(r'^## ([34][abc]\.\d+) (.+)$',t,re.M):
  units.append({'id':code,'title':title,'chapter':p.name})
 for label,target in re.findall(r'\[([^\]]+)\]\(([^)]+)\)',t):
  links.append({'file':p.name,'label':label,'target':target})
  if not urlparse(target).scheme and not target.startswith('#'):
   local=(p.parent/unquote(target.split('#')[0])).resolve()
   if not local.is_file():broken.append({'file':p.name,'target':target})
   if local.suffix=='.pdf':source_ids.add(local.stem)
expected={f'{g}.{i}' for g,n in [('3a',6),('3b',6),('3c',5),('4a',5),('4b',6),('4c',7)] for i in range(1,n+1)}
assert {u['id'] for u in units}==expected
assert not broken,broken
intro='''# 第三、第四点：知识要点详细解读

整理日期：2026-09-09。对应截图的“计算与模型执行优化”和“大规模集群可靠性与容错”，共 **35个知识要点、6个专题章节**，另附术语、公式与横向比较。

解读依据已归档的原始论文、关键机制段落及官方文档，按“问题与定义—工作机制—示例—适用条件与代价—评价指标—文献依据”展开。它是一份知识讲解，不是对77篇论文逐篇全文翻译，也不声称复现了实验。文中算例是明确设定条件的教学示例；工程建议标明为综合分析。

- [打开网页合订版](知识要点详细解读.html)：侧边目录、章节跳转、打印样式，全文可用浏览器查找。
- [打开Markdown合订版](知识要点详细解读_合订版.md)：便于复制、编辑与继续扩写。
- [返回文献总索引](../README_文献总索引.md)。

## 分章阅读与覆盖清单

'''
for p in chapters:
 title=p.read_text(encoding='utf-8').splitlines()[0].lstrip('# ')
 intro+=f'### [{title}]({p.name})\n\n'
 selected=[u for u in units if u['chapter']==p.name]
 if selected:
  for u in selected:intro+=f'- {u["id"]} {u["title"]}\n'
 else:intro+='- 术语速查、简化公式、易混淆概念与报告评价模板。\n'
 intro+='\n'
intro+='''## 阅读顺序建议

先读3b.1理解请求生命周期，再读3a理解计算成本；随后读3c的另一类迭代计算。第四点先读4a建立故障分类，再读4b理解训练状态，最后读4c理解在线请求的恢复语义。准备报告时，可先看每章最后的组合关系或评价框架，再深入具体小节。

## 来源与核验

每个知识要点均附对应论文或官方文档；论文链接指向资料库中的原始PDF。辅助文件“来源核读摘录.json”保留自动提取的关键词窗口及PDF页码，供回溯定位，可能含排版识别误差，不宜直接引用为论文原文。它不是逐项结论的完整证据表；正文避免转引未经复核的实验性能倍数。

新增FP8缩放、vLLM前缀缓存设计两份官方页面，并修复原资料中三个PyTorch文档的网页跳转，正文已保存在上级“官方工程文档”文件夹。stable/latest网页会变化，涉及API行为时应核对实际版本。
'''
(HERE/'00_阅读入口.md').write_text(intro,encoding='utf-8')
parts=['# 第三、第四点知识要点详细解读\n\n2026-09-09 · 35个知识要点 · 基于原始论文与官方文档\n\n以下算例均为教学示例，非论文实测。每节提供文献链接。\n\n[TOC]\n']
for p in chapters:
 t=p.read_text(encoding='utf-8')
 # Make chapter h2, point h3 and preserve all relative citation links.
 t=re.sub(r'^(#{1,5}) ',r'\1# ',t,flags=re.M)
 parts.append(t)
full='\n\n---\n\n'.join(parts)
file_toc='\n'.join('- ['+p.read_text(encoding='utf-8').splitlines()[0].lstrip('# ')+']('+p.name+')' for p in chapters)
(HERE/'知识要点详细解读_合订版.md').write_text(full.replace('[TOC]',file_toc),encoding='utf-8')
md=markdown.Markdown(extensions=['tables','fenced_code','toc'],extension_configs={'toc':{'slugify':slugify_unicode,'toc_depth':'2-3'}})
body=md.convert(full);body=re.sub(r'<div class="toc">.*?</div>','',body,count=1,flags=re.S)
style='''*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:22px}body{margin:0;background:#f3f5f8;color:#202b39;font:17px/1.85 system-ui,"Microsoft YaHei",sans-serif}aside{position:fixed;inset:0 auto 0 0;width:300px;overflow:auto;padding:24px 18px;background:#102b46;color:#e2ebf3}aside h2{font-size:19px;margin:0 0 12px}aside a{color:#d6e4f2;text-decoration:none}aside li{margin:8px 0;line-height:1.5;font-size:13px}aside ul{padding-left:18px}aside>.toc>ul{padding-left:12px}main{margin:32px 35px 50px 335px;max-width:1080px;background:white;border:1px solid #dfe5ec;border-radius:10px;padding:44px 52px}h1{font-size:32px;line-height:1.4}h2{font-size:26px;color:#153c60;border-bottom:2px solid #d7e2ed;padding:14px 0}h3{font-size:21px;margin-top:40px;color:#174b74}a{color:#1564a6;overflow-wrap:anywhere}p{margin:16px 0}code{font:14px/1.7 Consolas,monospace;background:#edf3f8;padding:3px 5px;border-radius:4px;white-space:normal;overflow-wrap:anywhere}table{border-collapse:collapse;width:100%;font-size:14px;margin:24px 0}th,td{border:1px solid #dce3eb;padding:10px;vertical-align:top}th{background:#eef4f9;text-align:left}hr{border:0;border-top:1px solid #dfe5ed;margin:42px 0}.toplinks{font-size:14px;color:#607487}.tools{margin-bottom:15px;font-size:13px}button{cursor:pointer;padding:7px 12px;background:#e6eef6;border:0;border-radius:4px;color:#173c5b}@media(max-width:1050px){aside{position:static;width:auto;max-height:320px}main{margin:18px;padding:24px}table{display:block;overflow-x:auto}h1{font-size:26px}}@media print{aside,.tools{display:none}body{background:white;font-size:11pt}main{margin:0;padding:0;border:0;max-width:none}h2,h3{break-after:avoid}table{font-size:9pt}a{color:inherit}tr{break-inside:avoid}}'''
page='<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>第三、第四点知识要点详细解读</title><style>'+style+'</style></head><body><aside><h2>知识要点详细解读</h2><p class="tools">35个要点 · 6个专题<br>Ctrl+F 查找全文</p>'+md.toc+'</aside><main><div class="tools"><a href="00_阅读入口.md">阅读入口</a> · <a href="../README_文献总索引.md">文献资料库</a> · <button onclick="window.print()">打印</button></div>'+body+'</main></body></html>'
(HERE/'知识要点详细解读.html').write_text(page,encoding='utf-8')
report={'knowledge_points':len(units),'chapters':6,'distinct_local_paper_references':len(source_ids),'local_and_web_citation_links':len(links),'broken_local_links':broken,'chinese_characters':len(re.findall(r'[\u4e00-\u9fff]',full)),'units':units}
(HERE/'覆盖与链接核验.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
# Update the existing entry points without altering the original paper archive.
rp=ROOT/'README_文献总索引.md';rt=rp.read_text(encoding='utf-8')
docs=json.loads((ROOT/'官方文档元数据.json').read_text(encoding='utf-8'));n=sum(r.get('status')=='saved' for r in docs)
rt=re.sub(r'\d+ 份官方工程文档',f'{n} 份官方工程文档',rt)
entry='- [35个知识要点详细解读](详细解读/00_阅读入口.md) · [网页合订版](详细解读/知识要点详细解读.html)\n'
if entry not in rt:rt=rt.replace('## 数量与覆盖',entry+'\n## 数量与覆盖')
for d in docs:
 if d['id'] in ['NVIDIA_FP8_Delayed','vLLM_Prefix_Design'] and f'**{d["id"]}**' not in rt:
  line=f'- **{d["id"]}**（{d["group"]}）：{d["reading_note"]} [官网]({d["url"]}) · [网页快照]({d["snapshot"]})\n'
  rt=rt.replace('## 下载与核验说明',line+'\n## 下载与核验说明')
rp.write_text(rt,encoding='utf-8')
hp=ROOT/'文献索引.html';ht=hp.read_text(encoding='utf-8').replace('11份官方工程文档',f'{n}份官方工程文档')
if '详细解读/知识要点详细解读.html' not in ht:ht=ht.replace('</header>','<p><a href="详细解读/知识要点详细解读.html">新增：35个知识要点详细解读</a></p></header>')
hp.write_text(ht,encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='units'},ensure_ascii=False))
