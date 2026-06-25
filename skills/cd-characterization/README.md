# cd-characterization

## Carbon Dot Characterization Pipeline

Generates and executes characterization workflows for synthesized carbon dots. Covers structural, optical, and surface chemistry characterization.

### Stages

1. **Optical Characterization** — UV-Vis absorption, PL emission/excitation, quantum yield (QY) measurement, time-resolved fluorescence
2. **Structural Characterization** — TEM/HRTEM size analysis, XRD pattern matching, SAED analysis
3. **Surface Chemistry** — FTIR functional group identification, XPS elemental composition, zeta potential
4. **Data Processing** — Baseline correction, peak deconvolution, QY calculation (relative method with reference standard)
5. **Report Generation** — Structured characterization report with all metrics, spectra plots, and comparison to literature

### Key Metrics

| Metric | Method | Target |
|---|---|---|
| Quantum Yield (QY) | Relative method (quinine sulfate / rhodamine 6G) | >20% (baseline), >50% (good), >80% (excellent) |
| Emission wavelength | PL spectroscopy | Tunable 400-700 nm |
| Particle size | TEM image analysis | 1-10 nm (typical CDs) |
| Crystallinity | XRD / SAED | Graphitic (002) plane at ~25° |
| Surface groups | FTIR | -OH, -COOH, -NH₂, -SH |
| Elemental composition | XPS | C, N, O, S, P, B ratios |
| Colloidal stability | Zeta potential | >|±30| mV (stable) |

### Integration

- Reads synthesis protocol from `cd-synthesis`
- Hands off results to `cd-application`
- Stores characterization strategies in `cd-memory`

### Output Format

```yaml
characterization_report:
  optical:
    uv_vis_peaks: [<nm>]
    pl_emission_max: <nm>
    pl_excitation_max: <nm>
    qy: <value>%
    qy_reference: <standard name>
    lifetime: <ns>
  structural:
    tem_size_mean: <nm>
    tem_size_std: <nm>
    xrd_peaks: [{angle: <2θ>, plane: <hkl>}]
    interlayer_spacing: <nm>
  surface:
    ftir_peaks: [{wavenumber: <cm⁻¹>, assignment: <group>}]
    xps_composition: {C: <at%>, N: <at%>, O: <at%>}
    zeta_potential: <mV>
  quality_flags:
    - <flag if metric outside expected range>
```
