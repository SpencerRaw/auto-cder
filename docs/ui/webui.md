# Auto-CDer WebUI Interface Design

## Design Principles
- Modern, clean dashboard inspired by EvoScientist's WebUI (Next.js/React)
- Real-time streaming panels with collapsible sections
- Dark mode by default (lab-friendly), toggle to light mode
- Responsive layout: 3-column on desktop, stacked on tablet

---

## Page 1: Dashboard — Goal Input

```
┌──────────────────────────────────────────────────────────────────────────────┐
│  auto-cder                              [Skills] [Memory] [Settings] [👤]   │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─ New CD Research Goal ─────────────────────────────────────────────────┐ │
│  │                                                                          │ │
│  │  What carbon dots do you want to create?                                 │ │
│  │                                                                          │ │
│  │  ┌──────────────────────────────────────────────────────────────────┐   │ │
│  │  │  Synthesize high-QY N,S co-doped carbon dots from citric acid    │   │ │
│  │  │  and thiourea for selective Hg²⁺ sensing in water samples...     │   │ │
│  │  └──────────────────────────────────────────────────────────────────┘   │ │
│  │                                                                          │ │
│  │  ── Quick Settings ─────────────────────────────────────────────────    │ │
│  │  ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────────────┐   │ │
│  │  │ Precursor Type   │ │ Target Property │ │ Application Domain      │   │ │
│  │  │ ○ Citric Acid    │ │ ○ High QY       │ │ ○ Metal Ion Sensing     │   │ │
│  │  │ ○ PDA-based      │ │ ○ Red Emission  │ │ ○ Bioimaging            │   │ │
│  │  │ ○ Biomass        │ │ ○ Upconversion  │ │ ○ Photocatalysis        │   │ │
│  │  │ ● Custom Mix     │ │ ○ NIR Emission  │ │ ● Other: Hg²⁺ sensing   │   │ │
│  │  └─────────────────┘ └─────────────────┘ └─────────────────────────┘   │ │
│  │                                                                          │ │
│  │  ┌──────────────────────────────────────────────────────────────────┐   │ │
│  │  │  ⚡ Auto-CDer will:                                               │   │ │
│  │  │  1. Search 70+ CD papers for relevant synthesis protocols        │   │ │
│  │  │  2. Generate 21 candidate ideas via Idea Tree Search             │   │ │
│  │  │  3. Rank by Synthesis Novelty, Feasibility, Relevance, Clarity   │   │ │
│  │  │  4. Execute 5-stage CD experiment pipeline                       │   │ │
│  │  │  5. Learn from results → improve future proposals                │   │ │
│  │  └──────────────────────────────────────────────────────────────────┘   │ │
│  │                                                                          │ │
│  │  [▶ Start Research]  [💾 Save Draft]                                    │ │
│  └──────────────────────────────────────────────────────────────────────────┘ │
│                                                                              │
│  ┌─ Recent Research ──────────────────────────────────────────────────────┐ │
│  │  #   Goal                                     Status      QY     Date   │ │
│  │  1   N,S-CDs from CA+thiourea → Hg²⁺         ✅ Complete  52.3%  6/25  │ │
│  │  2   Red-CDs from o-PD → mitochondrial img    ✅ Complete  38.1%  6/24  │ │
│  │  3   Biomass CDs from orange peel → MB deg    ⚠️ Partial   22.7%  6/23  │ │
│  │  4   N-CDs from CA+urea → Cu²⁺ sensing        ✅ Complete  45.2%  6/22  │ │
│  └─────────────────────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Page 2: Idea Generation — Tournament View

```
┌──────────────────────────────────────────────────────────────────────────────┐
│  auto-cder  >  N,S-CDs from CA+Thiourea for Hg²⁺ Sensing                     │
│  [Dashboard] [📝 Ideas] [🔬 Experiments] [📊 Report] [🧠 Memory]             │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─ Literature Grounding ──────────────────────────────┬──────────────────┐ │
│  │  46 papers retrieved                                 │  Gap Analysis    │ │
│  │  ┌─────────────────────────────────────────────┐    │                  │ │
│  │  │ ████████████ CA+thiourea CDs synthesis (23) │    │ ⚠️ No papers     │ │
│  │  │ ████████ N,S co-doped CDs sensing (15)      │    │    on CA+thio     │ │
│  │  │ ████ CD-based Hg²⁺ detection (8)            │    │    for Hg²⁺!     │ │
│  │  │ ▌ CA+thiourea+Hg²⁺ (0) ← NOVEL!            │    │                  │ │
│  │  └─────────────────────────────────────────────┘    │ ✅ Novelty high  │ │
│  └────────────────────────────────────────────────────┴──────────────────┘ │
│                                                                              │
│  ┌─ Idea Tree Search — 21 Candidates ─────────────────────────────────────┐ │
│  │                                                                          │ │
│  │  ┌─ 🥇 #14 ─────────────────────────┬────────────────────────────────┐  │ │
│  │  │  Elo 1582  ▲142 from baseline    │  CA:Thiourea = 1:2              │  │ │
│  │  │                                  │  Hydrothermal 180°C, 8h, pH 5  │  │ │
│  │  │  Novelty  ████████████ 92%       │  Expected QY: 45-55%           │  │ │
│  │  │  Feasible ████████████ 88%       │  Expected λ_em: 475-490 nm     │  │ │
│  │  │  Relevant ████████████ 95%       │  LOD est: <50 nM               │  │ │
│  │  │  Clarity  ████████████ 90%       │  Dialysis 1kDa MWCO            │  │ │
│  │  │              [Extend to Proposal]│                                 │  │ │
│  │  └─────────────────────────────────┴─────────────────────────────────┘  │ │
│  │                                                                          │ │
│  │  ┌─ 🥈 #7 ─── ─────────────────────┬────────────────────────────────┐  │ │
│  │  │  Elo 1541                        │  CA:Thiourea = 1:1.5            │  │ │
│  │  │  Novelty 85% | Feasible 92%      │  Microwave 200°C, 20min         │  │ │
│  │  └──────────────────────────────────┴────────────────────────────────┘  │ │
│  │                                                                          │ │
│  │  ┌─ 🥉 #3 ─────────────────────────┬────────────────────────────────┐  │ │
│  │  │  Elo 1523                        │  CA:Thiourea = 2:1              │  │ │
│  │  │  Novelty 78% | Feasible 90%      │  Solvothermal EtOH, 180°C       │  │ │
│  │  └──────────────────────────────────┴────────────────────────────────┘  │ │
│  │                                                                          │ │
│  │                   [Show All 21 Ideas]  [Re-run Tournament]               │ │
│  └──────────────────────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Page 3: Experiment Execution — Live Dashboard

