#!/usr/bin/env python3
"""
Slide Deck Image Generator using Google Gemini 3 Pro Image Preview
Generates professional presentation slide images
"""

import os
import sys
import time
from pathlib import Path

# Set UTF-8 encoding for console output
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'replace')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'replace')

try:
    from google import genai
    from google.genai import types
except ImportError:
    print("Installing google-genai...")
    os.system(f"{sys.executable} -m pip install google-genai -q")
    from google import genai
    from google.genai import types

# Configuration
GOOGLE_API_KEY = "AIzaSyCiaZeyKS-Wya63DoE328lxI_kLUpvyb0Q"

# 7 slides content for Scientific style
SLIDES = [
    {
        "filename": "01-cover.png",
        "prompt": """Create a professional academic presentation cover slide.

Title: "Forward Propagation"
Subtitle: "BGformer Blood Glucose Prediction Model - Mathematical Expression"
Course: "BS6220: Spatial and Multi-omics Data Analytics"

Style:
- Clean white/light gray background
- Professional academic style
- Large bold title at center
- Subtitle below in smaller text
- Course info at bottom
- Simple glucose molecule or neural network icon as decoration
- 16:9 aspect ratio landscape orientation
- No slide numbers"""
    },
    {
        "filename": "02-problem-context.png",
        "prompt": """Create a professional presentation slide about blood glucose prediction.

Title: "Problem Context: Blood Glucose Prediction"

Content to show:
- Left side: Simple icon of a glucose monitor/CGM device
- Right side: Key points as bullet list:
  * Input: Continuous glucose monitoring data (5-min intervals)
  * Challenge: Predict glucose 60-90 minutes ahead
  * Application: Early warning for diabetes management
  * Solution: BGformer transformer-based model

Style:
- Clean white background
- Professional academic style
- Clear readable text (Aptos or similar sans-serif font)
- 16:9 landscape orientation
- Blue accent color for highlights
- No slide numbers"""
    },
    {
        "filename": "03-forward-propagation.png",
        "prompt": """Create a professional presentation slide showing forward propagation pipeline.

Title: "Forward Propagation Pipeline"

Show a horizontal flow diagram with boxes and arrows:
[Input] -> [FEM Module] -> [Encoder] -> [Decoder] -> [Output]

Below each box, add Chinese labels:
Input: "Blood Glucose Data"
FEM: "Feature Enhancement"
Encoder: "MOC Attention"
Decoder: "DAM Fusion"
Output: "Prediction"

Style:
- Clean white background
- Professional flow diagram with rounded rectangles
- Arrows connecting each stage
- Blue/teal color scheme
- 16:9 landscape orientation
- Clear readable labels
- No slide numbers"""
    },
    {
        "filename": "04-periodic-features.png",
        "prompt": """Create a professional presentation slide about periodic feature extraction.

Title: "FEM Module: Periodic Features (Eq. 5-7)"

Content:
Left side - Formulas in a box:
  hour_of_day(x) = hour(x) / 23 - 0.5
  minute_of_hour(x) = minute(x) / 59 - 0.5
  Range: [-0.5, +0.5]

Right side - Numeric Example table:
| Timestamp | hour_of_day | minute_of_hour |
| 08:15:30  | -0.152      | -0.246         |
| 08:20:30  | -0.152      | -0.161         |

Style:
- Clean white background
- Two-column layout
- Formula box on left with light blue background
- Data table on right
- Professional academic style
- 16:9 landscape
- No slide numbers"""
    },
    {
        "filename": "05-trend-features.png",
        "prompt": """Create a professional presentation slide about trend feature extraction.

Title: "FEM Module: Trend Features (Eq. 11)"

Content:
Formula: trend(i) = (1-alpha) * SUM(alpha^t * x_{i-t})

Numeric Example (show step by step):
- Parameters: alpha = 0.3
- Input: [120, 125, 130] mg/dL
- Weights: [1, 0.3, 0.09]
- Calculation: 130 + 37.5 + 10.8 = 178.3
- Result: trend = 0.7 * 178.3 = 124.81 mg/dL

Include a small line chart showing raw data vs smoothed trend line.

Style:
- Clean white background
- Formula at top
- Step-by-step calculation in center
- Small chart at bottom right
- Professional academic style
- 16:9 landscape
- No slide numbers"""
    },
    {
        "filename": "06-experimental-results.png",
        "prompt": """Create a professional presentation slide showing experimental results.

Title: "Experimental Results (60-min Prediction)"

Content:
Dataset info: DirecNet, 16 diabetic patients, 5-min intervals

Comparison table:
| Model       | MAE    | RMSE   |
| ARIMA       | 56.03  | 69.88  |
| LSTM        | 28.44  | 35.70  |
| Transformer | 29.33  | 38.15  |
| Informer    | 28.47  | 37.06  |
| BGformer    | 23.46  | 31.35  | <- highlight this row

Key Result: BGformer achieves 14% improvement over Informer

Style:
- Clean white background
- Data table with BGformer row highlighted in light green or blue
- Clear comparison visualization
- Professional academic style
- 16:9 landscape
- No slide numbers"""
    },
    {
        "filename": "07-contribution.png",
        "prompt": """Create a professional presentation slide for team contribution.

Title: "Team Contribution"

Content layout with placeholder text:
- Class Presentation: [Name 1, Name 2]
- Recorded Presentation: [Name 3]
- Research & Slides: [Name 4, Name 5]
- Numeric Example: [Name 6]
- Coordination: [Name 7]

At bottom:
"AI Tools Used: Claude AI for content generation, Google Gemini for slide images"

Reference:
[1] Xue et al. (2024). BGformer: An improved Informer model. Journal of Biomedical Informatics.

Style:
- Clean white background
- Bullet list format
- Professional academic style
- 16:9 landscape
- No slide numbers"""
    }
]


