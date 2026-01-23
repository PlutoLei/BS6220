# BGformer Forward Propagation 演示文稿内容

> **课程**: BS6220 Spatial and Multi-omics Data Analytics  
> **主题**: Forward Propagation (Mathematical Expression)  
> **模型**: BGformer 血糖预测模型

---

## Slide 1: 封面

### Forward Propagation
### (Mathematical Expression)

**基于BGformer的血糖预测模型**

BS6220: Spatial and Multi-omics Data Analytics

Group X · 2025

---

## Slide 2: 背景：为什么需要血糖预测？

### 问题
- 糖尿病影响全球数百万人
- 血糖异常导致严重并发症
- 现有方法难以捕捉血糖波动性

### 解决方案
- 机器学习预测血糖趋势
- 提前60-90分钟预警
- 辅助胰岛素和饮食决策
- **BGformer模型**

---

## Slide 3: Forward Propagation 的目的

### 定义
将输入数据通过一系列**数学变换**，逐层传递，最终得到预测输出

### 流程图
```
输入          特征提取        注意力计算      生成预测        输出
血糖时序  →   FEM模块    →    Encoder    →   Decoder   →   未来血糖
```

### 核心
本次重点讲解 **Feature Enhancement Module (FEM)** 的前向传播数学表达式

---

## Slide 4: 数值例子①：周期性特征提取

### 公式 (Eq. 5-7)
```
hour_of_day = hour(x) / 23 - 0.5
minute_of_hour = minute(x) / 59 - 0.5
second_of_minute = second(x) / 59 - 0.5
```

### 目的
- 将时间戳归一化到 **[-0.5, 0.5]** 区间
- 捕捉血糖的**日内周期性变化**模式

### 计算示例
输入：3个连续血糖测量点的时间戳

| 时间戳 | hour_of_day | minute_of_hour |
|--------|-------------|----------------|
| t1 = 08:15:30 | 8/23 - 0.5 = **-0.152** | 15/59 - 0.5 = **-0.246** |
| t2 = 08:20:30 | 8/23 - 0.5 = **-0.152** | 20/59 - 0.5 = **-0.161** |
| t3 = 08:25:30 | 8/23 - 0.5 = **-0.152** | 25/59 - 0.5 = **-0.076** |

---

## Slide 5: 数值例子②：趋势特征提取

### 指数加权移动平均 (Eq. 11)
```
trend(i) = (1-α) × Σ α^t × x_{i-t}
```

α = 平滑系数，控制历史数据的影响权重

### 目的
- 捕捉血糖的**长期趋势**
- 平滑短期波动，突出整体变化方向

### 特性
**α越小** → 历史数据权重越大 → 趋势越平滑

### 计算示例
输入血糖值 (mg/dL)：x₁=120, x₂=125, x₃=130

设 α = 0.3，计算 trend(3)：

```
trend(3) = (1-0.3) × Σ 0.3^t × x_{3-t}
         = 0.7 × (0.3⁰×130 + 0.3¹×125 + 0.3²×120)
         = 0.7 × (130 + 37.5 + 10.8)
         = 0.7 × 178.3
         = 124.81 mg/dL
```

**解读**：趋势值124.81介于最新值130和历史均值之间，反映上升趋势

---

## Slide 6: BGformer 整体架构

### 数据流
```
输入         FEM          Encoder       Decoder       输出
血糖序列  →  周期+趋势  →  MOC机制   →  DAM模块   →  60/90min
```

### 创新1: FEM (Feature Enhancement Module)
- 周期特征提取 (Eq. 5-9)
- 趋势特征提取 (Eq. 11)
- 季节分解 (Eq. 10)

### 创新2: MOC (Microscale Overlapping Concerns)
- 窗口化局部注意力 (Eq. 12-14)
- 降低计算复杂度
- 捕捉短期依赖

### 创新3: DAM (Dual Attention Module)
- MOC + DAGA组合
- 动态温度参数 (Eq. 15-16)
- 全局+局部注意力融合

---

## Slide 7: MOC: 微尺度重叠关注机制

### 核心思想
将长序列分割为**重叠的小窗口**，仅在窗口内计算注意力分数

### 公式 (Eq. 12-14)
```
X_win = [x_(k+i) for i in 0..W-1]
Scores = softmax(Q * K^T) * V
Y_i = Sum(A_ij * V_j)
```

### 参数
- **W**: 窗口大小
- **O**: 重叠步数

### 窗口化示意图 (W=3, O=1)

原始序列：t1, t2, t3, t4, t5

