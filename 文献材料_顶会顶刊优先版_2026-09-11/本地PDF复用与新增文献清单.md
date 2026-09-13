# 本地 PDF 复用与新增文献清单

新版优先复用原资料库中的 PDF，并以正式 proceedings 页面作为发表状态依据。下列链接可直接打开已有本地文件；“新增清单”列出本轮检索发现、旧库尚未收录的高优先级正式论文。其中 29 篇一级论文已经下载，入口及实际 PDF 来源见[新增 PDF 下载结果](新增PDF/README.md)；二级论文保留正式页面链接，可在扩写相应小节时继续补充。

## 已有本地 PDF：6.3

### 低精度、算子与编译

- 混合精度与量化：[Mixed Precision Training](../文献材料_第三四点_2026-09-09/3a_低精度_算子_编译优化/MixedPrecision.pdf)、[LLM.int8()](../文献材料_第三四点_2026-09-09/3a_低精度_算子_编译优化/LLMint8.pdf)、[GPTQ](../文献材料_第三四点_2026-09-09/3a_低精度_算子_编译优化/GPTQ.pdf)、[SmoothQuant](../文献材料_第三四点_2026-09-09/3a_低精度_算子_编译优化/SmoothQuant.pdf)、[AWQ](../文献材料_第三四点_2026-09-09/3a_低精度_算子_编译优化/AWQ.pdf)、[FP8 PTQ](../文献材料_第三四点_2026-09-09/3a_低精度_算子_编译优化/FP8PTQ.pdf)。
- 注意力内核：[FlashAttention](../文献材料_第三四点_2026-09-09/3a_低精度_算子_编译优化/FlashAttention.pdf)、[FlashAttention-2](../文献材料_第三四点_2026-09-09/3a_低精度_算子_编译优化/FlashAttention2.pdf)、[FlashAttention-3](../文献材料_第三四点_2026-09-09/3a_低精度_算子_编译优化/FlashAttention3.pdf)、[FlashDecoding++](../文献材料_第三四点_2026-09-09/3b_大模型推理加速/FlashDecoding.pdf)。
- 编译：[TVM](../文献材料_第三四点_2026-09-09/3a_低精度_算子_编译优化/TVM.pdf)、[Ansor](../文献材料_第三四点_2026-09-09/3a_低精度_算子_编译优化/Ansor.pdf)、[TensorIR](../文献材料_第三四点_2026-09-09/3a_低精度_算子_编译优化/TensorIR.pdf)、[TASO](../文献材料_第三四点_2026-09-09/3a_低精度_算子_编译优化/TASO.pdf)、[Triton](../文献材料_第三四点_2026-09-09/3a_低精度_算子_编译优化/Triton.pdf)。Triton 属 MAPL 2019 workshop，只作为实现补充。

### 大模型推理

- 调度和 KV Cache：[Orca](../文献材料_第三四点_2026-09-09/3b_大模型推理加速/Orca.pdf)、[PagedAttention](../文献材料_第三四点_2026-09-09/3b_大模型推理加速/PagedAttention.pdf)、[Sarathi-Serve](../文献材料_第三四点_2026-09-09/3b_大模型推理加速/SarathiServe.pdf)、[SGLang](../文献材料_第三四点_2026-09-09/3b_大模型推理加速/SGLang.pdf)。
- P/D 分离：[DistServe](../文献材料_第三四点_2026-09-09/3b_大模型推理加速/DistServe.pdf)、[Splitwise](../文献材料_第三四点_2026-09-09/3b_大模型推理加速/Splitwise.pdf)。[P/D-Serve](../文献材料_第三四点_2026-09-09/3b_大模型推理加速/PDServe.pdf)仍是预印本，只作部署案例。
- 推测解码：[Speculative Decoding](../文献材料_第三四点_2026-09-09/3b_大模型推理加速/SpeculativeDecoding.pdf)、[SpecInfer](../文献材料_第三四点_2026-09-09/3b_大模型推理加速/SpecInfer.pdf)、[EAGLE](../文献材料_第三四点_2026-09-09/3b_大模型推理加速/EAGLE.pdf)、[Medusa](../文献材料_第三四点_2026-09-09/3b_大模型推理加速/Medusa.pdf)。[Speculative Sampling](../文献材料_第三四点_2026-09-09/3b_大模型推理加速/SpeculativeSampling.pdf)仅作同期预印本。

