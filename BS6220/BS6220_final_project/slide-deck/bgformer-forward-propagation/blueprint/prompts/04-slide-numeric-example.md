# Slide 04: Numeric Example - EWMA Calculation

## Image Specifications

- **Aspect Ratio**: 16:9 (1920 x 1080 px)
- **Format**: PNG
- **Filename**: 04-slide-numeric-example.png

---

## Blueprint Style Guidelines

### Color Palette
| Element | Color | Hex Code |
|---------|-------|----------|
| Background | Blueprint Paper | #FAF8F5 |
| Grid Lines | Light Gray | #E5E5E5 |
| Primary Text | Deep Slate | #334155 |
| Primary Accent | Engineering Blue | #2563EB |
| Highlight | Amber | #F59E0B |

### Typography
- **Headlines**: Aptos, bold, 36-40pt
- **Formulas**: Aptos or Monospace, 18-22pt
- **Calculations**: Aptos, 16-18pt

---

## Content Specifications

### Headline
**NUMERIC EXAMPLE · 数值示例**

### Sub-headline
**Exponential Weighted Moving Average (EWMA) - Eq. 11**

### Formula
```
trend(i) = (1-α) × Σ α^t × x_{i-t}
```

### Step-by-Step Calculation

**Given:**
- α = 0.3
- Input glucose: [120, 125, 130] mg/dL

**Step 1: Calculate Weights**
| t | α^t | Weight |
|---|-----|--------|
| 0 | 0.3⁰ | 1.000 |
| 1 | 0.3¹ | 0.300 |
| 2 | 0.3² | 0.090 |

**Step 2: Weighted Sum**
```
= 130 × 1.000 + 125 × 0.300 + 120 × 0.090
= 130.0 + 37.5 + 10.8
= 178.3
```

**Step 3: Apply (1-α)**
```
trend(3) = 0.7 × 178.3 = 124.81 mg/dL
```

### Interpretation
- Raw latest value: 130 mg/dL
- Smoothed trend: 124.81 mg/dL
- Reduces noise, captures underlying trend

---

## Visual Description

### Layout: Split-Screen
- **Left**: Formula and parameters
- **Right**: Step-by-step calculation trace

### Left Column Elements

1. **Formula Box**
   - EWMA formula prominently displayed
   - "Eq. 11" label
   - Engineering blue border

2. **Parameter Box**
   - α = 0.3
   - Input vector visualization
   - Bar chart showing [120, 125, 130]

3. **Weight Decay Curve (Small)**
   - Shows exponential decay α^t
   - X-axis: time steps
   - Y-axis: weight value

### Right Column Elements

1. **Calculation Trace Box**
   - Step 1: Weight table
   - Step 2: Weighted sum calculation
   - Step 3: Final result (amber highlight)

2. **Result Highlight**
   - "trend(3) = 124.81 mg/dL" in amber (#F59E0B)
   - Comparison: Raw vs Smoothed

### Visual Flow
- Arrows showing calculation flow
- Grid-aligned step boxes
- Clear numerical progression

---

## Prompt for Image Generation

```
A 16:9 presentation slide in blueprint engineering style showing EWMA numeric calculation example.

Background: Blueprint off-white paper (#FAF8F5) with light gray (#E5E5E5) grid overlay.

Layout: Split-screen design

Left side:
- Formula box with engineering blue (#2563EB) border:
  "trend(i) = (1-α) × Σ α^t × x_{i-t}"
  Label "Eq. 11"
- Parameter box: "α = 0.3"
- Small bar chart showing input [120, 125, 130] mg/dL
- Small exponential decay curve showing weights decreasing

Right side - Calculation Trace:
- Step 1 box: Weight table
  | t | α^t | Weight |
  | 0 | 1.000 |
  | 1 | 0.300 |
  | 2 | 0.090 |

- Step 2 box: Weighted Sum
  "130×1.0 + 125×0.3 + 120×0.09 = 178.3"

- Step 3 box: Final Result (highlighted in amber #F59E0B)
  "trend(3) = 0.7 × 178.3 = 124.81 mg/dL"

- Result comparison:
  "Raw: 130 → Smoothed: 124.81"

Typography:
- Headline "NUMERIC EXAMPLE · 数值示例" bold, deep slate (#334155), at top
- Sub-headline "Exponential Weighted Moving Average (EWMA) - Eq. 11"

Style: Technical blueprint with step-by-step calculation boxes, orthogonal flow arrows, amber highlights for final results. No decorative elements, no slide numbers.
```