def generate_with_gemini3(prompt: str, output_path: str, retry_count: int = 2) -> bool:
    """Generate image using Gemini 3 Pro Image Preview"""
    client = genai.Client(api_key=GOOGLE_API_KEY)

    for attempt in range(retry_count + 1):
        try:
            response = client.models.generate_content(
                model='gemini-3-pro-image-preview',
                contents=prompt,
                config=types.GenerateContentConfig(
                    response_modalities=['IMAGE', 'TEXT'],
                )
            )

            if response.candidates:
                for candidate in response.candidates:
                    if candidate.content and candidate.content.parts:
                        for part in candidate.content.parts:
                            if hasattr(part, 'inline_data') and part.inline_data:
                                os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else '.', exist_ok=True)
                                with open(output_path, 'wb') as f:
                                    f.write(part.inline_data.data)
                                print(f"[OK] Generated: {os.path.basename(output_path)}")
                                return True

            print(f"  Attempt {attempt + 1}: No image in response")

        except Exception as e:
            error_msg = str(e)
            print(f"  Attempt {attempt + 1} failed: {error_msg[:100]}")
            if "429" in error_msg or "quota" in error_msg.lower():
                print("  Rate limit hit, waiting 30 seconds...")
                time.sleep(30)
            elif attempt < retry_count:
                time.sleep(5)

    print(f"[FAILED] {os.path.basename(output_path)}")
    return False


def main():
    """Main function to generate all 7 slides"""
    output_dir = Path(__file__).parent / "scientific-gemini3"
    output_dir.mkdir(exist_ok=True)

    total = len(SLIDES)
    success = 0

    print(f"\n{'='*50}")
    print(f"Generating {total} slides with Gemini 3 Pro")
    print(f"{'='*50}")

    for i, slide in enumerate(SLIDES, 1):
        output_path = str(output_dir / slide["filename"])

        # Skip if already exists
        if os.path.exists(output_path):
            print(f"[{i}/{total}] Skipping {slide['filename']} (already exists)")
            success += 1
            continue

        print(f"\n[{i}/{total}] Generating {slide['filename']}...")

        if generate_with_gemini3(slide["prompt"], output_path):
            success += 1

        # Rate limiting
        time.sleep(5)

    print(f"\n{'='*50}")
    print(f"GENERATION COMPLETE: {success}/{total} slides")
    print(f"Output directory: {output_dir}")
    print(f"{'='*50}")


if __name__ == "__main__":
    main()
