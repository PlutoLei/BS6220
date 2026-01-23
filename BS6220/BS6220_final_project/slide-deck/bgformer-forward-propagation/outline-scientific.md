# Slide Deck Outline

**Topic**: BGformer Forward Propagation - Blood Glucose Prediction Model
**Style**: scientific
**Audience**: Academic / Research (intermediate-experts)
**Language**: 中英双语 (Chinese with English terms)
**Slide Count**: 10 slides
**Generated**: 2026-01-23 12:00

---

<STYLE_INSTRUCTIONS>
Design Aesthetic: Academic scientific illustration aesthetic for biological pathways, chemical processes, and technical systems. Clean, precise diagrams with proper labeling and clear visual flow. Educational clarity with professional polish. Think textbook quality illustrations and academic journal figures.

Background:
  Color: Off-White (#FAFAFA) or Light Blue-Gray (#F0F4F8)
  Texture: None or very subtle paper grain for print feel

Typography:
  Primary Font: Clean serif font (Times New Roman style) for formal academic feel. Bold weight for main titles. Professional, authoritative presence.
  Secondary Font: Sans-serif for diagram labels and annotations. Clear, readable at small sizes.
  Body Font: Serif for body paragraphs, sans-serif for bullet points and lists.

Color Palette:
  Primary Text: Dark Slate (#1E293B) - Headlines, body
  Label Text: Medium Gray (#475569) - Annotations
  Pathway 1: Teal (#0D9488) - Primary pathway, FEM module
  Pathway 2: Blue (#3B82F6) - Secondary pathway, MOC module
  Pathway 3: Purple (#8B5CF6) - Tertiary pathway, DAM module
  Alert: Red (#EF4444) - Key metrics, emphasis
  Positive: Green (#22C55E) - Results, improvements

Visual Elements:
  - Flow diagrams with precise arrows
  - Mathematical formula boxes with clear notation
  - Data tables with color-coded cells
  - Timeline/progression indicators
  - Numbered step sequences

Style Rules:
  Do: Use precise, consistent line weights; Label all components clearly; Show directional flow with arrows; Include mathematical notation; Create numbered sequences
  Don't: Use decorative illustrations; Create imprecise diagrams; Omit labels; Add slide numbers or logos
</STYLE_INSTRUCTIONS>

---

## Slide 1 of 10

**Type**: Cover
**Filename**: 01-slide-cover.png

// NARRATIVE GOAL
Establish the academic context and create immediate interest in the BGformer model for blood glucose prediction.

// KEY CONTENT
Headline: Forward Propagation
Sub-headline: BGformer 血糖预测模型的数学表达式
Context: BS6220: Spatial and Multi-omics Data Analytics

// VISUAL
Central glucose molecule structure with neural network pathways emanating outward. Clean scientific illustration style. Mathematical symbols (Σ, α, softmax) floating subtly in background. Time series wave pattern at bottom representing blood glucose data.

// LAYOUT
Layout: title-hero
Centered composition with large title, glucose molecule as hero visual, course info at bottom.

---

## Slide 2 of 10

**Type**: Content
**Filename**: 02-slide-problem-context.png

// NARRATIVE GOAL
Establish the clinical importance and challenge of blood glucose prediction.

// KEY CONTENT
Headline: 为什么需要血糖预测？
Sub-headline: Clinical Challenge & Solution
Body:
- 糖尿病影响全球数亿人口
- 血糖波动导致严重并发症
- 提前60-90分钟预警至关重要
- BGformer: 基于Transformer的创新解决方案

// VISUAL
Left side: Human silhouette with pancreas highlighted, glucose molecules in bloodstream. Right side: Time series chart showing glucose fluctuations with danger zones marked. Arrow pointing to prediction window (60-90 min ahead).

// LAYOUT
Layout: split-screen
Left: Clinical illustration; Right: Data visualization with prediction window highlighted.

---

## Slide 3 of 10

**Type**: Content
**Filename**: 03-slide-forward-propagation.png

// NARRATIVE GOAL
Define forward propagation and introduce the BGformer pipeline.

// KEY CONTENT
Headline: Forward Propagation 前向传播
Sub-headline: 从输入到预测的数学变换过程
Body:
- 输入: 历史血糖时序数据
- 变换: 特征提取 → 注意力计算 → 预测生成
- 输出: 未来60/90分钟血糖值

// VISUAL
Linear flow diagram: [Blood Glucose Time Series] → [FEM Module] → [Encoder (MOC)] → [Decoder (DAM)] → [Predicted Glucose]. Each box labeled with mathematical notation. Arrows showing data flow direction.

// LAYOUT
Layout: linear-progression
Horizontal flow from left to right with clear stage markers.

---

## Slide 4 of 10

**Type**: Content
**Filename**: 04-slide-periodic-features.png

// NARRATIVE GOAL
Demonstrate the mathematical formulation of periodic feature extraction with concrete numerical example.

// KEY CONTENT
Headline: 周期性特征提取 (Eq. 5-7)
Sub-headline: Capturing Circadian Patterns in Blood Glucose
Body:
- hour_of_day = hour(x) / 23 - 0.5
- minute_of_hour = minute(x) / 59 - 0.5
- 归一化到 [-0.5, 0.5] 区间

Numerical Example Table:
| 时间戳 | hour_of_day | minute_of_hour |
| 08:15:30 | -0.152 | -0.246 |
| 08:20:30 | -0.152 | -0.161 |
| 08:25:30 | -0.152 | -0.076 |

// VISUAL
24-hour circular clock diagram with glucose patterns overlaid. Mathematical formula boxes on the right. Data table with calculated values. Color gradient showing time progression.

// LAYOUT
Layout: split-screen
Left: Circular time diagram; Right: Formulas and calculation table.

---

## Slide 5 of 10

**Type**: Content
**Filename**: 05-slide-trend-features.png

// NARRATIVE GOAL
Explain exponential weighted moving average for trend extraction with step-by-step calculation.

// KEY CONTENT
Headline: 趋势特征提取 (Eq. 11)
Sub-headline: Exponential Weighted Moving Average
Formula: trend(i) = (1-α) × Σ α^t × x_{i-t}

Calculation Example:
- 输入: x₁=120, x₂=125, x₃=130 mg/dL
- α = 0.3
- trend(3) = 0.7 × (130 + 37.5 + 10.8) = 124.81 mg/dL

Interpretation: 趋势值介于历史均值和最新值之间，反映上升趋势

// VISUAL
Line chart showing raw glucose values vs. smoothed trend line. Formula box with step-by-step calculation breakdown. Weight decay visualization (α^t exponential curve). Arrow indicating trend direction.

// LAYOUT
Layout: two-columns
Left: Trend visualization chart; Right: Mathematical calculation breakdown.

---

## Slide 6 of 10

**Type**: Content
**Filename**: 06-slide-bgformer-architecture.png

// NARRATIVE GOAL
Present the complete BGformer architecture with three innovation modules.

// KEY CONTENT
Headline: BGformer 整体架构
Sub-headline: Three Key Innovations
Body:
- FEM (Feature Enhancement Module): 周期+趋势+季节分解
- MOC (Microscale Overlapping Concerns): 窗口化局部注意力
- DAM (Dual Attention Module): 全局+局部注意力融合

// VISUAL
Hierarchical architecture diagram with three colored sections (Teal for FEM, Blue for MOC, Purple for DAM). Data flow arrows connecting modules. Key equation references labeled. Input/output clearly marked.

// LAYOUT
Layout: hierarchical-layers
Stacked layers showing FEM → MOC → DAM progression with bidirectional arrows for DAM.

---

## Slide 7 of 10

**Type**: Content
**Filename**: 07-slide-moc-mechanism.png

// NARRATIVE GOAL
Explain the MOC windowing mechanism for computational efficiency.

// KEY CONTENT
Headline: MOC: 微尺度重叠关注机制
Sub-headline: Windowed Local Attention for Efficiency
Formulas:
- X_win = [x_(k+i) for i in 0..W-1]
- Scores = softmax(Q·K^T / √d_k)·V

Window Example (W=3, O=1):
- Window 1: [t1, t2, t3]
- Window 2: [t2, t3, t4]
- Window 3: [t3, t4, t5]

Complexity: O(L²) → O(W×L)

// VISUAL
Sequence diagram showing overlapping windows. Attention matrix visualization (sparse vs. full). Complexity comparison bar chart. Color-coded window segments.

// LAYOUT
Layout: split-screen
Left: Window overlap diagram; Right: Attention matrix and complexity comparison.

---

## Slide 8 of 10

**Type**: Content
**Filename**: 08-slide-experimental-results.png

// NARRATIVE GOAL
Present quantitative evidence of BGformer's superiority over baseline methods.

// KEY CONTENT
Headline: 实验结果：60分钟预测性能
Sub-headline: DirecNet Dataset - 16 Diabetic Patients
Data Table:
| Model | MAE ↓ | RMSE ↓ |
| ARIMA | 56.03 | 69.88 |
| LSTM | 28.44 | 35.70 |
| Transformer | 29.33 | 38.15 |
| Informer | 28.47 | 37.06 |
| **BGformer** | **23.46** | **31.35** |

Key Finding: ~14% improvement over Informer baseline

// VISUAL
Bar chart comparing all models with BGformer highlighted in green. Error bars if applicable. Improvement percentage callout. Performance improvement arrow annotation.

// LAYOUT
Layout: dashboard
Central comparison table with bar chart visualization. Key metric callouts.

---

## Slide 9 of 10

**Type**: Content
**Filename**: 09-slide-summary.png

// NARRATIVE GOAL
Synthesize the key innovations and their practical impact.

// KEY CONTENT
Headline: 总结：从数学到临床应用
Sub-headline: Forward Propagation in BGformer
Body:
- 算法目的: 从血糖时序中提取特征并预测未来值
- 核心创新: FEM周期特征 + MOC窗口注意力 + DAM双重融合
- 临床价值: 提前60-90分钟预警
- 性能提升: ~14% (vs Informer)

// VISUAL
Hub-spoke diagram with "BGformer" at center. Three innovation modules as spokes. Clinical application icons (glucose meter, alert notification). Performance metric highlight badge.

// LAYOUT
Layout: hub-spoke
Central model name with innovations radiating outward. Summary points in text boxes.

---

## Slide 10 of 10

**Type**: Back Cover
**Filename**: 10-slide-back-cover.png

// NARRATIVE GOAL
Provide academic closure with references and team acknowledgment.

// KEY CONTENT
Headline: References & Acknowledgments
Body:
1. Xue, Y., Guan, S., and Jia, W. (2024). BGformer: An improved Informer model. Journal of Biomedical Informatics.
2. Zhou, H., et al. (2021). Informer: Beyond efficient transformer. AAAI.
3. DirecNet Dataset: Diabetes Research in Children Network

AI Disclosure: Presentation assisted by Claude AI

// VISUAL
Clean reference list layout. Academic styling with proper citation format. Course logo placeholder area. Team contribution section.

// LAYOUT
Layout: bullet-list
Numbered references with clean academic formatting.