```
┌──────────────────────────────────────────────────────────────────────────────┐
│  auto-cder  >  N,S-CDs from CA+Thiourea  >  [🔬 Experiments]                 │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─ 5-Stage Progress ─────────────────────────────────────────────────────┐ │
│  │                                                                          │ │
│  │  Stage 1            Stage 2         Stage 3         Stage 4   Stage 5   │ │
│  │  Synthesis          Purification    Characterize    App.      Reprod.   │ │
│  │  ┌──────┐          ┌──────┐        ┌──────┐        ┌──────┐  ┌──────┐  │ │
│  │  │  ✅  │──────────│  ✅  │────────│  ⏳  │────────│  ○  │──│  ○  │  │ │
│  │  │ 5/20 │          │ 3/12 │        │ 2/12 │        │ 0/18 │  │ 0/10 │  │ │
│  │  └──────┘          └──────┘        └──────┘        └──────┘  └──────┘  │ │
│  │  Passed on          Passed on       Running...       Queued    Queued   │ │
│  │  Attempt #5         Attempt #3      ────────         ──────    ──────   │ │
│  └──────────────────────────────────────────────────────────────────────────┘ │
│                                                                              │
│  ┌─ Stage 3: Characterization Pipeline ────────────────────────────────────┐ │
│  │                                                                          │ │
│  │  ┌─ Optical ───────────────────┐  ┌─ Structural ─────────────────────┐  │ │
│  │  │                             │  │                                   │  │ │
│  │  │  UV-Vis Spectrum            │  │  TEM Image Analysis               │  │ │
│  │  │  ┌─────────────────────┐   │  │  ┌───────────────────────────┐    │  │ │
│  │  │  │  .-'''-._           │   │  │  │   ●  ●    ●               │    │  │ │
│  │  │  │ /         \         │   │  │  │     ● ●  ● ●  ●           │    │  │ │
│  │  │  │/   peak    \        │   │  │  │  ●  ●   ●   ●   ●         │    │  │ │
│  │  │  │   @ 340nm   \       │   │  │  │    ●  ● ●  ●  ● ●         │    │  │ │
│  │  │  │              '--    │   │  │  │  ●   ●   ●    ●           │    │  │ │
│  │  │  └─────────────────────┘   │  │  └───────────────────────────┘    │  │ │
│  │  │  π-π* @ 240nm ✓           │  │  Mean: 4.2 ± 0.8 nm               │  │ │
│  │  │  n-π* @ 340nm ✓           │  │  N = 120 particles                │  │ │
│  │  │                            │  │  Lattice: 0.34 nm (002) ✓         │  │ │
│  │  └────────────────────────────┘  └───────────────────────────────────┘  │ │
│  │                                                                          │ │
│  │  ┌─ PL Spectroscopy ─────────┐  ┌─ FTIR ────────────────────────────┐  │ │
│  │  │  λ_ex = 360 nm            │  │  3400 cm⁻¹ -OH ✓                  │  │ │
│  │  │  λ_em = 475 nm ✓          │  │  3200 cm⁻¹ -NH₂ ✓                 │  │ │
│  │  │  QY = 52.3% ± 2.1% ✓     │  │  1700 cm⁻¹ C=O ✓                  │  │ │
│  │  │  Lifetime τ = 8.2 ns     │  │  1100 cm⁻¹ C=S ✓                   │  │ │
│  │  │  FWHM = 82 nm            │  │  1400 cm⁻¹ C-N ✓                   │  │ │
│  │  └────────────────────────────┘  └───────────────────────────────────┘  │ │
│  │                                                                          │ │
│  │  [View Raw Data]  [Download Spectra]  [Reprocess]                        │ │
│  └──────────────────────────────────────────────────────────────────────────┘ │
│                                                                              │
│  ┌─ Live Console ──────────────────────────────────────────────────────────┐ │
│  │  [14:32:01] Stage 3, Attempt 2: Starting PL measurement...              │ │
│  │  [14:32:15] λ_em scan complete (350-700 nm), peak @ 475 nm              │ │
│  │  [14:32:30] QY measurement: I_sample/I_ref = 0.968, A=0.05              │ │
│  │  [14:32:31] QY = 0.54 × 0.968 × (0.05/0.05) × (1.33²/1.33²) = 52.3%   │ │
│  │  [14:32:31] ✅ QY > 40% threshold — PASSED                               │ │
│  └─────────────────────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Page 4: Final Report — Shareable Dashboard

```
┌──────────────────────────────────────────────────────────────────────────────┐
│  auto-cder  >  N,S-CDs from CA+Thiourea  >  [📊 Report]                      │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─ CD Experiment Report — June 25, 2026 ──────────────────── [📥 Export] ┐ │
│  │                                                                          │ │
│  │  ┌──────────────────┬──────────────────┬──────────────────────────────┐ │ │
│  │  │  Synthesis ✅     │  Characterize ✅  │  Application ✅              │ │ │
│  │  │                  │                  │                              │ │ │
│  │  │   QY       52.3% │  Size   4.2 nm   │  LOD      18.5 nM           │ │ │
│  │  │   Yield    23.5% │  λ_em   475 nm   │  Range  0.05-50 μM          │ │ │
│  │  │   λ_em    475 nm │  XRD    Graphitic│  Selec.  Hg²⁺ >> others     │ │ │
│  │  │   UV       Blue  │  Charge -28.5 mV │  R²      0.996              │ │ │
│  │  └──────────────────┴──────────────────┴──────────────────────────────┘ │ │
│  │                                                                          │ │
│  │  ┌─ Key Plots ───────────────────────────────────────────────────────┐  │ │
│  │  │  [TEM] [XRD] [FTIR] [UV-Vis] [PL] [Stern-Volmer] [Selectivity]   │  │ │
│  │  │  ┌─────────────┐ ┌──────────────┐ ┌──────────────┐                │  │ │
│  │  │  │ TEM Image   │ │ PL Spectra   │ │ SV Plot      │                │  │ │
│  │  │  │   ● ●  ●    │ │    ┌─┐       │ │    /         │                │  │ │
│  │  │  │  ● ● ● ●    │ │   /   \      │ │   /          │                │  │ │
│  │  │  │ ●  ●  ● ●   │ │  /     \     │ │  /           │                │  │ │
│  │  │  └─────────────┘ │ └──────────────┘ │ └──────────────┘                │  │ │
│  │  │  Size: 4.2 nm    │ λ_ex/λ_em shown  │ K_SV = 4.2×10³ M⁻¹             │  │ │
│  │  └───────────────────────────────────────────────────────────────────┘  │ │
│  │                                                                          │ │
│  │  ┌─ Evolution Activity ───────────────────────────────────────────────┐ │ │
│  │  │  CD-IDE → M_I^CD: "CA+Thiourea N,S-CDs: high-QY blue emission     │ │ │
│  │  │                      with inherent Hg²⁺ selectivity"              │ │ │
│  │  │  CD-IVE → M_I^CD: ✅ SUCCESS — reinforced                         │ │ │
│  │  │  CD-ESE → M_E^CD: 5 strategies stored (synthesis, char, app...)   │ │ │
│  │  └───────────────────────────────────────────────────────────────────┘ │ │
│  └──────────────────────────────────────────────────────────────────────────┘ │
│                                                                              │
│  ┌─ Next Steps ────────────────────────────────────────────────────────────┐ │
│  │  [🧪 Test real water samples]  [📝 Generate manuscript]  [🔄 New Goal]  │ │
│  └──────────────────────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## WebUI Component Tree

