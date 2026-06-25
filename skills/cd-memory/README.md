# cd-memory

## Persistent CD Research Memory

The self-evolution layer for Auto-CDer. Stores and evolves CD research knowledge across experiment cycles through two memory modules and three evolution mechanisms.

### Architecture

```
cd-memory/
├── M_I^CD (Ideation Memory)
│   ├── directions/          # Promising CD research directions (from CD-IDE)
│   │   ├── precursor-patterns.json
│   │   ├── doping-strategies.json
│   │   └── property-maps.json
│   └── validation/          # Validated/refuted hypotheses (from CD-IVE)
│       ├── successful.json
│       └── dead-ends.json
│
└── M_E^CD (Experimentation Memory)
    ├── synthesis/            # Reusable synthesis protocols (from CD-ESE)
    │   ├── hydrothermal/
    │   ├── microwave/
    │   └── pyrolysis/
    ├── characterization/     # Characterization workflows
    │   ├── optical/
    │   ├── structural/
    │   └── surface/
    ├── application/          # Application validation scripts
    │   ├── sensing/
    │   ├── bioimaging/
    │   └── catalysis/
    └── reproducibility/      # Batch consistency checklists
```

### Three Evolution Mechanisms

#### 1. CD-IDE (Idea Direction Evolution)
- **Trigger:** After every completed CD idea generation cycle
- **Input:** $G^{CD}$, top-3 ranked ideas $\mathbf{I}_{top}^{CD}$
- **Action:** Summarize promising research directions: "N-doped CDs from citric acid + urea consistently achieve QY 40-60% in hydrothermal synthesis at 180°C/6h"
- **Write to:** `M_I^CD/directions/`

#### 2. CD-IVE (Idea Validation Evolution)
- **Trigger:** After every completed CD experiment cycle
- **Input:** $P^{CD}$ (proposal), $W^{CD}$ (execution report)
- **Action:** Classify outcomes:
  - **Success** (QY > 20%, application works) → reinforce direction
  - **Implementation Failure** (synthesis error, equipment issue) → flag protocol gaps
  - **Fundamental Failure** (no fluorescence, app mechanism invalid) → record dead-end
- **Write to:** `M_I^CD/validation/`

#### 3. CD-ESE (Experiment Strategy Evolution)
- **Trigger:** After every completed 5-stage experiment cycle
- **Input:** $P^{CD}$, $\{H_E^s\}_{s=1}^5$ (full execution histories)
- **Action:** Distill reusable strategies:
  - **Synthesis Strategy:** Optimal T/t/pH grids, precursor ratios that worked
  - **Characterization Strategy:** Spectral processing pipelines, QY calculation templates
  - **Application Strategy:** Interference study designs, calibration protocols
- **Write to:** `M_E^CD/`

### Memory Retrieval

Uses `mxbai-embed-large` embeddings with cosine similarity:
- `Retrieve_I(M_I^CD, G^{CD})` — retrieves top-$k_I$ ideation items relevant to goal
- `Retrieve_E(M_E^CD, P^{CD})` — retrieves top-$k_E$ experiment strategies relevant to proposal

### Integration

- **Read by:** `cd-synthesis`, `cd-literature` (ideation phase); `cd-characterization`, `cd-application` (experiment phase)
- **Written by:** Evolution Manager Agent (EMA) after each task completion
- **Persistence:** `~/.autocder/memory/` (file-based, JSON + embeddings)

### Design Principle

Memory is the **moat** — the more CD experiments Auto-CDer runs, the better its synthesis proposals, characterization workflows, and application designs become. This is the same self-improving loop that makes EvoScientist effective.
