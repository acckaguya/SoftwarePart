# 第三、第四点文献资料库

整理日期：2026-09-09。共 **77 篇论文PDF、13 份官方工程文档**，PDF合计约 **331.3 MB**。

> **第二轮筛选（2026-09-11）：** 按正式顶会/顶刊优先重新核验后的章节大纲、29 篇新增 PDF 和预印本降级清单，见[顶会顶刊优先版资料包](../文献材料_顶会顶刊优先版_2026-09-11/README.md)。

对应截图：第三点“计算与模型执行优化”、第四点“大规模集群可靠性与容错”。六个专题分别存放；每篇均保留来源链接、原站网页、中文选读说明和元数据。

- [阅读路线与报告写作建议](阅读路线与报告写作建议.md)：按报告小点安排先读论文与比较维度。
- [网页检索入口](文献索引.html)：可按关键词和专题筛选，并直接打开本地PDF。
- [BibTeX引用文件](references.bib)：用于Zotero、JabRef等文献管理软件。
- [结构化元数据](文献元数据.json)、[下载校验](下载校验.json)、[检索发现记录](检索记录.txt)。

这是检索与归档资料包，中文注释是选读导航，不代表逐篇全文精读或实验复现。arXiv按预印本标识引用；列表日期优先采用原站引用元数据，不将首次提交年份混作会议发表年份。2026年材料可用于跟进前沿，正式引用请核实具体版本与发表状态。

- [35个知识要点详细解读](详细解读/00_阅读入口.md) · [网页合订版](详细解读/知识要点详细解读.html)

## 数量与覆盖

| 子点 | 论文数 |
|---|---:|
| 3a_低精度_算子_编译优化 | 17 |
| 3b_大模型推理加速 | 13 |
| 3c_Diffusion与HPC_AI | 17 |
| 4a_监控_故障诊断 | 7 |
| 4b_检查点_训练恢复 | 12 |
| 4c_推理高可用_SLO | 11 |

## 论文索引

### 3a_低精度_算子_编译优化

- **MixedPrecision｜Mixed Precision Training**（2017/10/10；必读）
  - 用途：混合精度训练基础：低精度计算与关键状态保留高精度。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/1710.03740) · [本地PDF，12页](3a_低精度_算子_编译优化/MixedPrecision.pdf)
- **FP8Formats｜FP8 Formats for Deep Learning**（2022/09/12；必读）
  - 用途：FP8数值格式及训练与推理的数值设计。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2209.05433) · [本地PDF，9页](3a_低精度_算子_编译优化/FP8Formats.pdf)
- **FP8LM｜FP8-LM: Training FP8 Large Language Models**（2023/10/27；扩展）
  - 用途：大语言模型FP8训练的系统实现。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2310.18313) · [本地PDF，23页](3a_低精度_算子_编译优化/FP8LM.pdf)
- **LLMint8｜LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale**（2022/08/15；扩展）
  - 用途：INT8推理与离群特征处理。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2208.07339) · [本地PDF，20页](3a_低精度_算子_编译优化/LLMint8.pdf)
- **GPTQ｜GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers**（2022/10/31；必读）
  - 用途：面向大模型的训练后权重量化。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2210.17323) · [本地PDF，16页](3a_低精度_算子_编译优化/GPTQ.pdf)
- **SmoothQuant｜SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models**（2022/11/18；必读）
  - 用途：通过平滑激活离群值实现权重与激活量化。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2211.10438) · [本地PDF，13页](3a_低精度_算子_编译优化/SmoothQuant.pdf)
- **AWQ｜AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration**（2023/06/01；必读）
  - 用途：激活感知的低比特权重量化。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2306.00978) · [本地PDF，15页](3a_低精度_算子_编译优化/AWQ.pdf)
- **FP8PTQ｜Efficient Post-training Quantization with FP8 Formats**（2023/09/26；扩展）
  - 用途：FP8格式的训练后量化。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2309.14592) · [本地PDF，16页](3a_低精度_算子_编译优化/FP8PTQ.pdf)
