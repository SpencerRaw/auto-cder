# CD Application Validation Prompt Template

You are a carbon dot application expert. Given characterized CDs, design and validate the optimal application.

## Context

**Characterization Report:** {{characterization_report}}
**User Goal Application Domain:** {{application_domain}}
**Prior Strategies from cd-memory:** {{cd_memory_context}}

## Process

### Step 1: Application Selection
Map CD properties to application suitability:

| CD Property | Best Application | Rationale |
|---|---|---|
| High QY (>50%), blue emission | Metal ion sensing | Strong signal, easy quenching detection |
| Red emission (>600 nm) | Bioimaging | Tissue penetration, low autofluorescence |
| Surface -NH₂, -COOH groups | pH sensing / drug delivery | pH-responsive fluorescence |
| Narrow bandgap | Photocatalysis | Efficient visible light absorption |
| N,S co-doped | Multi-ion sensing | Diverse binding sites for different metals |
| Biomass-derived, low toxicity | In vivo bioimaging | Biocompatible by origin |

### Step 2: Protocol Design

**For Sensing:**
- Prepare CD stock solution (typically 0.1-1.0 mg/mL)
- Prepare analyte stock solutions at graded concentrations
- Measure F₀ (initial fluorescence) at λ_ex/λ_em
- Titrate analyte, record F at each concentration
- For selectivity: test 15+ metal ions at same concentration (e.g., 100 μM)
- Stern-Volmer analysis: F₀/F = 1 + K_SV[Q] (static) or F₀/F = 1 + k_qτ₀[Q] (dynamic)
- LOD = 3σ/slope (from calibration curve linear region)

**For Bioimaging:**
- MTT assay: CD concentrations 0-500 μg/mL, 24h incubation, measure cell viability
- Cellular uptake: Incubate CDs with cells (50-200 μg/mL, 1-4h), wash, image on confocal
- Photostability: Continuous laser exposure, record intensity decay over 30 min
- Compare to commercial dyes (DAPI, FITC, Alexa Fluor)

### Step 3-5: Execute, Analyze, Benchmark
- Run all experiments with n ≥ 3 replicates
- Calculate metrics with 95% confidence intervals
- Compare against top-5 literature CD systems for same application
- Identify distinguishing feature (e.g., wider linear range, better selectivity for specific ion, lower cytotoxicity)

## Output

Generate `application-report.yaml` with all metrics, calibration curves, selectivity radar plots, and benchmark comparison table.
