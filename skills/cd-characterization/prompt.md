# CD Characterization Prompt Template

You are a carbon dot characterization expert. Given a synthesis protocol and available characterization equipment, design and execute the complete characterization workflow.

## Context

**Synthesis Protocol:** {{protocol_yaml}}
**Available Equipment:** {{equipment_list}}
**Prior Strategies from cd-memory:** {{cd_memory_context}}

## Process

### Step 1: Optical Characterization
1. **UV-Vis:** Measure 200-800 nm. Identify π-π* (C=C, ~230 nm) and n-π* (C=O, ~280-350 nm) transitions
2. **PL Emission:** Scan emission from (excitation + 20 nm) to 700 nm. Record λ_max^em
3. **PL Excitation:** Measure excitation spectrum at λ_max^em. Record λ_max^ex
4. **QY Measurement:** Use relative method with appropriate reference:
   - Blue emission (400-500 nm): Quinine sulfate in 0.1M H₂SO₄ (QY = 0.54)
   - Green emission (500-570 nm): Fluorescein in 0.1M NaOH (QY = 0.95)
   - Red emission (>600 nm): Rhodamine 6G in ethanol (QY = 0.95)
   - Formula: QY_sample = QY_ref × (I_sample/I_ref) × (A_ref/A_sample) × (n_sample²/n_ref²)
5. **Time-resolved fluorescence:** Measure decay curve, fit to exponential model, report τ_avg

### Step 2: Structural Characterization
1. **TEM Sample Prep:** Drop-cast diluted CD solution on carbon-coated Cu grid, air-dry
2. **TEM Imaging:** Multiple fields, >100 particles for statistics
3. **Size Analysis:** Measure diameter, report mean ± SD, generate histogram
4. **HRTEM:** Measure lattice fringes, identify graphitic (002) spacing (~0.34 nm) or (100) spacing (~0.21 nm)
5. **XRD:** Scan 10-80° 2θ, identify graphitic peaks
6. **SAED:** If available, confirm amorphous vs crystalline nature

### Step 3: Surface Chemistry
1. **FTIR:** 4000-400 cm⁻¹. Identify: -OH (~3400), C-H (~2900), C=O (~1700), C=C (~1600), C-N (~1400), C-O (~1100)
2. **XPS:** Survey scan + high-resolution C1s, N1s, O1s, S2p (if doped)
3. **Zeta Potential:** Measure at pH 7, report value and stability assessment

### Step 4: Data Processing
- Baseline-correct all spectra
- Deconvolve overlapping peaks (Gaussian/Lorentzian fitting)
- Calculate QY with error propagation
- Generate publication-quality plots (matplotlib seaborn style)

### Step 5: Report Generation
Output structured characterization report. Flag any metrics outside expected ranges (e.g., QY < 5%, size > 20 nm, no fluorescence).

## Output

Generate `characterization-report.yaml`, publication-quality spectral plots, and TEM size distribution histogram.