- **Microscaling｜Post Training Quantization of Large Language Models with Microscaling Formats**（2024/05/12；扩展）
  - 用途：微缩放格式与多种量化方法组合。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2405.07135) · [本地PDF，18页](3a_低精度_算子_编译优化/Microscaling.pdf)
- **FlashAttention｜FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness**（2022/05/27；必读）
  - 用途：通过IO感知分块优化精确注意力。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2205.14135) · [本地PDF，34页](3a_低精度_算子_编译优化/FlashAttention.pdf)
- **FlashAttention2｜FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning**（2023/07/17；扩展）
  - 用途：注意力算子的工作划分与并行优化。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2307.08691) · [本地PDF，14页](3a_低精度_算子_编译优化/FlashAttention2.pdf)
- **FlashAttention3｜FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision**（2024/07/11；必读）
  - 用途：异步执行与低精度注意力内核。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2407.08608) · [本地PDF，22页](3a_低精度_算子_编译优化/FlashAttention3.pdf)
- **TVM｜TVM: An Automated End-to-End Optimizing Compiler for Deep Learning**（2018/02/12；必读）
  - 用途：端到端深度学习编译与硬件映射。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/1802.04799) · [本地PDF，16页](3a_低精度_算子_编译优化/TVM.pdf)
- **Ansor｜Ansor: Generating High-Performance Tensor Programs for Deep Learning**（2020/06/11；必读）
  - 用途：张量程序自动搜索与自动调优。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2006.06762) · [本地PDF，19页](3a_低精度_算子_编译优化/Ansor.pdf)
- **TensorIR｜TensorIR: An Abstraction for Automatic Tensorized Program Optimization**（2022/07/09；扩展）
  - 用途：张量程序中间表示与硬件张量化。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2207.04296) · [本地PDF，14页](3a_低精度_算子_编译优化/TensorIR.pdf)
- **TASO｜TASO: Optimizing Deep Learning Computation with Automatic Generation of Graph Substitutions**（2019；扩展）
  - 用途：自动生成图替换规则的计算图优化。
  - 来源类型/出处：SOSP 2019。
  - [原始页面](https://catalyst.cs.cmu.edu/projects/taso.html) · [本地PDF，16页](3a_低精度_算子_编译优化/TASO.pdf)
- **Triton｜Triton: An Intermediate Language and Compiler for Tiled Neural Network Computations**（2019；必读）
  - 用途：面向分块张量计算的语言与编译器。
  - 来源类型/出处：MAPL 2019。
  - [原始页面](https://research.ibm.com/publications/triton-an-intermediate-language-and-compiler-for-tiled-neural-network-computations) · [本地PDF，10页](3a_低精度_算子_编译优化/Triton.pdf)

### 3b_大模型推理加速

- **Orca｜Orca: A Distributed Serving System for Transformer-Based Generative Models**（2022；必读）
  - 用途：迭代级调度与选择性批处理，连续批处理的基础。
  - 来源类型/出处：16th USENIX Symposium on Operating Systems Design and Implementation (OSDI 22)。
  - [原始页面](https://www.usenix.org/conference/osdi22/presentation/yu) · [本地PDF，19页](3b_大模型推理加速/Orca.pdf)
- **PagedAttention｜Efficient Memory Management for Large Language Model Serving with PagedAttention**（2023/09/12；必读）
  - 用途：分页KV缓存与共享，vLLM核心论文。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2309.06180) · [本地PDF，16页](3b_大模型推理加速/PagedAttention.pdf)
- **SGLang｜SGLang: Efficient Execution of Structured Language Model Programs**（2023/12/12；必读）
  - 用途：结构化生成与RadixAttention前缀复用。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2312.07104) · [本地PDF，20页](3b_大模型推理加速/SGLang.pdf)
- **SarathiServe｜Taming Throughput-Latency Tradeoff in LLM Inference with Sarathi-Serve**（2024/03/04；必读）
  - 用途：分块Prefill与减小解码停顿的批调度。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2403.02310) · [本地PDF，18页](3b_大模型推理加速/SarathiServe.pdf)
