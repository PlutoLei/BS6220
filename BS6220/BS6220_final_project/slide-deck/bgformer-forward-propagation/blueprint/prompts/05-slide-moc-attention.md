# Slide 05: MOC Attention Mechanism

## Image Specifications

- **Aspect Ratio**: 16:9 (1920 x 1080 px)
- **Format**: PNG
- **Filename**: 05-slide-moc-attention.png

---

## Blueprint Style Guidelines

### Color Palette
| Element | Color | Hex Code |
|---------|-------|----------|
| Background | Blueprint Paper | #FAF8F5 |
| Grid Lines | Light Gray | #E5E5E5 |
| Primary Text | Deep Slate | #334155 |
| Primary Accent | Engineering Blue | #2563EB |
| Secondary Accent | Navy Blue | #1E3A5F |
| Highlight | Amber | #F59E0B |

### Typography
- **Headlines**: Aptos, bold, 36-40pt
- **Specifications**: Aptos, 18-22pt
- **Formulas**: Aptos/Monospace, 16-18pt

---

## Content Specifications

### Headline
**MOC ATTENTION · 微尺度重叠关注机制**

### Sub-headline
**Microscale Overlapping Concerns - Eq. 12-14**

### Core Innovation
Standard Transformer attention has O(L²) complexity.
MOC reduces this to O(W×L) via windowed local attention.

### Window Parameters
- **W**: Window size
- **O**: Overlap between windows

### Window Overlap Diagram (W=3, O=1)
```
Sequence: [t1] [t2] [t3] [t4] [t5]
Window 1:  [=========]
Window 2:       [=========]
Window 3:            [=========]
```

### Attention Formula
```
Attention(Q,K,V) = softmax(Q·K^T / √d_k) · V
```

### Complexity Comparison
| Method | Complexity |
|--------|------------|
| Standard | O(L²) |
| MOC | O(W×L) |

---

## Visual Description

### Layout: Split-Screen
- **Left**: Window overlap schematic
- **Right**: Attention matrix & complexity

### Left Side Elements

1. **Window Overlap Diagram**
   - Horizontal sequence bar: [t1, t2, t3, t4, t5]
   - Three overlapping window brackets below
   - Window 1: t1-t3 (engineering blue)
   - Window 2: t2-t4 (navy blue)
   - Window 3: t3-t5 (engineering blue)
   - Overlap regions in light blue fill
   - Dimension lines: W=3, O=1

2. **Parameter Labels**
   - "Window Size: W=3"
   - "Overlap: O=1"

### Right Side Elements

1. **Sparse Attention Matrix**
   - 5×5 grid visualization
   - Diagonal blocks filled (windowed attention)
   - Off-diagonal empty (computational savings)
   - Engineering blue filled cells

2. **Complexity Box**
   - "Standard: O(L²)" (dimmed/strikethrough)
   - "MOC: O(W×L)" (amber highlight)
   - Arrow showing reduction

3. **Formula Box**
   - Attention equation
   - "Eq. 12-14" label

---

## Prompt for Image Generation

```
A 16:9 presentation slide in blueprint engineering style showing MOC windowed attention mechanism.

Background: Blueprint off-white paper (#FAF8F5) with light gray (#E5E5E5) grid overlay.

Layout: Split-screen design

Left side - Window Overlap Diagram:
- Horizontal sequence bar: 5 blocks labeled [t1] [t2] [t3] [t4] [t5]
- Three overlapping window brackets below:
  - Window 1: spans t1-t3 (engineering blue #2563EB)
  - Window 2: spans t2-t4 (navy blue #1E3A5F)
  - Window 3: spans t3-t5 (engineering blue)
- Overlap regions (t2, t3, t4) highlighted with light blue (#BFDBFE)
- Dimension lines showing "W=3" and "O=1"

Right side:
- Sparse attention matrix (5×5 grid):
  - Diagonal blocks filled with engineering blue
  - Off-diagonal areas empty/white
  - Shows computational savings visually

- Complexity comparison box:
  - "Standard Attention: O(L²)" with strikethrough
  - Arrow pointing to
  - "MOC Attention: O(W×L)" highlighted in amber (#F59E0B)

- Formula box with engineering blue border:
  "Attention = softmax(Q·K^T / √d_k) · V"
  Label "Eq. 12-14"

Typography:
- Headline "MOC ATTENTION · 微尺度重叠关注机制" bold, deep slate (#334155), at top
- Sub-headline "Microscale Overlapping Concerns - Eq. 12-14"

Style: Technical blueprint with window schematic, sparse matrix visualization, complexity comparison. Orthogonal elements only, no decorative elements, no slide numbers.
```
