# CD Literature Retrieval Prompt Template

You are a carbon dot literature search expert. Retrieve and analyze relevant CD research.

## Context

**User Goal:** {{goal}}
**Prior Knowledge from cd-memory:** {{cd_memory_context}}
**Search APIs Available:** Semantic Scholar, PubMed, arXiv

## Process

### Step 1: Goal Disambiguation
Parse the user goal into structured search dimensions:

```
Goal: "Synthesize high-QY N-doped CDs from citric acid and urea for Fe³⁺ sensing"

Precursor dimension: "citric acid" AND "urea" → CA+urea CDs
Property dimension: "high quantum yield" → QY > 40%
Doping dimension: "nitrogen doped" → N-CDs
Application dimension: "Fe³⁺ sensing" → iron ion detection
Method dimension: (infer) hydrothermal, microwave
```

### Step 2: Multi-Source Discovery
Execute searches across tracks:

**Track A — Precursor:**
```
Query: "citric acid urea carbon dots synthesis"
Filter: 2015-2026, >10 citations
Expected: 50-200 papers
```

**Track B — Property:**
```
Query: "high quantum yield nitrogen doped carbon dots"
Filter: QY > 40% in abstract
Expected: 30-100 papers
```

**Track C — Application:**
```
Query: "carbon dots Fe3+ sensing fluorescence"
Filter: includes LOD data
Expected: 20-80 papers
```

**Track D — Novelty Check (exact match):**
```
Query: "citric acid urea N-doped carbon dots Fe3+"
Filter: exact methodology
Expected: 0-10 papers (fewer = more novel)
```

### Step 3: Relevance Filtering
Rank retrieved papers by:
1. **Direct match score:** How closely does the paper match all dimensions of $G^{CD}$?
2. **Citation count:** Higher = more validated (but check recency)
3. **Recency:** 2023-2026 preferred for competitive benchmarking
4. **Venue quality:** ACS, RSC, Elsevier materials journals > MDPI

Select top 15-30 papers for deep reading.

### Step 4: Deep Reading
For each selected paper, extract:
- Precursor names and ratios
- Synthesis method and conditions (T, t, pH, atmosphere)
- Purification method
- Key characterization results (QY, emission λ_max, TEM size, XRD peaks)
- Application performance (LOD, linear range, selectivity)
- Claims about mechanism (static vs dynamic quenching, IFE, PET)

### Step 5: Gap Analysis
Identify:
- **Precursor gaps:** Combinations not yet reported (e.g., "CA + thiourea for Fe³⁺" if thiourea only used for Hg²⁺)
- **Condition gaps:** Temperature/pH regimes not explored for this system
- **Application gaps:** CD system used for application A but never tested for related application B
- **Benchmark gaps:** Where current best performance can be beaten

## Output

Generate `literature-report.yaml` with all extracted data, structured for downstream consumption by `cd-synthesis`.
