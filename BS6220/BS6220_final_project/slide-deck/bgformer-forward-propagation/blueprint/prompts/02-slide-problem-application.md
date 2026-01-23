# Slide 02: Problem & Application

## Image Specifications

- **Aspect Ratio**: 16:9 (1920 x 1080 px)
- **Format**: PNG
- **Filename**: 02-slide-problem-application.png

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
- **Body**: Aptos, 20-24pt

---

## Content Specifications

### Headline
**PROBLEM & APPLICATION · 问题与应用**

### Algorithm Purpose (算法目的)
- **Task**: Time-series prediction for blood glucose levels
- **Goal**: Predict 60-90 minutes ahead for early intervention

### Real-World Application (真实应用)
**Diabetes Management Early Warning System**
- Input: CGM data (5-min intervals)
- Output: Actionable glucose prediction
- Benefit: Prevent hypoglycemia/hyperglycemia events

### Why BGformer?
- Captures periodic patterns (meals, sleep cycles)
- Extracts trend information (EWMA smoothing)
- Efficient attention mechanism (linear complexity)

---

## Visual Description

### Layout: Three-Section
- **Left**: Problem definition block
- **Center**: Application scenario illustration
- **Right**: Solution highlights

### Key Visual Elements

1. **Problem Block**
   - CGM waveform icon
   - Time arrow showing 60-90 min prediction window
   - Dimension lines indicating the gap to predict

2. **Application Block**
   - Diabetes patient icon (simple, schematic)
   - Alert/warning indicator
   - "Early Warning" label with amber highlight

3. **Solution Block**
   - Three key features in list format
   - Checkmarks in engineering blue

### Flow Arrows
- Orthogonal arrows connecting Problem → Application → Solution
- Left-to-right data flow

---

## Prompt for Image Generation

```
A 16:9 presentation slide in blueprint engineering style showing problem definition and application.

Background: Blueprint off-white paper (#FAF8F5) with light gray (#E5E5E5) grid overlay.

Layout: Three-section horizontal design

Left section - Problem:
- Title: "Blood Glucose Prediction Challenge"
- CGM waveform signal icon
- Time dimension line showing "60-90 min prediction window"
- Engineering blue (#2563EB) outlined box

Center section - Application:
- Title: "Diabetes Early Warning System"
- Simple patient monitoring schematic
- Alert indicator highlighted in amber (#F59E0B)
- Arrow showing "CGM Data → Prediction → Alert"

Right section - Solution:
- Title: "Why BGformer?"
- Three bullet points with checkmarks:
  - "Periodic pattern capture"
  - "Trend extraction (EWMA)"
  - "Efficient attention O(W×L)"
- Engineering blue checkmark icons

Connections: Orthogonal arrows linking the three sections left-to-right.

Typography:
- Headline "PROBLEM & APPLICATION · 问题与应用" bold sans-serif, deep slate (#334155), at top

Style: Technical blueprint with clean blocks, orthogonal connections, no decorative elements, no slide numbers.
```