- **DistServe｜DistServe: Disaggregating Prefill and Decoding for Goodput-optimized Large Language Model Serving**（2024/01/18；必读）
  - 用途：Prefill与Decode分离并以goodput优化部署。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2401.09670) · [本地PDF，18页](3b_大模型推理加速/DistServe.pdf)
- **Splitwise｜Splitwise: Efficient generative LLM inference using phase splitting**（2023/11/30；必读）
  - 用途：按推理阶段划分资源的架构设计。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2311.18677) · [本地PDF，15页](3b_大模型推理加速/Splitwise.pdf)
- **PDServe｜P/D-Serve: Serving Disaggregated Large Language Model at Scale**（2024/08/15；扩展）
  - 用途：规模化PD分离部署与恢复的工程经验。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2408.08147) · [本地PDF，15页](3b_大模型推理加速/PDServe.pdf)
- **SpeculativeDecoding｜Fast Inference from Transformers via Speculative Decoding**（2022/11/30；必读）
  - 用途：草稿模型与验证模型协同的推测解码。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2211.17192) · [本地PDF，13页](3b_大模型推理加速/SpeculativeDecoding.pdf)
- **SpeculativeSampling｜Accelerating Large Language Model Decoding with Speculative Sampling**（2023/02/02；扩展）
  - 用途：保持目标采样分布的推测采样机制。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2302.01318) · [本地PDF，11页](3b_大模型推理加速/SpeculativeSampling.pdf)
- **Medusa｜Medusa: Simple LLM Inference Acceleration Framework with Multiple Decoding Heads**（2024/01/19；扩展）
  - 用途：多解码头生成候选token以加速推理。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2401.10774) · [本地PDF，27页](3b_大模型推理加速/Medusa.pdf)
- **EAGLE｜EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty**（2024/01/26；扩展）
  - 用途：基于特征预测的推测解码。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2401.15077) · [本地PDF，13页](3b_大模型推理加速/EAGLE.pdf)
- **SpecInfer｜SpecInfer: Accelerating Generative Large Language Model Serving with Tree-based Speculative Inference and Verification**（2023/05/16；扩展）
  - 用途：树状候选生成与并行验证。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2305.09781) · [本地PDF，18页](3b_大模型推理加速/SpecInfer.pdf)
- **FlashDecoding｜FlashDecoding++: Faster Large Language Model Inference on GPUs**（2023/11/02；扩展）
  - 用途：解码阶段的算子与执行优化。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2311.01282) · [本地PDF，16页](3b_大模型推理加速/FlashDecoding.pdf)

### 3c_Diffusion与HPC_AI

- **DDIM｜Denoising Diffusion Implicit Models**（2020/10/06；必读）
  - 用途：扩散采样加速的基础方法。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2010.02502) · [本地PDF，22页](3c_Diffusion与HPC_AI/DDIM.pdf)
- **DPMSolver｜DPM-Solver: A Fast ODE Solver for Diffusion Probabilistic Model Sampling in Around 10 Steps**（2022/06/02；必读）
  - 用途：以专用高阶求解器减少采样步数。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2206.00927) · [本地PDF，31页](3c_Diffusion与HPC_AI/DPMSolver.pdf)
- **DPMSolverPlus｜DPM-Solver++: Fast Solver for Guided Sampling of Diffusion Probabilistic Models**（2022/11/02；扩展）
  - 用途：面向引导扩散采样的高阶求解。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2211.01095) · [本地PDF，24页](3c_Diffusion与HPC_AI/DPMSolverPlus.pdf)
- **ProgressiveDistillation｜Progressive Distillation for Fast Sampling of Diffusion Models**（2022/02/01；必读）
  - 用途：通过渐进蒸馏减少生成步骤。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2202.00512) · [本地PDF，21页](3c_Diffusion与HPC_AI/ProgressiveDistillation.pdf)
