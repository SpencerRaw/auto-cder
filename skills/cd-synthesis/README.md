# cd-synthesis

## Carbon Dot Synthesis Protocol Generation

Generates executable carbon dot synthesis protocols from user goals. Covers precursor selection, doping strategy, synthesis method, and reaction condition optimization.

### Stages

1. **Precursor Analysis** — Evaluate precursor candidates (citric acid, phenylenediamine, biomass, etc.) for target emission properties
2. **Doping Strategy** — Select dopant elements (N, S, P, B) and dopant precursors based on target QY and emission wavelength
3. **Method Selection** — Choose synthesis method (hydrothermal, microwave, pyrolysis, electrochemical, ultrasonic) with justification
4. **Condition Optimization** — Propose temperature, time, pH, precursor ratio with ranges for optimization
5. **Protocol Generation** — Output step-by-step executable synthesis protocol with safety notes

### Output Format

```yaml
protocol:
  precursor:
    primary: <precursor name>
    ratio: <mass or molar ratio>
    dopant: <dopant precursor>
    dopant_ratio: <ratio>
  solvent: <water/ethanol/DMF/etc>
  method: <hydrothermal/microwave/pyrolysis>
  conditions:
    temperature: <°C>
    time: <hours>
    pH: <value or range>
  expected:
    qy_range: <min-max %>
    emission_range: <min-max nm>
    color_under_uv: <blue/green/red/etc>
  safety_notes:
    - <note 1>
    - <note 2>
```

### Integration

- Reads from `cd-memory` for successful precursor-dopant patterns
- Hands off to `cd-characterization` for the characterization plan
- Hands off to `cd-application` for application validation design
