from collect import *

DOCS=[
('NVIDIA_MixedPrecision','3a','https://docs.nvidia.com/deeplearning/performance/mixed-precision-training/index.html','混合精度训练与损失缩放官方指南。'),
('DCGM_Diagnostics','4a','https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/dcgm-diagnostics.html','GPU诊断与健康检查。'),
('NsightSystems','4a','https://docs.nvidia.com/nsight-systems/UserGuide/index.html','CPU、CUDA和通信时间线的性能分析。'),
('PyTorch_Profiler','4a','https://docs.pytorch.org/docs/stable/profiler.html','算子耗时、形状和内存分析接口。'),
('PyTorch_DCP','4b','https://docs.pytorch.org/docs/stable/distributed.checkpoint.html','分布式检查点API与重分片加载。'),
('PyTorch_AsyncDCP','4b','https://docs.pytorch.org/tutorials/recipes/distributed_async_checkpoint_recipe.html','异步检查点的实现与内存开销。'),
('PyTorch_Elastic','4b','https://docs.pytorch.org/docs/stable/elastic/run.html','弹性启动、worker故障与恢复语义。'),
('RayServe_FaultTolerance','4c','https://docs.ray.io/en/latest/serve/production-guide/fault-tolerance.html','副本、控制器与服务层容错边界。'),
('RayServe_LoadShedding','4c','https://docs.ray.io/en/latest/serve/production-guide/best-practices.html','请求队列、负载削减、超时与重试。'),
('SmartSim_Experiments','3c','https://www.craylabs.org/docs/experiment.html','仿真与AI组件的部署和通信。'),
('DeepDriveMD_Docs','3c','https://deepdrivemd-pipeline.readthedocs.io/en/latest/','同步与异步仿真学习推理工作流。'),
]
def doc(item):
    alias,group,url,note=item
    out=ROOT/'官方工程文档';out.mkdir(exist_ok=True)
    r=dict(id=alias,group=group,url=url,reading_note=note,kind='official_document',accessed='2026-09-09')
    try:
        data,final,ct=get(url);p=Page(data.decode('utf-8',errors='replace'));r['title']=p.title
        path=out/(alias+'.html');path.write_bytes(data)
        r.update(status='saved',snapshot=path.relative_to(ROOT).as_posix(),final_url=final,bytes=len(data))
    except Exception as e:r.update(status='failed',error=str(e),title=alias)
    print(alias+' '+r['status'],flush=True)
    return r
if __name__=='__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool: rs=list(pool.map(doc,DOCS))
    (ROOT/'官方文档元数据.json').write_text(json.dumps(rs,ensure_ascii=False,indent=2),encoding='utf-8')
    for s in (ROOT/'seeds.txt').read_text(encoding='utf-8').splitlines():
        if s.split('|')[1] in ['TASO','Triton']: collect(s.split('|'))