- **ConsistencyModels｜Consistency Models**（2023/03/02；必读）
  - 用途：一致性模型与少步生成。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2303.01469) · [本地PDF，42页](3c_Diffusion与HPC_AI/ConsistencyModels.pdf)
- **LatentConsistency｜Latent Consistency Models: Synthesizing High-Resolution Images with Few-Step Inference**（2023/10/06；扩展）
  - 用途：潜空间一致性模型与少步文生图。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2310.04378) · [本地PDF，18页](3c_Diffusion与HPC_AI/LatentConsistency.pdf)
- **DeepCache｜DeepCache: Accelerating Diffusion Models for Free**（2023/12/01；必读）
  - 用途：利用相邻去噪步骤的特征冗余进行缓存复用。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2312.00858) · [本地PDF，18页](3c_Diffusion与HPC_AI/DeepCache.pdf)
- **TeaCache｜Timestep Embedding Tells: It's Time to Cache for Video Diffusion Model**（2024/11/28；必读）
  - 用途：使用时间步嵌入估计变化并决定特征缓存复用。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2411.19108) · [本地PDF，11页](3c_Diffusion与HPC_AI/TeaCache.pdf)
- **DistriFusion｜DistriFusion: Distributed Parallel Inference for High-Resolution Diffusion Models**（2024/02/29；扩展）
  - 用途：以异步通信与特征复用支持分布式扩散推理。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2402.19481) · [本地PDF，12页](3c_Diffusion与HPC_AI/DistriFusion.pdf)
- **FNO｜Fourier Neural Operator for Parametric Partial Differential Equations**（2020/10/18；必读）
  - 用途：傅里叶神经算子作为PDE解映射的代理。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2010.08895) · [本地PDF，16页](3c_Diffusion与HPC_AI/FNO.pdf)
- **DeepONet｜DeepONet: Learning nonlinear operators for identifying differential equations based on the universal approximation theorem of operators**（2019/10/08；扩展）
  - 用途：学习算子映射的代理模型基础。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/1910.03193) · [本地PDF，22页](3c_Diffusion与HPC_AI/DeepONet.pdf)
- **GraphCast｜GraphCast: Learning skillful medium-range global weather forecasting**（2022/12/24；扩展）
  - 用途：学习型天气预报作为科学计算加速案例。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2212.12794) · [本地PDF，102页](3c_Diffusion与HPC_AI/GraphCast.pdf)
- **SmartSim｜Using Machine Learning at Scale in HPC Simulations with SmartSim: An Application to Ocean Climate Modeling**（2021/04/13；必读）
  - 用途：HPC数值模拟与在线深度学习推理耦合。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2104.09355) · [本地PDF，11页](3c_Diffusion与HPC_AI/SmartSim.pdf)
- **Colmena｜Colmena: Scalable Machine-Learning-Based Steering of Ensemble Simulations for High Performance Computing**（2021/10/06；扩展）
  - 用途：机器学习驱动的HPC模拟集合调度。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2110.02827) · [本地PDF，13页](3c_Diffusion与HPC_AI/Colmena.pdf)
- **ColmenaExascale｜Employing Artificial Intelligence to Steer Exascale Workflows with Colmena**（2024/08/26；必读）
  - 用途：仿真、训练、推理交织的超算工作流。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2408.14434) · [本地PDF，12页](3c_Diffusion与HPC_AI/ColmenaExascale.pdf)
- **DeepDriveMD｜DeepDriveMD: Deep-Learning Driven Adaptive Molecular Simulations for Protein Folding**（2019/09/17；必读）
  - 用途：深度学习引导自适应分子模拟。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/1909.07817) · [本地PDF，9页](3c_Diffusion与HPC_AI/DeepDriveMD.pdf)
