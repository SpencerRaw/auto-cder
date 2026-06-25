# Auto-CDer CLI Interface Design

## Design Principles
- Clean, information-dense terminal interface inspired by EvoScientist's CLI
- Color-coded stages (green = success, yellow = in-progress, red = failure, blue = info)
- Real-time streaming output with progress indicators
- Keyboard shortcuts for common actions

---

## Screen 1: Onboarding / Config

```
┌──────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│     █████╗ ██╗   ██╗████████╗ ██████╗       ██████╗██████╗ ███████╗██████╗
│    ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗     ██╔════╝██╔══██╗██╔════╝██╔══██╗
│    ███████║██║   ██║   ██║   ██║   ██║     ██║     ██║  ██║█████╗  ██████╔╝
│    ██╔══██║██║   ██║   ██║   ██║   ██║     ██║     ██║  ██║██╔══╝  ██╔══██╗
│    ██║  ██║╚██████╔╝   ██║   ╚██████╔╝     ╚██████╗██████╔╝███████╗██║  ██║
│    ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝       ╚═════╝╚═════╝ ╚══════╝╚═╝  ╚═╝
│                                                                          │
│              Autonomous Carbon Dot Experiment Researcher v0.1.0           │
│                                                                          │
│  ┌─ Configuration ────────────────────────────────────────────────────┐  │
│  │                                                                     │  │
│  │  LLM Provider [gemini]: ████████████████████████  gemini-2.5-pro    │  │
│  │  Code Model   [claude]: ████████████████████████  claude-4.5-haiku  │  │
│  │  Embeddings   [ollama]: ████████████████████████  mxbai-embed-large │  │
│  │  Workspace    [local]:  ████████████████████████  ~/.autocder/      │  │
│  │  Literature   [s2|pubmed]: █████████████████████  semantic-scholar   │  │
│  │                                                                     │  │
│  │  API Keys: [GEMINI_API_KEY ✓] [ANTHROPIC_API_KEY ✓]                 │  │
│  │                                                                     │  │
│  │  [Enter] Confirm  [Tab] Next Field  [Ctrl+C] Quit                   │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                                                          │
│  ┌─ Skills ───────────────────────────────────────────────────────────┐  │
│  │  [✓] cd-synthesis        [✓] cd-characterization                    │  │
│  │  [✓] cd-application      [✓] cd-memory                              │  │
│  │  [✓] cd-literature       [ ] cd-reproducibility (optional)          │  │
│  │                                                                     │  │
│  │  /install-skill auto-cder/skills@cd-synthesis  to add more          │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## Screen 2: Main CLI — Goal Input & Idea Generation

```
╔══════════════════════════════════════════════════════════════════════════╗
║  auto-cder > _                                                          ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  Enter your CD research goal (or /help):                                 ║
║                                                                          ║
║  > Synthesize high-QY N,S co-doped carbon dots from citric acid          ║
║    and thiourea for selective Hg²⁺ sensing in water                      ║
║                                                                          ║
║  ┌─ Parsed Goal ────────────────────────────────────────────────────┐   ║
║  │  Precursor:   citric acid + thiourea                              │   ║
║  │  Dopant:      N, S (co-doping from thiourea)                      │   ║
║  │  Property:    High quantum yield (>40%)                           │   ║
║  │  Application: Hg²⁺ sensing (aqueous)                              │   ║
║  └──────────────────────────────────────────────────────────────────┘   ║
║                                                                          ║
║  [Enter] Submit  [/help] Commands  [/memory] View Memory  [Esc] Back    ║
╚══════════════════════════════════════════════════════════════════════════╝

--- After submission, streaming output ---

