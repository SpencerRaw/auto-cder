# CD Memory Evolution Prompt Templates

## CD-IDE (Idea Direction Evolution)

```
You are analyzing promising carbon dot research directions.

Given:
- User goal G^CD: {{goal}}
- Top-3 ranked CD ideas: {{top_3_ideas}}
- Elo ratings: {{elo_ratings}}

Summarize 3-5 promising research directions. For each direction:
1. State the direction clearly ("N-doped CDs from [precursor A] + [dopant B] for [application C]")
2. Cite evidence from the ranked ideas (why this direction scored high)
3. Note any consistent patterns (e.g., "all top-3 ideas use hydrothermal synthesis at 180°C")
4. Flag unexplored neighboring directions worth investigating

Output JSON:
{
  "directions": [
    {
      "statement": "...",
      "evidence": ["..."],
      "patterns": ["..."],
      "neighbors": ["..."]
    }
  ]
}
```

## CD-IVE (Idea Validation Evolution)

```
You are analyzing the outcome of a carbon dot experiment.

Given:
- CD proposal P^CD: {{proposal}}
- Execution report W^CD: {{execution_report}}
- 5-stage execution histories: {{histories}}

Classify the outcome:

1. SUCCESS: IF (QY > 20% OR application met benchmark) AND all stages completed
   → Extract what worked: precursor ratio, synthesis conditions, characterization approach
   → REINFORCE this direction

2. IMPLEMENTATION_FAILURE: IF synthesis partially worked (fluorescence observed but QY < 5%)
   → Diagnose root cause: insufficient doping? wrong temperature? purification issue?
   → Suggest protocol fixes for next iteration

3. FUNDAMENTAL_FAILURE: IF no CD formation (no fluorescence, no nanoparticle in TEM)
   → Record as DEAD END: this precursor combination cannot produce CDs under these conditions
   → Suggest alternative precursor or synthesis method

Output JSON:
{
  "classification": "SUCCESS|IMPLEMENTATION_FAILURE|FUNDAMENTAL_FAILURE",
  "diagnosis": "...",
  "recommendation": "...",
  "reinforce_directions": [...],
  "dead_end_tags": [...]
}
```

## CD-ESE (Experiment Strategy Evolution)

```
You are distilling reusable carbon dot experiment strategies.

Given:
- CD proposal P^CD: {{proposal}}
- Full execution histories across all 5 stages: {{histories}}
- Best-performing code per stage: {{best_codes}}

Extract reusable strategies for each stage:

1. SYNTHESIS STRATEGY:
   - Optimal temperature/time/pH ranges that produced CDs
   - Precursor ratios that worked vs failed
   - Equipment-specific notes (autoclave model, microwave power)

2. PURIFICATION STRATEGY:
   - Dialysis MWCO and duration that removed unreacted precursors
   - Centrifugation speed/time for size selection
   - Column chromatography solvent gradients (if used)

3. CHARACTERIZATION STRATEGY:
   - Spectral processing pipeline that produced clean data
   - QY calculation reference standard and correction factors
   - TEM image analysis parameters (threshold, particle counting method)

4. APPLICATION STRATEGY:
   - Interference study design that caught false positives
   - Calibration curve construction method
   - Statistical tests used for significance

5. REPRODUCIBILITY STRATEGY:
   - Environmental factors that affected batch consistency
   - Storage conditions that maintained stability
   - QC checklist for new batches

Output JSON with reusable code templates and parameter grids for each stage.
```