重叠窗口划分：
| 窗口 | 包含元素 |
|------|----------|
| Window 1 | t1, t2, t3 |
| Window 2 | t2, t3, t4 |
| Window 3 | t3, t4, t5 |

### 优势
降低复杂度 O(L×L) → O(W×W×L/W)

---

## Slide 8: 实验结果

### 数据集信息
| 项目 | 详情 |
|------|------|
| 数据集 | DirecNet - 16位糖尿病患者 |
| 采样间隔 | 5分钟 |
| 预测窗口 | 60分钟 / 90分钟 |

### 60分钟预测性能对比（平均值）

| Model | MAE ↓ | RMSE ↓ | 特点 |
|-------|-------|--------|------|
| ARIMA | 56.03 | 69.88 | 传统模型 |
| LSTM | 28.44 | 35.70 | 深度学习 |
| Transformer | 29.33 | 38.15 | 注意力 |
| Informer | 28.47 | 37.06 | 稀疏注意力 |
| **BGformer (Ours)** | **23.46** | **31.35** | FEM+MOC+DAM |

### 结论
BGformer在MAE和RMSE上均优于8种基准方法，60分钟和90分钟预测均表现最佳

---

## Slide 9: 总结

### 🎯 算法目的
通过数学变换实现**前向传播**，从血糖时序数据中提取特征并预测未来值

### 💡 核心创新
- FEM：周期+趋势特征增强
- MOC：窗口化局部注意力
- DAM：双重注意力融合

### 🏥 实际应用
- 糖尿病患者血糖预测
- 提前**60-90分钟**预警

### Forward Propagation 数学表达
通过**时间特征归一化**和**指数平滑趋势提取**，将原始血糖序列转换为丰富的特征表示，送入Encoder-Decoder进行预测

**性能提升：~14%** (vs Informer)

---

## Slide 10: 参考文献

1. **Xue, Y., Guan, S., and Jia, W.** (2024). BGformer: An improved Informer model to enhance blood glucose prediction. *Journal of Biomedical Informatics*, 157, 104715.

2. **Zhou, H., et al.** (2021). Informer: Beyond efficient transformer for long sequence time-series forecasting. *AAAI*, 35(12), 11106-11115.

3. **Vaswani, A., et al.** (2017). Attention is all you need. *NeurIPS*, 30.

4. **DirecNet Dataset:** Diabetes Research in Children Network. https://public.jaeb.org/direcnet

### AI使用声明
本演示文稿的内容框架、数值算例和PPT制作使用了Claude AI辅助生成。所有技术内容均基于原始论文进行验证。

---

## Slide 11: 团队成员贡献

| 成员 | 贡献领域 |
|------|----------|
| [姓名1] | 课堂汇报 Class Presentation, 协调统筹 Coordination |
| [姓名2] | 课堂汇报 Class Presentation |
| [姓名3] | 录制视频 Recorded Presentation |
| [姓名4] | 资料研究与PPT制作 Research and Slides |
| [姓名5] | 数值算例设计 Numeric Example Design |

---

## 附录：关键公式汇总

### FEM模块 - 周期性特征 (Eq. 5-7)
```
hour_of_day(x) = hour(x) / 23 - 0.5
minute_of_hour(x) = minute(x) / 59 - 0.5
second_of_minute(x) = second(x) / 59 - 0.5
```

### FEM模块 - 趋势特征 (Eq. 11)
```
trend(i) = (1-α) × Σ_{t=0}^{∞} α^t × x_{i-t}
```

### MOC模块 - 窗口注意力 (Eq. 12-14)
```
X_win^(k) = [x_{k+i} | i ∈ [0, W-1]]
Scores^(k) = softmax(Q·K^T / √d_k)·V
Y_i^(k) = Σ_j A_{ij}^(k) · V_j^(k)
```

### 复杂度分析
- 标准注意力: O(L²)
- MOC注意力: O(W² × L/W) = O(W × L)

---

## 演讲时间分配建议（7分钟）

| 部分 | 时长 | 幻灯片 |
|------|------|--------|
| 背景介绍 | 1分钟 | Slide 2 |
| Forward Propagation目的 | 0.5分钟 | Slide 3 |
| 数值例子①：周期特征 | 1.5分钟 | Slide 4 |
| 数值例子②：趋势特征 | 1.5分钟 | Slide 5 |
| BGformer架构概述 | 1分钟 | Slide 6 |
| MOC机制 | 0.5分钟 | Slide 7 |
| 实验结果与总结 | 1分钟 | Slide 8-9 |

---

*文档生成时间：2025年*