### Diffusion 与 HPC-AI

- 采样和蒸馏：[DDIM](../文献材料_第三四点_2026-09-09/3c_Diffusion与HPC_AI/DDIM.pdf)、[DPM-Solver](../文献材料_第三四点_2026-09-09/3c_Diffusion与HPC_AI/DPMSolver.pdf)、[DPM-Solver++](../文献材料_第三四点_2026-09-09/3c_Diffusion与HPC_AI/DPMSolverPlus.pdf)、[Progressive Distillation](../文献材料_第三四点_2026-09-09/3c_Diffusion与HPC_AI/ProgressiveDistillation.pdf)、[Consistency Models](../文献材料_第三四点_2026-09-09/3c_Diffusion与HPC_AI/ConsistencyModels.pdf)。
- 缓存与并行：[DeepCache](../文献材料_第三四点_2026-09-09/3c_Diffusion与HPC_AI/DeepCache.pdf)、[TeaCache](../文献材料_第三四点_2026-09-09/3c_Diffusion与HPC_AI/TeaCache.pdf)、[DistriFusion](../文献材料_第三四点_2026-09-09/3c_Diffusion与HPC_AI/DistriFusion.pdf)。
- 代理与工作流：[FNO](../文献材料_第三四点_2026-09-09/3c_Diffusion与HPC_AI/FNO.pdf)、[DeepONet](../文献材料_第三四点_2026-09-09/3c_Diffusion与HPC_AI/DeepONet.pdf)、[GraphCast](../文献材料_第三四点_2026-09-09/3c_Diffusion与HPC_AI/GraphCast.pdf)、[SmartSim](../文献材料_第三四点_2026-09-09/3c_Diffusion与HPC_AI/SmartSim.pdf)、[Streaming AI-HPC](../文献材料_第三四点_2026-09-09/3c_Diffusion与HPC_AI/StreamingAIHPC.pdf)、[Colmena Exascale](../文献材料_第三四点_2026-09-09/3c_Diffusion与HPC_AI/ColmenaExascale.pdf)。

## 已有本地 PDF：6.4

- 故障特征和诊断：[Datacenter Characterization](../文献材料_第三四点_2026-09-09/4a_监控_故障诊断/DatacenterCharacterization.pdf)、[MegaScale](../文献材料_第三四点_2026-09-09/4a_监控_故障诊断/MegaScale.pdf)、[TPUv4 Resiliency](../文献材料_第三四点_2026-09-09/4a_监控_故障诊断/TPUResiliency.pdf)、[SuperBench](../文献材料_第三四点_2026-09-09/4a_监控_故障诊断/SuperBench.pdf)、[Minder](../文献材料_第三四点_2026-09-09/4a_监控_故障诊断/Minder.pdf)、[Holmes](../文献材料_第三四点_2026-09-09/4a_监控_故障诊断/Holmes.pdf)、[SDCs in the Wild](../文献材料_第三四点_2026-09-09/4a_监控_故障诊断/SDCsInTheWild.pdf)。
- 检查点和训练恢复：[CheckFreq](../文献材料_第三四点_2026-09-09/4b_检查点_训练恢复/CheckFreq.pdf)、[Check-N-Run](../文献材料_第三四点_2026-09-09/4b_检查点_训练恢复/CheckNRun.pdf)、[Gemini](../文献材料_第三四点_2026-09-09/4b_检查点_训练恢复/Gemini.pdf)、[ByteCheckpoint](../文献材料_第三四点_2026-09-09/4b_检查点_训练恢复/ByteCheckpoint.pdf)、[SWIFT](../文献材料_第三四点_2026-09-09/4b_检查点_训练恢复/SWIFT.pdf)、[TrainMover](../文献材料_第三四点_2026-09-09/4b_检查点_训练恢复/TrainMover.pdf)、[Oobleck](../文献材料_第三四点_2026-09-09/4b_检查点_训练恢复/Oobleck.pdf)、[ReCycle](../文献材料_第三四点_2026-09-09/4b_检查点_训练恢复/ReCycle.pdf)、[Bamboo](../文献材料_第三四点_2026-09-09/4b_检查点_训练恢复/Bamboo.pdf)、[MoEvement](../文献材料_第三四点_2026-09-09/4b_检查点_训练恢复/MoEvement.pdf)。
- 在线推理可靠性：[DéjàVu](../文献材料_第三四点_2026-09-09/4c_推理高可用_SLO/DejaVu.pdf)、[Llumnix](../文献材料_第三四点_2026-09-09/4c_推理高可用_SLO/Llumnix.pdf)、[ServerlessLLM](../文献材料_第三四点_2026-09-09/4c_推理高可用_SLO/ServerlessLLM.pdf)、[GhostServe](../文献材料_第三四点_2026-09-09/4c_推理高可用_SLO/GhostServe.pdf)、[JITServe](../文献材料_第三四点_2026-09-09/4c_推理高可用_SLO/JITServe.pdf)、[KUNSERVE](../文献材料_第三四点_2026-09-09/4c_推理高可用_SLO/KunServe.pdf)。