- **StreamingAIHPC｜Coupling streaming AI and HPC ensembles to achieve 100-1000x faster biomolecular simulations**（2021/04/10；扩展）
  - 用途：流式耦合AI与HPC集合任务。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2104.04797) · [本地PDF，11页](3c_Diffusion与HPC_AI/StreamingAIHPC.pdf)

### 4a_监控_故障诊断

- **MegaScale｜MegaScale: Scaling Large Language Model Training to More Than 10,000 GPUs**（2024；必读）
  - 用途：万卡训练的可观测性、故障定位与慢节点治理。
  - 来源类型/出处：21st USENIX Symposium on Networked Systems Design and Implementation (NSDI 24)。
  - [原始页面](https://www.usenix.org/conference/nsdi24/presentation/jiang-ziheng) · [本地PDF，17页](4a_监控_故障诊断/MegaScale.pdf)
- **SuperBench｜SuperBench: Improving Cloud AI Infrastructure Reliability with Proactive Validation**（2024/02/09；必读）
  - 用途：通过主动性能验证发现云AI基础设施灰故障。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2402.06194) · [本地PDF，16页](4a_监控_故障诊断/SuperBench.pdf)
- **Minder｜Minder: Faulty Machine Detection for Large-scale Distributed Model Training**（2025；必读）
  - 用途：大规模训练中的故障机器检测。
  - 来源类型/出处：22nd USENIX Symposium on Networked Systems Design and Implementation (NSDI 25)。
  - [原始页面](https://www.usenix.org/conference/nsdi25/presentation/deng) · [本地PDF，18页](4a_监控_故障诊断/Minder.pdf)
- **Holmes｜Holmes: Localizing Irregularities in LLM Training with Mega-scale GPU Clusters**（2025；必读）
  - 用途：超大GPU集群训练异常定位。
  - 来源类型/出处：22nd USENIX Symposium on Networked Systems Design and Implementation (NSDI 25)。
  - [原始页面](https://www.usenix.org/conference/nsdi25/presentation/yao) · [本地PDF，19页](4a_监控_故障诊断/Holmes.pdf)
- **TPUResiliency｜Resiliency at Scale: Managing Google’s TPUv4 Machine Learning Supercomputer**（2024；扩展）
  - 用途：TPUv4超算的可用性与弹性管理案例。
  - 来源类型/出处：21st USENIX Symposium on Networked Systems Design and Implementation (NSDI 24)。
  - [原始页面](https://www.usenix.org/conference/nsdi24/presentation/zu) · [本地PDF，15页](4a_监控_故障诊断/TPUResiliency.pdf)
- **DatacenterCharacterization｜Characterization of Large Language Model Development in the Datacenter**（2024；必读）
  - 用途：数据中心大模型开发负载、故障与自动恢复实证。
  - 来源类型/出处：21st USENIX Symposium on Networked Systems Design and Implementation (NSDI 24)。
  - [原始页面](https://www.usenix.org/conference/nsdi24/presentation/hu) · [本地PDF，22页](4a_监控_故障诊断/DatacenterCharacterization.pdf)
- **SDCsInTheWild｜SDCs in the Wild: Characterizing and Diagnosing SDC-Defective GPUs in Production LLM Training (Operational Systems)**（2026；前沿）
  - 用途：生产训练中静默数据损坏的特征与缺陷GPU诊断。
  - 来源类型/出处：20th USENIX Symposium on Operating Systems Design and Implementation (OSDI 26)。
  - [原始页面](https://www.usenix.org/conference/osdi26/presentation/zheng) · [本地PDF，20页](4a_监控_故障诊断/SDCsInTheWild.pdf)

### 4b_检查点_训练恢复

- **CheckFreq｜CheckFreq: Frequent, Fine-Grained DNN Checkpointing**（2021；必读）
  - 用途：细粒度检查点、自适应保存频率与计算IO重叠。
  - 来源类型/出处：19th USENIX Conference on File and Storage Technologies (FAST 21)。
  - [原始页面](https://www.usenix.org/conference/fast21/presentation/mohan) · [本地PDF，15页](4b_检查点_训练恢复/CheckFreq.pdf)
- **CheckNRun｜Check-N-Run: a Checkpointing System for Training Deep Learning Recommendation Models**（2022；必读）
  - 用途：推荐模型差分检查点与压缩，增量保存的重要案例。
  - 来源类型/出处：19th USENIX Symposium on Networked Systems Design and Implementation (NSDI 22)。
  - [原始页面](https://www.usenix.org/conference/nsdi22/presentation/eisenman) · [本地PDF，16页](4b_检查点_训练恢复/CheckNRun.pdf)
- **Gemini｜Gemini: Fast failure recovery in distributed training with in-memory checkpoints**（2023；必读）
  - 用途：内存检查点放置与网络调度，加快训练恢复。
  - 来源类型/出处：SOSP 2023。
  - [原始页面](https://www.amazon.science/publications/gemini-fast-failure-recovery-in-distributed-training-with-in-memory-checkpoints) · [本地PDF，18页](4b_检查点_训练恢复/Gemini.pdf)
- **ByteCheckpoint｜ByteCheckpoint: A Unified Checkpointing System for Large Foundation Model Development**（2025；必读）
  - 用途：统一分布式检查点与跨并行配置恢复。
  - 来源类型/出处：22nd USENIX Symposium on Networked Systems Design and Implementation (NSDI 25)。
  - [原始页面](https://www.usenix.org/conference/nsdi25/presentation/wan-borui) · [本地PDF，21页](4b_检查点_训练恢复/ByteCheckpoint.pdf)
- **SWIFT｜SWIFT: Expedited Failure Recovery for Large-scale DNN Training**（2023/02/13；必读）
  - 用途：利用数据并行状态副本加速故障恢复。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2302.06173) · [本地PDF，14页](4b_检查点_训练恢复/SWIFT.pdf)
- **Oobleck｜Oobleck: Resilient Distributed Training of Large Models Using Pipeline Templates**（2023/09/15；必读）
  - 用途：基于流水线模板的弹性容错训练。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2309.08125) · [本地PDF，15页](4b_检查点_训练恢复/Oobleck.pdf)
- **Bamboo｜Bamboo: Making Preemptible Instances Resilient for Affordable Training of Large DNNs**（2022/04/26；扩展）
  - 用途：以冗余计算支持抢占式实例上的容错训练。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2204.12013) · [本地PDF，17页](4b_检查点_训练恢复/Bamboo.pdf)
- **ReCycle｜ReCycle: Resilient Training of Large DNNs using Pipeline Adaptation**（2024/05/22；扩展）
  - 用途：通过流水线适配应对资源故障。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2405.14009) · [本地PDF，18页](4b_检查点_训练恢复/ReCycle.pdf)
- **InMemoryHP｜Fault-Tolerant Hybrid-Parallel Training at Scale with Reliable and Efficient In-memory Checkpointing**（2023/10/19；扩展）
  - 用途：混合并行训练的可靠内存检查点。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2310.12670) · [本地PDF，13页](4b_检查点_训练恢复/InMemoryHP.pdf)
- **TrainMover｜TrainMover: An Interruption-Resilient Runtime for ML Training**（2026；前沿）
  - 用途：弹性与备用机器支持低中断训练恢复。
  - 来源类型/出处：20th USENIX Symposium on Operating Systems Design and Implementation (OSDI 26)。
  - [原始页面](https://www.usenix.org/conference/osdi26/presentation/lao) · [本地PDF，19页](4b_检查点_训练恢复/TrainMover.pdf)
- **MoEvement｜Sparse Checkpointing for Fast and Reliable MoE Training**（2026；前沿）
  - 用途：MoE稀疏增量检查点与局部恢复。
  - 来源类型/出处：23rd USENIX Symposium on Networked Systems Design and Implementation (NSDI 26)。
  - [原始页面](https://www.usenix.org/conference/nsdi26/presentation/gandhi) · [本地PDF，22页](4b_检查点_训练恢复/MoEvement.pdf)
- **TierCheck｜TierCheck: Tiered Checkpointing for Fault Tolerance in Large Language Model Training**（2026/05/18；前沿）
  - 用途：按故障异质性进行分层差分检查点与恢复。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2605.17821) · [本地PDF，14页](4b_检查点_训练恢复/TierCheck.pdf)

### 4c_推理高可用_SLO

- **DejaVu｜DéjàVu: KV-cache Streaming for Fast, Fault-tolerant Generative LLM Serving**（2024/03/04；必读）
  - 用途：KV缓存流式保存与容错推理。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2403.01876) · [本地PDF，24页](4c_推理高可用_SLO/DejaVu.pdf)
- **Llumnix｜Llumnix: Dynamic Scheduling for Large Language Model Serving**（2024/06/05；必读）
  - 用途：请求与KV状态迁移、动态负载均衡；与崩溃恢复区分。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2406.03243) · [本地PDF，19页](4c_推理高可用_SLO/Llumnix.pdf)
- **ServerlessLLM｜ServerlessLLM: Low-Latency Serverless Inference for Large Language Models**（2024/01/25；必读）
  - 用途：快速模型加载与推理迁移，支持弹性服务。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2401.14351) · [本地PDF，19页](4c_推理高可用_SLO/ServerlessLLM.pdf)
- **KunServe｜KunServe: Parameter-centric Memory Management for Efficient Memory Overloading Handling in LLM Serving**（2024/12/24；扩展）
  - 用途：以参数为中心的内存管理，处理推理服务内存过载。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2412.18169) · [本地PDF，17页](4c_推理高可用_SLO/KunServe.pdf)
- **SLOMetrics｜Revisiting Service Level Objectives and System Level Metrics in Large Language Model Serving**（2024/10/18；必读）
  - 用途：SLO与goodput指标设计，避免只统计平均吞吐。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2410.14257) · [本地PDF，12页](4c_推理高可用_SLO/SLOMetrics.pdf)
