# cd-literature

## Carbon Dot Literature Retrieval & Analysis

Retrieves and analyzes CD research literature to ground idea generation in existing knowledge. Uses Semantic Scholar API + PubMed for biomedical CD applications.

### Stages

1. **Goal Disambiguation** — Parse user goal $G^{CD}$ into search queries targeting precursor, property, and application dimensions
2. **Multi-Source Discovery** — Search Semantic Scholar, PubMed, arXiv for CD papers across three tracks:
   - **Precursor Track:** Papers using the specified precursor (e.g., "citric acid carbon dots synthesis")
   - **Property Track:** Papers achieving the target property (e.g., "high quantum yield carbon dots")
   - **Application Track:** Papers in the target application (e.g., "carbon dots Fe3+ sensing")
3. **Relevance Filtering** — Rank papers by: citation count, recency, venue quality, and goal similarity
4. **Deep Reading** — Extract synthesis protocols, characterization data, and benchmark results from top papers
5. **Gap Analysis** — Identify what has NOT been done (precursor combinations, doping strategies, applications) to guide novelty

### Search Query Generation

Given $G^{CD} = (PrecursorSet, TargetProperty, ApplicationDomain)$:

```
Precursor Track:  "{precursor_1} {precursor_2} carbon dots synthesis"
Property Track:   "{target_property} carbon dots {precursor_class}"
Application Track: "carbon dots {application_domain} detection sensing"
Novelty Check:    "{precursor_1} {dopant} carbon dots {application}" (to find exact matches)
```

### Output Format

```yaml
literature_report:
  papers_retrieved: <N>
  papers_relevant: <n>
  synthesis_protocols_extracted:
    - paper: <title>
      precursor: <name>
      method: <hydrothermal/microwave>
      conditions: {T: <°C>, t: <h>, pH: <value>}
      qy: <value>%
      application: <domain>
  benchmarks:
    - metric: <QY/LOD/size>
      best_reported: <value>
      typical_range: [<min>, <max>]
  gaps_identified:
    - <unexplored precursor combination or application>
```

### Integration

- **Feeds into:** `cd-synthesis` (literature-grounded idea generation)
- **Reads from:** `cd-memory` (previously discovered papers and dead-ends to avoid re-reading)
- **Stores to:** `cd-memory` (newly discovered papers, extracted protocols, benchmark data)
