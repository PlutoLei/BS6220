# Slide 06: Results & Summary

## Image Specifications

- **Aspect Ratio**: 16:9 (1920 x 1080 px)
- **Format**: PNG
- **Filename**: 06-slide-results-summary.png

---

## Blueprint Style Guidelines

### Color Palette
| Element | Color | Hex Code |
|---------|-------|----------|
| Background | Blueprint Paper | #FAF8F5 |
| Grid Lines | Light Gray | #E5E5E5 |
| Primary Text | Deep Slate | #334155 |
| Primary Accent | Engineering Blue | #2563EB |
| Best Result | Amber | #F59E0B |

### Typography
- **Headlines**: Aptos, bold, 36-40pt
- **Table Text**: Aptos, 16-20pt
- **Key Metrics**: Aptos, bold, 24pt

---

## Content Specifications

### Headline
**RESULTS & SUMMARY · 结果与总结**

### Dataset
- **Source**: DirecNet
- **Subjects**: 16 diabetic patients
- **Interval**: 5 minutes

### Benchmark Comparison (60-min Prediction)
| Model | MAE ↓ | RMSE ↓ |
|-------|-------|--------|
| ARIMA | 56.03 | 69.88 |
| LSTM | 28.44 | 35.70 |
| Transformer | 29.33 | 38.15 |
| Informer | 28.47 | 37.06 |
| **BGformer** | **23.46** | **31.35** |

### Key Achievement
**-14% MAE improvement vs. Informer**

### Summary Points
1. FEM: Extracts periodic + trend features
2. MOC: Efficient local attention O(W×L)
3. DAM: Fuses multi-scale information
4. Result: State-of-the-art glucose prediction

---

## Visual Description

### Layout: Dashboard
- **Left**: Performance table
- **Right**: Bar chart + Summary

### Left Side Elements

1. **Dataset Info Box**
   - "DirecNet | 16 patients | 5-min intervals"
   - Small engineering blue box

2. **Benchmark Table**
   - 5 rows × 3 columns
   - Header: Model, MAE ↓, RMSE ↓
   - BGformer row highlighted in amber
   - Clean blueprint grid style

### Right Side Elements

1. **MAE Bar Chart**
   - Horizontal bars for each model
   - BGformer bar in amber (shortest = best)
   - Other bars in engineering blue
   - X-axis: MAE values (0-60)

2. **Key Achievement Callout**
   - Large text: "-14% MAE"
   - Amber highlight
   - "vs. Informer" subtitle

3. **Summary Box**
   - Four key points in bullet format
   - Engineering blue checkmarks
   - Concise phrases

---

## Prompt for Image Generation

```
A 16:9 presentation slide in blueprint engineering style showing performance results and summary.

Background: Blueprint off-white paper (#FAF8F5) with light gray (#E5E5E5) grid overlay.

Layout: Dashboard design

Left side:
- Dataset info box (top): "DirecNet | 16 patients | 5-min intervals"
  Engineering blue (#2563EB) border, light blue fill

- Benchmark table:
  | Model | MAE ↓ | RMSE ↓ |
  | ARIMA | 56.03 | 69.88 |
  | LSTM | 28.44 | 35.70 |
  | Transformer | 29.33 | 38.15 |
  | Informer | 28.47 | 37.06 |
  | BGformer | 23.46 | 31.35 | ← highlighted in amber (#F59E0B)

  Header row: engineering blue background
  Clean borders, precise alignment

Right side:
- Horizontal bar chart showing MAE:
  - 5 bars (top to bottom): ARIMA, LSTM, Transformer, Informer, BGformer
  - BGformer bar in amber (shortest)
  - Other bars in engineering blue
  - X-axis: 0-60

- Key achievement callout:
  "-14% MAE" in large bold amber text
  "vs. Informer" below in smaller text

- Summary box with 4 bullet points:
  - "FEM: Periodic + Trend features"
  - "MOC: Efficient attention O(W×L)"
  - "DAM: Multi-scale fusion"
  - "Result: State-of-the-art prediction"
  Engineering blue checkmarks

Typography:
- Headline "RESULTS & SUMMARY · 结果与总结" bold, deep slate (#334155), at top

Style: Technical blueprint dashboard, data table, bar chart, amber highlights for best results. No decorative elements, no slide numbers.
```