╔══════════════════════════════════════════════════════════════════════════╗
║  auto-cder > Synthesize high-QY N,S co-doped carbon dots...             ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  ▸ Stage 1/5: CD Literature Retrieval                                    ║
║  ├─ [Semantic Scholar] Searching: "citric acid thiourea carbon dots"    ║
║  │  └─ Found 47 papers, 23 relevant after filtering                     ║
║  ├─ [Semantic Scholar] Searching: "N S co-doped carbon dots Hg sensing" ║
║  │  └─ Found 31 papers, 15 relevant                                     ║
║  ├─ [PubMed] Searching: "carbon dots mercury detection"                 ║
║  │  └─ Found 12 papers, 8 relevant                                      ║
║  └─ ✓ Literature retrieval complete (46 papers, 3.2s)                   ║
║                                                                          ║
║  ▸ Stage 2/5: CD Idea Generation (Idea Tree Search)                      ║
║  ├─ [cd-memory] Retrieved 2 ideation records (CA+urea N-CDs, thiourea)  ║
║  ├─ [cd-literature] Grounding ideas with 46 papers                      ║
║  ├─ Branch 1/7: CA:Thiourea=1:1, hydrothermal 180°C/6h                  ║
║  │  └─ Review: "Good precedent for thiourea as S source..."             ║
║  ├─ Branch 2/7: CA:Thiourea=1:2, microwave 200°C/15min                  ║
║  │  └─ Review: "Higher S content may red-shift emission..."             ║
║  ├─ Branch 3/7: CA:Thiourea=2:1, hydrothermal 200°C/8h                  ║
║  │  └─ Review: "Lower dopant ratio, check QY impact..."                 ║
║  │  ... generating 21 candidates (3 parallel workers) ...               ║
║  └─ ✓ 21 ideas generated, Elo tournament in progress                    ║
║                                                                          ║
║  ▸ Tournament Results:                                                   ║
║  ├─ 🥇 Idea #14 (Elo 1582): CA:Thiourea=1:2, hydrothermal 180°C/8h,    ║
║  │     pH 5, dialysis 1kDa, expect QY 45-55%, λ_em 480nm               ║
║  ├─ 🥈 Idea #7  (Elo 1541): CA:Thiourea=1:1.5, microwave 200°C/20min  ║
║  ├─ 🥉 Idea #3  (Elo 1523): CA:Thiourea=2:1, solvothermal EtOH 180°C  ║
║  └─ ✓ Top-1 extended into full proposal (P^CD generated)                ║
║                                                                          ║
║  ▸ Stage 3/5: Proposal Draft ──────────────────────────────────────     ║
║  └─ View full proposal: /proposal                                       ║
║                                                                          ║
║  Continue to experiment execution? [Y/n] _                               ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Screen 3: Experiment Execution (5-Stage CD Experiment Tree Search)

