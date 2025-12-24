# BS6220 Group Assignment: Spatial Transcriptomics Analysis of Hepatocellular Carcinoma Treatment Response

## Overview

This project analyzes spatial transcriptomics data from hepatocellular carcinoma (HCC) patients to understand treatment response patterns using 10x Genomics Visium technology. The analysis compares cell type compositions and ligand-receptor interactions across different treatment response categories.

## Data Description

- **Samples**: 26 paired samples from HCC patients (Pre-treatment and Post-treatment)
- **Quality Control**: 21 samples passed QC (81% pass rate)
- **Technology**: 10x Genomics Visium spatial transcriptomics
- **Normalization**: SCTransform (SCT)

### Response Categories

| Category | Description | Sample Count |
|----------|-------------|--------------|
| NR | Non-Responder | 12 samples |
| Progressor | Disease Progression | 2 samples |
| Super Responder | Excellent Response | 8 samples |
| Unknown | Unclassified | 4 samples |

## Analysis Methods

### Cell Type Deconvolution
- **RCTD** (Robust Cell Type Decomposition)
- **cell2location**
- **CARD** (Cell Type Annotation using Reference Dataset)

### Ligand-Receptor Interaction Analysis
- **CellChat**
- **CellPhoneDB**
- **COMMOT** (COMMunication analysis by Optimal Transport)

## Repository Structure

```
BS6220/
├── README.md
└── Group Assignment/
    ├── Analysis_Report_Final.md    # Comprehensive analysis report
    ├── README.md
    └── figures/                     # All visualization outputs
        ├── celltype_*.png          # Cell type analysis figures
        ├── lr_*.png                # Ligand-receptor analysis figures
        ├── spatial_*.png           # Spatial visualization figures
        ├── dimplot_*.png           # UMAP clustering figures
        ├── method_comparison_*.png # Tool comparison figures
        └── marker_heatmap.png      # Marker gene heatmap
```

## Key Figures

### Spatial Visualizations
- `spatial_all_response_types_combined.png` - Spatial cluster distribution comparing Pre/Post treatment across response categories
- `spatial_clusters_*.png` - Individual sample spatial clustering
- `spatial_features_*.png` - Spatial feature expression patterns
- `spatial_colocalization.png` - Cell type co-localization analysis

### UMAP Clustering
- `dimplot_all_response_types_combined.png` - UMAP visualization comparing Pre/Post treatment for NR, Progressor, and Super Responder samples

### Cell Type Analysis
- `celltype_heatmap_response.png` - Cell type proportion heatmap by response
- `celltype_boxplot_response.png` - Cell type distribution boxplots
- `celltype_timepoint_interaction.png` - Pre/Post treatment comparison

### Ligand-Receptor Analysis
- `lr_heatmap_response.png` - L-R interaction intensity heatmap
- `lr_barplot_response.png` - L-R interaction frequency
- `lr_timepoint_interaction.png` - Treatment-induced L-R changes

### Method Comparison
- `method_comparison_celltype.png` - Comparison of cell type deconvolution tools
- `method_comparison_lr.png` - Comparison of L-R interaction tools

## Key Findings

1. **Super Responders** show distinct spatial clustering patterns with increased immune cell infiltration post-treatment
2. **Non-Responders** maintain similar cell type compositions before and after treatment
3. **Progressors** exhibit expansion of tumor-associated cell populations
4. Different deconvolution methods show high concordance for major cell types
5. L-R interaction analysis reveals treatment-induced changes in immune-tumor communication

## Technical Notes

- All 26 samples contain SCT (SCTransform) normalized data
- Per-sample analysis approach avoids cross-sample dimension mismatch issues
- Spatial coordinates extracted using `GetTissueCoordinates()` for visualization

## Authors

BS6220 Course Group Assignment

## License

This project is for educational purposes as part of the BS6220 course.