- **SCORPIO｜Scorpio: Serving Right Requests at the Right Time for Heterogeneous SLOs in LLM Inference**（2025/05/29；必读）
  - 用途：异质SLO下的请求选择与调度。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2505.23022) · [本地PDF，15页](4c_推理高可用_SLO/SCORPIO.pdf)
- **JITServe｜JITServe: SLO-aware LLM Serving with Imprecise Request Information**（2026；前沿）
  - 用途：请求信息不精确时的SLO感知服务。
  - 来源类型/出处：23rd USENIX Symposium on Networked Systems Design and Implementation (NSDI 26)。
  - [原始页面](https://www.usenix.org/conference/nsdi26/presentation/zhang-wei) · [本地PDF，25页](4c_推理高可用_SLO/JITServe.pdf)
- **GhostServe｜GhostServe: A Lightweight Checkpointing System in the Shadow for Fault-Tolerant LLM Serving**（2026/03/26；前沿）
  - 用途：轻量检查点支持推理故障恢复。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2605.00831) · [本地PDF，15页](4c_推理高可用_SLO/GhostServe.pdf)
- **KevlarFlow｜Towards Resiliency in Large Language Model Serving with KevlarFlow**（2026/01/30；前沿）
  - 用途：大模型服务韧性与故障处理。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2601.22438) · [本地PDF，13页](4c_推理高可用_SLO/KevlarFlow.pdf)