```
╔══════════════════════════════════════════════════════════════════════════╗
║  auto-cder > [EXECUTING] P^CD: N,S-CDs from CA+Thiourea for Hg²⁺       ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  ████████░░░░░░░░░░░░  Stage 1/5: Precursor & Synthesis (Attempt 3/20)  ║
║                                                                          ║
║  ┌─ Stage 1 Live ────────────────────────────────────────────────────┐  ║
║  │                                                                     │  ║
║  │  Attempt 1: CA:Thiourea=1:2, 180°C, 8h, pH 5                      │  ║
║  │  ├─ [CODE] synthesis_protocol_v1.py generated                       │  ║
║  │  ├─ [RUN]  ⏳ Hydrothermal reactor @ 180°C ... ETA 7h 52m          │  ║
║  │  ├─ [LOG]  Temperature stable at 180.3°C ± 0.5°C                   │  ║
║  │  └─ [STATUS] RUNNING (3/20 attempts used)                          │  ║
║  │                                                                     │  ║
║  │  Attempt 2: CA:Thiourea=1:1.5, 200°C, 6h, pH 7 (parallel worker)  │  ║
║  │  ├─ [CODE] synthesis_protocol_v2.py generated                       │  ║
║  │  ├─ [RUN]  ⏳ Hydrothermal reactor @ 200°C ... ETA 5h 54m          │  ║
║  │  └─ [STATUS] RUNNING                                               │  ║
║  │                                                                     │  ║
║  │  Attempt 3: CA:Thiourea=1:2, MW 200°C, 20min (queueued)           │  ║
║  │  └─ [STATUS] QUEUED                                               │  ║
║  │                                                                     │  ║
║  └─────────────────────────────────────────────────────────────────────┘  ║
║                                                                          ║
║  ┌─ Stage History ────────────────────────────────────────────────────┐  ║
║  │  Stage 1 (Synthesis):      [████████░░░░] 3/20 attempts, 0 pass    │  ║
║  │  Stage 2 (Purification):   [░░░░░░░░░░░░] pending                  │  ║
║  │  Stage 3 (Characterize):   [░░░░░░░░░░░░] pending                  │  ║
║  │  Stage 4 (Application):    [░░░░░░░░░░░░] pending                  │  ║
║  │  Stage 5 (Reproduce):      [░░░░░░░░░░░░] pending                  │  ║
║  └─────────────────────────────────────────────────────────────────────┘  ║
║                                                                          ║
║  [/stop] Abort  [/status] Details  [/log] Full Logs  [/mem] Memory      ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Screen 4: Execution Report (After Completion)

```
╔══════════════════════════════════════════════════════════════════════════╗
║  auto-cder > [COMPLETED] W^CD: Execution Report                         ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  ╔════════════════════════════════════════════════════════════════════╗  ║
║  ║                    CD EXPERIMENT REPORT                             ║  ║
║  ║         N,S co-doped CDs from Citric Acid + Thiourea               ║  ║
║  ╠════════════════════════════════════════════════════════════════════╣  ║
║  ║                                                                    ║  ║
║  ║  ┌─ Synthesis ───────────────────────────────────────────────┐    ║  ║
║  ║  │  Status: ✅ SUCCESS                                         │    ║  ║
║  ║  │  Best Protocol: CA:Thiourea = 1:2, 180°C, 8h, pH 5        │    ║  ║
║  ║  │  Yield: 23.5% (after dialysis)                             │    ║  ║
║  ║  │  UV Fluorescence: Bright blue (visible)                    │    ║  ║
║  ║  │  Attempts used: 5/20 (passed on 5th)                       │    ║  ║
║  ║  └────────────────────────────────────────────────────────────┘    ║  ║
║  ║                                                                    ║  ║
║  ║  ┌─ Characterization ────────────────────────────────────────┐    ║  ║
║  ║  │  Quantum Yield:  52.3% ± 2.1% (quinine sulfate ref)       │    ║  ║
║  ║  │  Emission λ_max: 475 nm (blue-cyan)                       │    ║  ║
║  ║  │  Excitation λ_max: 360 nm                                 │    ║  ║
║  ║  │  TEM Size:      4.2 ± 0.8 nm (n=120)                     │    ║  ║
║  ║  │  XRD:           Broad peak at 24.5° (graphitic 002)       │    ║  ║
║  ║  │  FTIR:          -OH, -NH₂, C=S, C-N, C=O confirmed        │    ║  ║
║  ║  │  Zeta Potential: -28.5 mV (moderately stable)             │    ║  ║
║  ║  └────────────────────────────────────────────────────────────┘    ║  ║
║  ║                                                                    ║  ║
║  ║  ┌─ Application: Hg²⁺ Sensing ───────────────────────────────┐    ║  ║
║  ║  │  LOD:           18.5 nM (4.5 ppb)                        │    ║  ║
║  ║  │  Linear Range:  0.05 - 50 μM (R² = 0.996)               │    ║  ║
║  ║  │  Selectivity:   Hg²⁺ >> Fe³⁺ > Cu²⁺ > others (15 ions)  │    ║  ║
║  ║  │  Response Time:  <2 min                                  │    ║  ║
║  ║  │  Mechanism:      Static quenching (K_SV = 4.2×10³ M⁻¹)  │    ║  ║
║  ║  └────────────────────────────────────────────────────────────┘    ║  ║
║  ║                                                                    ║  ║
║  ║  ┌─ Reproducibility ─────────────────────────────────────────┐    ║  ║
║  ║  │  Batch-to-Batch CV: 8.7% (QY), 5.2% (λ_em)              │    ║  ║
║  ║  │  Shelf Stability:   >30 days (QY retained >90%)          │    ║  ║
║  ║  │  Result:            ✅ REPRODUCIBLE                       │    ║  ║
║  ║  └────────────────────────────────────────────────────────────┘    ║  ║
║  ║                                                                    ║  ║
║  ║  ┌─ Evolution Summary ───────────────────────────────────────┐    ║  ║
║  ║  │  CD-IDE: "CA+Thiourea → N,S-CDs is a promising direction  │    ║  ║
║  ║  │          for high-QY blue emission with Hg²⁺ selectivity" │    ║  ║
║  ║  │  CD-IVE: ✅ SUCCESS — reinforcing this precursor-dopant   │    ║  ║
║  ║  │          combination in M_I^CD                           │    ║  ║
║  ║  │  CD-ESE: Stored synthesis protocol (180°C/8h/pH5),       │    ║  ║
║  ║  │          Hg²⁺ sensing calibration template                │    ║  ║
║  ║  └────────────────────────────────────────────────────────────┘    ║  ║
║  ║                                                                    ║  ║
║  ╚════════════════════════════════════════════════════════════════════╝  ║
║                                                                          ║
║  [/export] Save Report  [/paper] Generate Manuscript  [/next] New Goal   ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## Screen 5: Memory Inspection

