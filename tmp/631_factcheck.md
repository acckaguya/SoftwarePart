# 6.3.1“低精度训练与推理量化”事实审校清单

## 一、总的组织原则

FP16、BF16 和 FP8 首先是**数值格式及训练精度流**；W8A8、W4A16 和 W4A8KV4 首先是**推理阶段不同张量的位宽配置**。二者可以放在同一节讨论，但不能排成一条从“16 位到 4 位”的单线演进路线。较稳妥的写法是先写训练侧的“格式—精度流—稳定性”，再写推理侧的“量化对象—误差控制—执行内核”，最后用显存、带宽、计算、质量和端到端性能把两条线汇合。

建议在正文第一次使用 W/A/KV 记法时自行声明：**本文以 `Wb_wAb_aKVb_k` 表示线性层权重、矩阵乘输入激活和 KV Cache 的量化位宽；省略 KV 时不推断其位宽，整数或浮点格式另行标明。** 这是必要的，因为不同论文的缩写约定并不完全一致。例如 [QServe](https://proceedings.mlsys.org/paper_files/paper/2025/hash/fbe2b2f74a2ece8070d8fb073717bda6-Abstract-Conference.html) 在文内把 `WxAy` 定义为 `Ay` 与 `KVy` 同位宽时的缩写，而更广泛的用法往往只用 W/A 描述矩阵乘的两个输入。

## 二、术语边界审校

| 术语 | 可核验的边界 | 正文必须补足的信息 | 建议写法 |
|---|---|---|---|
| **FP16** | 通常指 IEEE binary16：1 位符号、5 位指数、10 位显式尾数。相较 BF16，FP16 有更多有效精度，但指数范围较窄。经典 [Mixed Precision Training](https://openreview.net/forum?id=r1gs9JgRZ)（ICLR 2018）采用 FP16 权重副本、激活和梯度进行前反向计算，同时保留 FP32 主权重，以 FP32 累加 FP16 乘积，并用 loss scaling 缓解小梯度下溢。 | 哪些算子输入/输出为 FP16；参数或主权重、梯度、优化器状态的保存精度；点积与归约的累加精度；是否使用动态 loss scaling。 | “Micikevicius 等在 ICLR 2018 的实现中，以 FP16 承担主要存储和矩阵计算，并用 FP32 主权重、FP32 累加及损失缩放保护更新精度。”不要把这一特定流程写成所有现代 AMP 实现的唯一形态。 |
| **BF16** | BF16 为 1 位符号、8 位指数、7 位显式尾数；它与 FP32 具有相同的指数位宽和近似相同的动态范围，但有效精度低于 FP16。正式的格式与硬件讨论可引 [Bfloat16 Processing for Neural Networks](https://doi.org/10.1109/ARITH.2019.00022)（IEEE ARITH 2019）。Google TPU 的具体实现以 BF16 乘法、FP32 累加，并会将 BF16 次正规数刷新为零，属于平台语义，不宜外推到所有硬件。 | 平台及其 BF16 算术语义；累加、参数更新和敏感算子的精度；是否仍需数值监测。 | “BF16 以较少尾数位换取与 FP32 相同的指数位宽，通常降低了训练对损失缩放的依赖。”不写“BF16 与 FP32 精度相同”或“BF16 绝不需要 loss scaling”。 |
| **FP8** | FP8 是格式族，不是单一格式。常见 E4M3 在有效精度上更有利，E5M2 具有更宽动态范围；编码变体、舍入/饱和语义和缩放粒度都会改变实际数值行为。[FP8 Formats for Deep Learning](https://arxiv.org/abs/2209.05433) 给出 E4M3/E5M2 提案，但它是 arXiv/CoRR 预印本；现代训练证据宜主引 [Scaling FP8 training to trillion-token LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/hash/f48b5133e89854a9e97cc22a6db83f25-Abstract-Conference.html)（ICLR 2025）和 [COAT](https://proceedings.iclr.cc/paper_files/paper/2025/hash/6ac807c9b296964409b277369e55621a-Abstract-Conference.html)（ICLR 2025）。 | E4M3/E5M2 或其他变体；缩放是 per-tensor、per-channel、per-block 还是 delayed/current scaling；覆盖哪些算子和张量；高精度回退、主权重、梯度与优化器状态；硬件原生支持。 | “一种常见的 tensor-scaled FP8 配方在前向采用 E4M3、在反向梯度采用 E5M2；该选择依赖缩放方案，并非 FP8 的固定规则。”NVIDIA [Transformer Engine 文档](https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/api/common.html)显示，block scaling 也可在前后向均使用 E4M3。 |
| **INT8-W8A8** | `W8A8` 只说明权重与矩阵乘输入激活各为 8 位，不自动说明它们是 INT8 还是 FP8，也不说明累加器、输出、KV Cache、非线性算子和未量化层。 [SmoothQuant](https://proceedings.mlr.press/v202/xiao23c.html)（ICML 2023）是训练后 INT8-W8A8：通过等价缩放把激活离群值造成的量化难度迁移到权重，并覆盖 LLM 的矩阵乘，而非宣称整个模型的全部状态都为 INT8。 | 数据类型；线性层/BMM 覆盖率；静态或动态激活量化；per-tensor/per-channel/per-token 粒度；累加与输出精度；KV 位宽。 | 首次写成“INT8-W8A8（权重 INT8、矩阵乘输入激活 INT8）”。如果讨论 FP8，则写“FP8-W8A8（E4M3，……缩放）”，避免把 INT8 和 FP8 的结果合并。 |
| **INT4-W4A16** | 通常是 weight-only 推理：权重以 INT4 存储，激活保持 FP16 或 BF16。A16 的具体格式必须说明。 [AWQ](https://proceedings.mlsys.org/paper_files/paper/2024/hash/42a452cbafa9dd64e9ba4aa95cc1ef21-Abstract-Conference.html)（MLSys 2024）用激活统计寻找权重通道缩放，但不量化激活；其 TinyChat 内核在计算时按需反量化权重。因此“activation-aware”是权重量化标定方法，不是 weight-activation quantization。 | W4 是 INT4、FP4、NF4 还是其他格式；A16 是 FP16 还是 BF16；分组大小、对称/非对称、scale/zero-point；KV 位宽；实际乘法和累加精度；反量化位置。 | “AWQ 属于 activation-aware 的 INT4 weight-only PTQ；本文将其执行配置记作 W4A16，并固定 A16=FP16。”若拿它与 KV4 比较，应进一步写 `W4A16KV16` 或直接说明 KV Cache 保持 16 位。 |
| **INT4/INT8-W4A8KV4** | 这是 [QServe](https://proceedings.mlsys.org/paper_files/paper/2025/hash/fbe2b2f74a2ece8070d8fb073717bda6-Abstract-Conference.html)（MLSys 2025）中 QoQ 的明确配置：4 位权重、8 位激活、4 位 KV Cache。其实现采用 per-token 对称 INT8 激活量化、per-head 非对称 INT4 KV 量化，并以渐进式权重量化使 GEMM 落在 INT8 Tensor Core 路径上。它不是“全模型 4 位”，也不是 W4A4；KV4 只在自回归推理的注意力状态中有意义。 | 三类张量的具体格式与粒度；KV 的 key/value 是否同配置；尺度元数据；未量化算子；GEMM 的实际输入、部分和及输出精度；上下文长度、并发和后端。 | “QoQ 采用 INT4-W4A8KV4：权重以 4 位存储，运行时形成 INT8 权重与 INT8 激活的 GEMM，KV Cache 以 4 位保存；收益依赖 QServe 的渐进式反量化和专用内核。” |

### 三个容易忽略的限定

1. **存储精度、乘法输入精度、累加精度和输出精度是四件事。** W/A/KV 记法主要描述张量表示，不能推出累加器。例如 QServe 的特定 W4A8 路径包含 INT4 到 INT8 的解码、INT8×INT8 Tensor Core 计算、INT32 部分和以及到 FP16 的转换；这不是 `W4A8KV4` 六个字符本身所蕴含的通用语义。
2. **“激活”通常指进入线性层或矩阵乘的输入，不等于训练中为反向传播保存的全部激活，也不等于 LayerNorm、Softmax、残差和采样等全部中间值。** SmoothQuant 的“all matrix multiplications”不能改写成“全模型所有算子均为 INT8”。
3. **KV Cache 是独立对象。** 其容量随层数、KV 头数、序列长度和并发增长，主要影响自回归推理；W8A8 或 W4A16 本身不应被用来推断 KV 位宽。

## 三、事实审校清单

### 可以保留，但需要带条件

- [ ] “FP16 混合精度训练使用 FP32 主权重、FP32 累加和 loss scaling”应明确归因于 ICLR 2018 的经典配方；现代框架可能保留 FP32 参数并只对选定算子 autocast，流程并非完全一致。
- [ ] “BF16 动态范围与 FP32 相当”宜写成“指数位宽相同、动态范围近似相同”，同时说明它的尾数精度低于 FP16。
- [ ] “BF16 减少 loss scaling 需求”可以写；“BF16 不需要数值稳定性处理”不可以写。
- [ ] “E4M3 用于前向、E5M2 用于反向”只能写成常见 FP8 配方，并绑定缩放方法和实现；更细粒度的 block scaling 可以改变这一选择。
- [ ] “FP8 训练达到 BF16 相当结果并提升吞吐”须绑定 [Scaling FP8 training to trillion-token LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/hash/f48b5133e89854a9e97cc22a6db83f25-Abstract-Conference.html) 的条件：7B 模型、256 个 Intel Gaudi2、最长 2T tokens、Smooth-SwiGLU 与双 Adam moment FP8 方案，论文报告最高约 34% 吞吐提升。
- [ ] “FP8 降低训练显存”须区分单个张量的理论字节数与端到端峰值显存。[COAT](https://proceedings.iclr.cc/paper_files/paper/2025/hash/6ac807c9b296964409b277369e55621a-Abstract-Conference.html)明确指出，常规 FP8 框架主要把线性层计算置于 FP8，而优化器状态和保存激活仍可能是高精度；COAT 额外量化这些对象后，在其测试中相对 BF16 获得 1.54× 端到端显存缩减和 1.43× 加速。
- [ ] “SmoothQuant 是 W8A8”应写成“训练后 INT8-W8A8，并主要覆盖矩阵乘”；其最高 1.56× 加速和约 2× 内存缩减是论文特定模型、硬件和实现下的结果。
- [ ] “AWQ 是 W4A16”应补充“INT4 weight-only，A16=FP16（或明确实际 A16 类型）”；性能优势主要来自减少权重搬运并融合按需反量化，特别适合低批量、带宽受限的生成阶段。
- [ ] “QServe 的 W4A8KV4 优于 W4A16/W8A8”只能表述为其 A100/L40S、给定模型、1024 输入/512 输出和最大可承载吞吐实验中的结果；不能提升为跨硬件、跨负载的普遍排序。

### 应直接改写的高风险结论

| 高风险写法 | 问题 | 建议改写 |
|---|---|---|
| “低精度从 FP16、BF16、FP8 演进到 W8A8、W4A16 和 W4A8KV4。” | 把数值格式与对象位宽配置放到同一分类层级。 | “训练侧围绕 FP16、BF16 与 FP8 的精度流演进；推理侧则按权重、激活和 KV Cache 的量化对象形成 W8A8、W4A16 与 W4A8KV4 等配置。” |
| “BF16 与 FP32 精度相同，因此无需 loss scaling。” | 相同的是指数位宽，尾数精度明显不同；是否需要缩放取决于训练与平台。 | “BF16 保留 FP32 的 8 位指数，通常比 FP16 更少依赖损失缩放，但关键归约和更新仍常保留较高精度。” |
| “FP8 的 E4M3 用于前向，E5M2 用于反向。” | 把常见实现配方误写成格式定义。 | “在一种常见的 tensor-scaled 配方中，前向使用 E4M3、反向梯度使用 E5M2；格式选择随缩放粒度与硬件实现而变化。” |
| “FP8 将 BF16 显存减半、速度提高一倍。” | 只按位宽推算，没有计入高精度状态、cast、scale 和非 FP8 算子。 | “FP8 可将被量化张量的元素存储宽度由 16 位降至 8 位，但端到端显存和吞吐取决于覆盖范围、状态精度、转换开销和原生内核。” |
| “W8A8 就是 FP8/INT8 全模型量化。” | W8A8 不指定数据类型，也不覆盖全部算子、KV 和累加器。 | “SmoothQuant 采用 INT8-W8A8 对 LLM 矩阵乘的权重和输入激活量化；其他算子、累加与 KV Cache 需另行说明。” |
| “LLM.int8() 是纯 W8A8。” | [LLM.int8()](https://proceedings.neurips.cc/paper_files/paper/2022/file/c3ba4962c05c49636d4c6206a97e9c8a-Paper-Conference.pdf)（NeurIPS 2022）把离群特征维度放入 16 位矩阵乘，其余超过 99.9% 的值走 INT8。 | “LLM.int8() 是 INT8 主路径与 FP16 离群维度路径并存的混合精度分解，不属于均匀的纯 INT8-W8A8。” |
| “ZeroQuant 的低比特方案是统一 W4A8。” | [ZeroQuant](https://proceedings.neurips.cc/paper_files/paper/2022/hash/adf7fa39d65e2983d724ff7da57f00ac-Abstract-Conference.html) 的低比特配置将全连接权重降为 INT4，而注意力权重和激活为 INT8。 | “ZeroQuant 的低比特配置采用分层混合位宽：全连接权重 INT4、注意力权重 INT8、激活 INT8。” |
| “AWQ 同时量化权重和激活。” | AWQ 中 Activation-aware 描述标定信号，方法本身是 weight-only。 | “AWQ 根据激活分布选择权重通道缩放，在不量化激活的前提下改善低比特权重误差。” |
| “W4A16 使用 4 位矩阵乘，所以计算峰值更高。” | AWQ/TinyChat 类路径通常按需解包、反量化到 FP16 再计算，主要节省权重带宽。 | “W4A16 以 4 位保存权重并在内核中融合反量化，其主要收益是减少权重访存；是否提高算术吞吐取决于具体内核和硬件。” |
| “W4A8KV4 是 4 位模型/4 位计算。” | A 为 8 位，QServe 的 GEMM 实际走 INT8 Tensor Core；只有权重存储与 KV 为 4 位。 | “QServe 将权重和 KV Cache 分别压缩至 INT4，将激活量化为 INT8，并通过渐进式权重解码执行 INT8 GEMM。” |
| “4 位在所有场景下最优。” | [The case for 4-bit precision](https://proceedings.mlr.press/v202/dettmers23a.html)（ICML 2023）的结论针对 16 位输入、3—8 位参数、特定模型族和零样本准确率/总模型比特权衡。 | “在该论文覆盖的模型族与零样本评测中，4 位参数在固定总模型比特下通常取得最佳精度；该结果不直接证明 W4A4、KV4、训练或任意硬件上的吞吐最优。” |
| “Atom 证明了 W4A8KV4 的效果。” | [Atom](https://proceedings.mlsys.org/paper_files/paper/2024/hash/5edb57c05c81d04beb716ef1d542fe9e-Abstract-Conference.html)（MLSys 2024）核心评估是 4 位 weight-activation，即 W4A4，不是 QServe 的 W4A8KV4。 | “Atom 可作为 W4A4 服务系统证据；W4A8KV4 的主证据应使用 QoQ/QServe。” |
| “loss scaling 与 FP8 tensor scaling 都是缩放，因此可以合并解释。” | 前者主要在反向中放大损失/梯度以避免 FP16 小梯度下溢；后者把张量数值映射到 FP8 可表示区间，粒度和更新时间也是算法组成。 | 分成两句解释，并分别说明作用对象、缩放粒度和回缩位置。 |

## 四、适合报告采用的比较维度

### 训练侧：FP16、BF16、FP8

| 比较维度 | 应写内容 | 不应使用的替代指标 |
|---|---|---|
| 表示能力 | 指数/尾数的取舍、次正规数和溢出语义；FP8 还要写 E4M3/E5M2 及 scale 粒度。 | 只比较“总位数”。 |
| 精度流 | 矩阵乘输入、累加器、输出、参数/主权重、梯度、优化器状态和保存激活分别是什么精度。 | 用“FP8 训练”概括所有状态。 |
| 稳定性 | loss scaling、tensor/block scaling、离群值、溢出/跳步、长程 loss 曲线、最终 time-to-quality。 | 只看短程 loss 或一次最终准确率。 |
| 显存 | 权重、主权重、梯度、优化器状态、保存激活、scale 元数据和工作区的峰值分解。 | 用 8/16=1/2 直接推导端到端显存。 |
| 性能 | 硬件型号、矩阵形状、批量、并行方式、原生低精度单元、cast/amax 开销、端到端 tokens/s。 | 厂商峰值 FLOPS 直接代替训练吞吐。 |
| 质量 | 相同数据、token 数、优化器和超参数下的收敛；大模型还应报告长程稳定性和下游指标。 | 把单一小模型结论外推到长程 LLM 训练。 |

### 推理侧：INT8-W8A8、INT4-W4A16、W4A8KV4

| 比较维度 | W4A16 | W8A8 | W4A8KV4 |
|---|---|---|---|
| 量化对象 | 权重；激活和 KV 通常保持 16 位，须显式确认。 | 权重和矩阵乘输入激活；KV 另报。 | 权重、矩阵乘输入激活、KV Cache 三者。 |
| 主要收益 | 降低静态权重容量与权重读带宽，常适合低批量、decode 主导场景。 | 同时降低权重/激活流量，并可调用 INT8 计算路径；在较大批量或 compute-bound GEMM 中更有机会受益。 | 同时压缩权重与长上下文 KV，并保持 INT8 GEMM；面向高并发云端服务的算法—内核协同。 |
| 主要代价 | INT4 解包/反量化、group scale 元数据；不直接减少 KV 容量。 | 激活离群值、动态量化与 Q/DQ 开销；量化覆盖率受算子支持影响。 | 权重解码、A8 标定、KV4 误差及专用 attention/GEMM 内核，软件依赖最强。 |
| 质量指标 | PPL、零样本/指令任务；注明 group size 和校准集。 | PPL、下游任务；注明静态/动态激活 scale 和离群值处理。 | 除 PPL/下游任务外，必须增加长上下文任务，单独评估 KV4。 |
| 系统指标 | 权重显存、batch=1/小 batch 的 decode 延迟和 tok/s。 | prefill/decode 分开，报告 batch/concurrency 下的吞吐与延迟。 | 权重/KV 显存分解、最大可承载并发、TTFT、TPOT、goodput 与长上下文吞吐。 |
| 结论边界 | AWQ/GPTQ 的速度结果依赖融合内核，算法精度不自动等于系统加速。 | SmoothQuant 的 W8A8 结论是 INT8 PTQ，不可与 FP8 PTQ直接合并。 | QServe 的优势来自 QoQ 与 QServe 共同设计，不应只归因于“位宽更低”。 |

横向比较时，至少固定模型与版本、硬件、推理后端、量化覆盖范围、校准数据、batch/concurrency、输入/输出长度和延迟约束。吞吐应同时给出绝对值与相同基线下的倍率；显存应拆分权重、KV、运行时工作区与 scale/zero-point 元数据；质量应同时报告困惑度、通用任务和长上下文任务。若这些条件没有对齐，只能把不同论文结果作为机制证据，不能制作排名式性能表。

## 五、可直接用于报告的建议表述

### 1. 训练侧过渡段

低精度训练并非把模型中的全部数据统一改成更短的格式，而是在矩阵乘输入、累加结果、参数更新和持久化状态之间设计一条精度流。[Mixed Precision Training](https://openreview.net/forum?id=r1gs9JgRZ)（ICLR 2018）所确立的经典 FP16 配方，以 FP16 承担主要前反向计算，同时通过 FP32 主权重、FP32 累加和损失缩放保护小幅参数更新与梯度；BF16 则保留 8 位指数，以较少尾数精度换取接近 FP32 的动态范围，因而通常降低了对损失缩放的依赖。二者仍需结合具体加速器说明累加、归约和优化器状态的精度，不能仅凭输入格式推断端到端数值行为。

### 2. FP8 段

FP8 进一步缩短矩阵计算输入，但 E4M3 与 E5M2 分别侧重有效精度和动态范围，实际可用性还取决于 per-tensor 或 per-block 缩放、离群值处理及高精度回退。一种常见配方在前向使用 E4M3、在反向梯度使用 E5M2，但这不是固定规则；更细粒度的缩放可以使前后向均采用 E4M3。ICLR 2025 的 [Scaling FP8 training to trillion-token LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/hash/f48b5133e89854a9e97cc22a6db83f25-Abstract-Conference.html)进一步表明，短程实验未暴露的 SwiGLU 离群值会在长程训练中造成失稳，作者通过 Smooth-SwiGLU 和 FP8 Adam 状态量化，在 256 个 Gaudi2 上完成 7B 模型、最长 2T tokens 的训练并报告相对 BF16 最高约 34% 的吞吐提升。该结果说明 FP8 的工程边界由格式、缩放、模型结构与状态精度共同决定，而不能由 8 位表示单独概括。

### 3. 推理量化段

推理量化更适合按量化对象区分。GPTQ 和 [AWQ](https://proceedings.mlsys.org/paper_files/paper/2024/hash/42a452cbafa9dd64e9ba4aa95cc1ef21-Abstract-Conference.html)主要代表 INT4 weight-only 路线，常记为 W4A16：前者利用近似二阶信息补偿逐层权重量化误差，后者依据激活分布选择权重通道缩放，但二者都不因“activation-aware”而把激活降至 4 位；其系统收益主要来自减少权重搬运，并依赖融合解包和反量化的专用内核。[SmoothQuant](https://proceedings.mlr.press/v202/xiao23c.html)则面向 INT8-W8A8，通过等价变换把激活离群值造成的量化难度迁移到权重，使矩阵乘的权重和输入激活均可进入 INT8 路径。两类方法分别缓解权重带宽和矩阵计算瓶颈，不能只按 4 位与 8 位判断优劣。

### 4. W4A8KV4 与工程收束段

长上下文和高并发服务还需要把 KV Cache 作为独立量化对象。[QServe](https://proceedings.mlsys.org/paper_files/paper/2025/hash/fbe2b2f74a2ece8070d8fb073717bda6-Abstract-Conference.html)（MLSys 2025）提出的 QoQ 采用 INT4-W4A8KV4，并通过渐进式权重量化把 4 位存储权重转换到 INT8 Tensor Core 的 GEMM 路径，同时用 SmoothAttention 控制 KV4 带来的误差；其收益来自权重、激活和 KV Cache 的联合压缩以及专用内核，并不意味着全模型执行 4 位运算。因此，对 W4A16、W8A8 和 W4A8KV4 的比较应同时报告模型质量、权重与 KV 显存、反量化开销、内核覆盖率、prefill/decode 性能和请求形态，只有在模型、硬件、后端、上下文长度与并发配置一致时，端到端吞吐倍率才具有直接可比性。

## 六、主证据及其可承担的结论

| 来源 | 正式状态 | 适合支撑 | 不宜承担 |
|---|---|---|---|
| [Mixed Precision Training](https://openreview.net/forum?id=r1gs9JgRZ) | ICLR 2018 | FP16 主权重、累加、loss scaling 的经典配方 | 所有现代 AMP 框架都采用完全相同的数据流 |
| [Bfloat16 Processing for Neural Networks](https://doi.org/10.1109/ARITH.2019.00022) | IEEE ARITH 2019 | BF16 格式和硬件算术取舍 | 所有 BF16 平台的次正规数、舍入和累加语义完全相同 |
| [Scaling FP8 training to trillion-token LLMs](https://proceedings.iclr.cc/paper_files/paper/2025/hash/f48b5133e89854a9e97cc22a6db83f25-Abstract-Conference.html) | ICLR 2025 | 长程 FP8 训练稳定性、SwiGLU 离群值、特定 Gaudi2 结果 | 任意模型/硬件上的统一 FP8 加速倍率 |
| [COAT](https://proceedings.iclr.cc/paper_files/paper/2025/hash/6ac807c9b296964409b277369e55621a-Abstract-Conference.html) | ICLR 2025 | 常规 FP8 覆盖边界、优化器和保存激活的显存问题 | “所有 FP8 框架都已把全部状态量化为 FP8” |
| [FP8 Quantization: The Power of the Exponent](https://proceedings.neurips.cc/paper_files/paper/2022/hash/5e07476b6bd2497e1fbd11b8f0b2de3c-Abstract-Conference.html) | NeurIPS 2022 | FP8 与 INT8 在 PTQ/QAT 中对动态范围和离群值的精度差异 | FP8 硬件一定比 INT8 更快 |
| [Efficient Post-training Quantization with FP8 Formats](https://proceedings.mlsys.org/paper_files/paper/2024/hash/dea9b4b6f55ae611c54065d6fc750755-Abstract-Conference.html) | MLSys 2024 | FP8 PTQ 的跨任务覆盖、E3M4/E4M3/E5M2 选择 | FP8 训练的收敛与状态精度 |
| [GPTQ](https://openreview.net/forum?id=tcbBPnfwxS) | ICLR 2023 | 近似二阶 one-shot weight-only PTQ、低批量生成内核 | 激活量化或通用大批量计算加速 |
| [SmoothQuant](https://proceedings.mlr.press/v202/xiao23c.html) | ICML 2023 | INT8-W8A8 PTQ、离群值平滑和矩阵乘落地 | 全模型全部状态 INT8 或 FP8 结论 |
| [AWQ](https://proceedings.mlsys.org/paper_files/paper/2024/hash/42a452cbafa9dd64e9ba4aa95cc1ef21-Abstract-Conference.html) | MLSys 2024 | activation-aware 的 weight-only PTQ 与 W4A16 内核 | 激活被量化的证据 |
| [The case for 4-bit precision](https://proceedings.mlr.press/v202/dettmers23a.html) | ICML 2023 | 固定总模型比特下，参数位宽与零样本精度的尺度关系 | KV4、W4A4、训练精度或硬件吞吐的普遍最优性 |
| [QServe](https://proceedings.mlsys.org/paper_files/paper/2025/hash/fbe2b2f74a2ece8070d8fb073717bda6-Abstract-Conference.html) | MLSys 2025 | W4A8KV4 定义、反量化代价、KV4 和真实服务吞吐 | 脱离 QoQ/QServe、A100/L40S 与请求配置的普遍倍率 |

补充材料的层级也应在参考文献中写清：[A Study of BFLOAT16 for Deep Learning Training](https://arxiv.org/abs/1905.12322) 和 [FP8 Formats for Deep Learning](https://arxiv.org/abs/2209.05433) 均为 arXiv/CoRR 预印本，适合作为机制背景；BF16 的平台行为可补引 [Google Cloud TPU 官方文档](https://cloud.google.com/tpu/docs/bfloat16)，FP8 配方和当前硬件支持可补引 [NVIDIA Transformer Engine 官方文档](https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/features/low_precision_training/fp8_current_scaling/fp8_current_scaling.html)，但厂商文档不应替代正式论文承担跨平台性能结论。