```
App
├── Layout
│   ├── Header (logo, nav tabs, user menu)
│   ├── Sidebar (context-sensitive: stages, memory, skills)
│   └── Main Content Area
├── Pages
│   ├── Dashboard (goal input, recent research, quick stats)
│   ├── Ideas (literature results, tournament bracket, proposal view)
│   ├── Experiments (5-stage progress, live console, plots)
│   ├── Report (final metrics, plots, evolution summary, export)
│   └── Memory (M_I^CD browser, M_E^CD browser, search)
├── Components
│   ├── GoalInput (text area + structured dropdowns)
│   ├── StageProgress (5-step progress bar)
│   ├── EloTournament (bracket visualization)
│   ├── LiveConsole (streaming log viewer)
│   ├── PlotViewer (interactive spectra/charts)
│   ├── MemoryGraph (knowledge graph visualization)
│   ├── SkillManager (install/uninstall/list)
│   └── ExportPanel (YAML/JSON/PDF export)
└── State
    ├── GoalContext (current G^CD, P^CD, W^CD)
    ├── ExecutionState (5-stage progress, live logs)
    └── MemoryState (M_I^CD, M_E^CD cache)
```

## Tech Stack

| Layer | Choice |
|---|---|
| Framework | Next.js 14 (App Router) |
| UI Library | Tailwind CSS + shadcn/ui |
| Charts | Recharts / D3.js |
| Streaming | Server-Sent Events (SSE) |
| State | Zustand |
| Backend | FastAPI (Python) → shared with CLI |