## 本轮新增：优先补入的正式论文

下表中的“一级”论文已全部补入 `新增PDF`；它们直接替换旧版中的预印本主引或填补原大纲的空白。“二级”论文用于扩充比较维度。

### 6.3 新增清单

| 优先级 | 论文与正式出处 | 用途 |
|---|---|---|
| 一级 | [Scaling FP8 training to trillion-token LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/hash/f48b5133e89854a9e97cc22a6db83f25-Abstract-Conference.html)（ICLR 2025） | 替换 FP8-LM，支撑长程大模型 FP8 稳定性。 |
| 一级 | [COAT](https://proceedings.iclr.cc/paper_files/paper/2025/hash/6ac807c9b296964409b277369e55621a-Abstract-Conference.html)（ICLR 2025） | 补齐激活和优化器状态 FP8 化。 |
| 一级 | [The Case for 4-bit Precision](https://proceedings.mlr.press/v202/dettmers23a.html)（ICML 2023） | 建立位宽、模型规模和精度边界。 |
| 一级 | [QServe](https://proceedings.mlsys.org/paper_files/paper/2025/hash/fbe2b2f74a2ece8070d8fb073717bda6-Abstract-Conference.html)（MLSys 2025） | 将 W4A8KV4 与真实服务吞吐连接起来。 |
| 一级 | [Apollo](https://proceedings.mlsys.org/paper_files/paper/2022/hash/e175e8a86d28d935be4f43719651f86d-Abstract.html)（MLSys 2022） | 直接支撑算子融合。 |
| 一级 | [Welder](https://www.usenix.org/conference/osdi23/presentation/shi)（OSDI 2023） | 跨算子 tile-graph 和内存调度。 |
| 一级 | [PyTorch 2](https://doi.org/10.1145/3620665.3640366)（ASPLOS 2024） | 动态图捕获到编译执行的生产路径。 |
| 一级 | [FlashInfer](https://proceedings.mlsys.org/paper_files/paper/2025/hash/dbf02b21d77409a2db30e56866a8ab3a-Abstract-Conference.html)（MLSys 2025） | 推理侧可组合注意力内核。 |
| 一级 | [Mooncake](https://www.usenix.org/conference/fast25/presentation/qin)（FAST 2025，Best Paper） | 集群级 KV Cache 与 P/D 分离。 |
| 一级 | [Prompt Cache](https://proceedings.mlsys.org/paper_files/paper/2024/hash/a66caa1703fe34705a4368c3014c1966-Abstract-Conference.html)（MLSys 2024） | 前缀模块化复用。 |
| 一级 | [IMPRESS](https://www.usenix.org/conference/fast25/presentation/chen-weijian-impress)（FAST 2025） | 多级前缀 KV 存储。 |
| 一级 | [UniPC](https://proceedings.neurips.cc/paper_files/paper/2023/hash/9c2aa1e456ea543997f6927295196381-Abstract-Conference.html)（NeurIPS 2023） | 少步 diffusion 求解器。 |
| 一级 | [Improved Training Technique for Latent Consistency Models](https://proceedings.iclr.cc/paper_files/paper/2025/hash/9541101fbc2f24bce5f2462b95db88c4-Abstract-Conference.html)（ICLR 2025） | 替换 LCM 预印本的主证据。 |
| 一级 | [Learning-to-Cache](https://proceedings.neurips.cc/paper_files/paper/2024/hash/f0b1515be276f6ba82b4f2b25e50bef0-Abstract-Conference.html)（NeurIPS 2024） | 将特征缓存扩展到 DiT。 |
| 一级 | [PipeFusion](https://proceedings.nips.cc/paper_files/paper/2025/hash/8da04a60948be713dc766f0c7e3a5b1f-Abstract-Conference.html)（NeurIPS 2025） | 支撑新增的多 GPU diffusion 小节。 |
| 一级 | [Neural Operator](https://www.jmlr.org/beta/papers/v24/21-1524.html)（JMLR 2023） | 代理模型的统一概念和理论。 |
| 二级 | [Atom](https://proceedings.mlsys.org/paper_files/paper/2024/hash/5edb57c05c81d04beb716ef1d542fe9e-Abstract-Conference.html)（MLSys 2024）、[QuaRot](https://proceedings.neurips.cc/paper_files/paper/2024/hash/b5b939436789f76f08b9d0da5e81af7c-Abstract-Conference.html)（NeurIPS 2024）、[SpinQuant](https://proceedings.iclr.cc/paper_files/paper/2025/hash/e5b1c0d4866f72393c522c8a00eed4eb-Abstract-Conference.html)（ICLR 2025） | 补充低比特系统协同和旋转量化。 |
| 二级 | [AStitch](https://doi.org/10.1145/3503222.3507723)（ASPLOS 2022）、[ROLLER](https://www.usenix.org/conference/osdi22/presentation/zhu)（OSDI 2022） | 补充融合与构造式张量编译。 |
| 二级 | [Sequoia](https://proceedings.neurips.cc/paper_files/paper/2024/hash/ea1f5f0878d43ff4fb8bf64ef4a2326c-Abstract-Conference.html)（NeurIPS 2024） | 推测解码树和硬件感知。 |
| 二级 | [AI-Enabling Workloads on Large-Scale GPU-Accelerated System](https://doi.org/10.1109/HPCA53966.2022.00093)（HPCA 2022） | HPC-AI 资源行为和评价证据。 |

### 6.4 新增清单

| 优先级 | 论文与正式出处 | 用途 |
|---|---|---|
| 一级 | [Robust LLM Training Infrastructure at ByteDance](https://doi.org/10.1145/3731569.3764838)（SOSP 2025） | 多层监控、隔离、替换和恢复的生产闭环。 |
| 一级 | [GREYHOUND](https://www.usenix.org/conference/atc25/presentation/wu-tianyuan)（USENIX ATC 2025） | 慢卡、慢链路和灰故障检测。 |
| 一级 | [Mycroft](https://doi.org/10.1145/3731569.3764848)（SOSP 2025） | 集合通信中的异常链路根因定位。 |
| 一级 | [Understanding Stragglers in Large Model Training Using What-if Analysis](https://www.usenix.org/conference/osdi25/presentation/lin-jinkun)（OSDI 2025） | 关键路径上的真实落后者定位。 |
| 一级 | [EROICA](https://www.usenix.org/conference/nsdi26/presentation/guan-yu)（NSDI 2026） | 十万 GPU 规模在线性能诊断。 |
| 一级 | [PCcheck](https://doi.org/10.1145/3669940.3707255)（ASPLOS 2025） | 异步检查点新主引。 |
| 一级 | [DataStates-LLM](https://doi.org/10.1145/3625549.3658685)（HPDC 2024，Best Paper） | 延迟、异步持久化。 |
| 一级 | [LowDiff](https://doi.org/10.1145/3712285.3759891)（SC 2025） | 通用差分检查点，替代 TierCheck 主引。 |
| 一级 | [Universal Checkpointing](https://www.usenix.org/conference/atc25/presentation/lian)（USENIX ATC 2025） | 跨并行配置的检查点重载。 |
| 一级 | [SpotServe](https://doi.org/10.1145/3620665.3640411)（ASPLOS 2024） | 抢占与实例故障后的状态恢复、重新并行化。 |
| 一级 | [BlitzScale](https://www.usenix.org/conference/osdi25/presentation/zhang-dingyan)（OSDI 2025） | 突发负载下快速扩容。 |
| 一级 | [AdaServe](https://doi.org/10.1145/3767295.3769315)（EuroSys 2026） | 多类型、多 SLO 请求调度。 |
| 一级 | [ServeGen](https://www.usenix.org/conference/nsdi26/presentation/xiang-servegen)（NSDI 2026） | 真实生成式 AI 服务负载刻画与生成。 |
| 二级 | [FLARE](https://www.usenix.org/conference/nsdi26/presentation/cui)（NSDI 2026）、[Attack of the Bubbles](https://www.usenix.org/conference/nsdi26/presentation/wu-tianyuan)（NSDI 2026） | 补充训练发散诊断和流水线落后者缓解。 |
| 二级 | [AdaCheck](https://www.usenix.org/conference/fast26/presentation/liu-weijie)（FAST 2026）、[Checkmate](https://www.usenix.org/conference/nsdi26/presentation/bhardwaj)（NSDI 2026） | 检查点压缩和逐迭代保存。 |
| 二级 | [Varuna](https://doi.org/10.1145/3492321.3519584)（EuroSys 2022）、[Sailor](https://doi.org/10.1145/3731569.3764839)（SOSP 2025）、[Di-PS](https://www.usenix.org/conference/nsdi26/presentation/li-shengwei)（NSDI 2026） | 资源动态变化、重配置和跨集群训练。 |
| 二级 | [HydraServe](https://www.usenix.org/conference/nsdi26/presentation/lou)（NSDI 2026） | 冷启动与服务容量恢复。 |

## 旧库中保留但不作主引的 PDF

[FP8 Formats](../文献材料_第三四点_2026-09-09/3a_低精度_算子_编译优化/FP8Formats.pdf)、[FP8-LM](../文献材料_第三四点_2026-09-09/3a_低精度_算子_编译优化/FP8LM.pdf)、[Microscaling](../文献材料_第三四点_2026-09-09/3a_低精度_算子_编译优化/Microscaling.pdf)、[Latent Consistency Models](../文献材料_第三四点_2026-09-09/3c_Diffusion与HPC_AI/LatentConsistency.pdf)、[TierCheck](../文献材料_第三四点_2026-09-09/4b_检查点_训练恢复/TierCheck.pdf)、[InMemoryHP/REFT](../文献材料_第三四点_2026-09-09/4b_检查点_训练恢复/InMemoryHP.pdf)、[P/D-Serve](../文献材料_第三四点_2026-09-09/3b_大模型推理加速/PDServe.pdf)、[SLOMetrics](../文献材料_第三四点_2026-09-09/4c_推理高可用_SLO/SLOMetrics.pdf)、[SCORPIO](../文献材料_第三四点_2026-09-09/4c_推理高可用_SLO/SCORPIO.pdf)、[KevlarFlow](../文献材料_第三四点_2026-09-09/4c_推理高可用_SLO/KevlarFlow.pdf)、[LUMEN](../文献材料_第三四点_2026-09-09/4c_推理高可用_SLO/LUMEN.pdf)和[Concordia](../文献材料_第三四点_2026-09-09/4c_推理高可用_SLO/Concordia.pdf)可用于技术演进或前沿展望，但正文必须注明其实际发表状态。