- **LUMEN｜LUMEN: Coordinated Failure Recovery for Distributed LLM Serving**（2026/06/16；前沿）
  - 用途：协调检查点放置、受影响请求分配与服务容量恢复。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2606.17787) · [本地PDF，15页](4c_推理高可用_SLO/LUMEN.pdf)
- **Concordia｜Concordia: JIT-Compiled Persistent-Kernel Checkpointing for Fault-Tolerant LLM Inference**（2026/06/22；前沿）
  - 用途：持久内核与检查点机制支持容错推理。
  - 来源类型/出处：arXiv（下载版本；会议发表信息另查原始页）。
  - [原始页面](https://arxiv.org/abs/2606.23521) · [本地PDF，16页](4c_推理高可用_SLO/Concordia.pdf)

## 官方工程文档（与研究论文分开）

- **NVIDIA_MixedPrecision**（3a）：混合精度训练与损失缩放官方指南。 [官网](https://docs.nvidia.com/deeplearning/performance/mixed-precision-training/index.html) · [网页快照](官方工程文档/NVIDIA_MixedPrecision.html)
- **DCGM_Diagnostics**（4a）：GPU诊断与健康检查。 [官网](https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/dcgm-diagnostics.html) · [网页快照](官方工程文档/DCGM_Diagnostics.html)
- **NsightSystems**（4a）：CPU、CUDA和通信时间线的性能分析。 [官网](https://docs.nvidia.com/nsight-systems/UserGuide/index.html) · [网页快照](官方工程文档/NsightSystems.html)
- **PyTorch_Profiler**（4a）：算子耗时、形状和内存分析接口。 [官网](https://docs.pytorch.org/docs/stable/profiler.html) · [网页快照](官方工程文档/PyTorch_Profiler.html)
- **PyTorch_DCP**（4b）：分布式检查点API与重分片加载。 [官网](https://docs.pytorch.org/docs/stable/distributed.checkpoint.html) · [网页快照](官方工程文档/PyTorch_DCP.html)
- **PyTorch_AsyncDCP**（4b）：异步检查点的实现与内存开销。 [官网](https://docs.pytorch.org/tutorials/recipes/distributed_async_checkpoint_recipe.html) · [网页快照](官方工程文档/PyTorch_AsyncDCP.html)
- **PyTorch_Elastic**（4b）：弹性启动、worker故障与恢复语义。 [官网](https://docs.pytorch.org/docs/stable/elastic/run.html) · [网页快照](官方工程文档/PyTorch_Elastic.html)
- **RayServe_FaultTolerance**（4c）：副本、控制器与服务层容错边界。 [官网](https://docs.ray.io/en/latest/serve/production-guide/fault-tolerance.html) · [网页快照](官方工程文档/RayServe_FaultTolerance.html)
- **RayServe_LoadShedding**（4c）：请求队列、负载削减、超时与重试。 [官网](https://docs.ray.io/en/latest/serve/production-guide/best-practices.html) · [网页快照](官方工程文档/RayServe_LoadShedding.html)
- **SmartSim_Experiments**（3c）：仿真与AI组件的部署和通信。 [官网](https://www.craylabs.org/docs/experiment.html) · [网页快照](官方工程文档/SmartSim_Experiments.html)
- **DeepDriveMD_Docs**（3c）：同步与异步仿真学习推理工作流。 [官网](https://deepdrivemd-pipeline.readthedocs.io/en/latest/) · [网页快照](官方工程文档/DeepDriveMD_Docs.html)

- **NVIDIA_FP8_Delayed**（3a）：FP8张量缩放与历史绝对最大值。 [官网](https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/features/low_precision_training/fp8_delayed_scaling/fp8_delayed_scaling.html) · [网页快照](官方工程文档/NVIDIA_FP8_Delayed.html)

- **vLLM_Prefix_Design**（3b）：前缀KV缓存的块哈希、复用条件与管理。 [官网](https://docs.vllm.ai/en/latest/design/prefix_caching/) · [网页快照](官方工程文档/vLLM_Prefix_Design.html)

## 下载与核验说明

所有PDF均检查文件标识并解析页数；校验日志保存SHA-256及首页文字摘录，用于题名复核。网页快照可能依赖联网样式。下载脚本仅访问公开原始来源，不包含付费数据库全文。脚本、原始快照及检索记录一并保留，方便后续更新。