```
╔══════════════════════════════════════════════════════════════════════════╗
║  auto-cder > /memory                                                     ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  ┌─ Ideation Memory (M_I^CD) ───────────────────────────────────────┐   ║
║  │                                                                     │   ║
║  │  Directions (CD-IDE) ─ 3 stored                                     │   ║
║  │  ├─ 📈 N,S co-doped CDs from CA+thiourea → high QY (45-55%)        │   ║
║  │  │   Evidence: 3 successful syntheses, average QY 49.7%             │   ║
║  │  ├─ 📈 Red-emissive CDs from o-PD + dopant → bioimaging             │   ║
║  │  │   Evidence: 2 successful, λ_em 610-635 nm                        │   ║
║  │  └─ 📈 Biomass CDs from orange peel → photocatalysis                │   ║
║  │     Evidence: 1 successful, degradation rate 92% in 60 min          │   ║
║  │                                                                     │   ║
║  │  Validation (CD-IVE) ─ 8 stored                                     │   ║
║  │  ├─ ✅ Success (5): CA+urea N-CDs, o-PD red CDs, peel cat CDs...   │   ║
║  │  ├─ ⚠️ Impl Failure (2): glucose+PEG (QY<1%), CA+EDTA (agg)        │   ║
║  │  └─ ❌ Dead Ends (1): CA+bare thiourea without pH control → no CDs  │   ║
║  └─────────────────────────────────────────────────────────────────────┘   ║
║                                                                          ║
║  ┌─ Experimentation Memory (M_E^CD) ──────────────────────────────────┐  ║
║  │                                                                     │   ║
║  │  Synthesis Strategies ─ 5 stored                                     │   ║
║  │  ├─ 🔧 Hydrothermal 180°C/8h/pH5 for CA+thio N,S-CDs                │   ║
║  │  ├─ 🔧 Microwave 200°C/20min for rapid N-CDs                        │   ║
║  │  └─ 🔧 Solvothermal EtOH 180°C/12h for red-emissive CDs             │   ║
║  │                                                                     │   ║
║  │  Characterization Strategies ─ 4 stored                              │   ║
║  │  ├─ 📊 QY calculation (quinine sulfate, λ_ex=360nm)                 │   ║
║  │  ├─ 📊 TEM size analysis (ImageJ macro, threshold=auto)              │   ║
║  │  └─ 📊 FTIR peak assignment (automated matching)                     │   ║
║  │                                                                     │   ║
║  │  Application Strategies ─ 3 stored                                   │   ║
║  │  ├─ 🎯 Hg²⁺ sensing (Stern-Volmer, 15-ion interference)             │   ║
║  │  ├─ 🎯 MTT cytotoxicity (HeLa, 0-500 μg/mL, 24h)                    │   ║
║  │  └─ 🎯 MB dye degradation (UV-Vis kinetics, scavenger analysis)     │   ║
║  └─────────────────────────────────────────────────────────────────────┘   ║
║                                                                          ║
║  [/view <id>] Inspect Item  [/search] Query Memory  [/clear] Reset       ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## CLI Commands Reference

| Command | Description |
|---|---|
| `/new <goal>` | Start new CD research goal |
| `/proposal` | View current CD research proposal |
| `/report` | View latest execution report |
| `/stages` | Show 5-stage progress |
| `/memory` | Inspect M_I^CD and M_E^CD |
| `/skills` | List installed CD skills |
| `/install-skill <src>` | Install a CD skill |
| `/literature <query>` | Manual literature search |
| `/export <format>` | Export report (yaml/json/pdf) |
| `/config` | Open configuration |
| `/logs` | View full execution logs |
| `/stop` | Abort current experiment |
| `/help` | Show all commands |

## Color Scheme

| Color | Meaning | Usage |
|---|---|---|
| 🔵 Blue | Info / System | Borders, stage labels, prompts |
| 🟢 Green | Success | Passed stages, high QY, LOD met |
| 🟡 Yellow | In Progress / Warning | Running experiments, implementation failures |
| 🔴 Red | Error / Dead End | Failed syntheses, fundamental failures |
| 🟣 Magenta | Memory / Evolution | Memory updates, IDE/IVE/ESE output |
| ⚪ White | Data / Values | Numeric results, metrics |
