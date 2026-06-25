# Auto-CDer Mobile Interface Design

## Design Principles
- Mobile-first, thumb-friendly interaction
- Push notifications for long-running synthesis/characterization stages
- Simplified views: monitor experiments on-the-go, full control on desktop
- Dark theme (OLED-friendly for lab use), minimal battery drain
- React Native (cross-platform iOS + Android)

---

## Screen 1: Home — Quick Actions

```
┌────────────────────────┐
│  auto-cder             │
│                        │
│  ┌──────────────────┐  │
│  │  🔬 Active Run    │  │
│  │  N,S-CDs QY 52.3%│  │
│  │  Stage 3/5 ████░ │  │
│  │  [Tap to view]   │  │
│  └──────────────────┘  │
│                        │
│  ┌──────────────────┐  │
│  │  📝 New Goal      │  │
│  │  Start CD research│  │
│  └──────────────────┘  │
│                        │
│  ┌──────────────────┐  │
│  │  📊 Last Report   │  │
│  │  N,S-CDs → Hg²⁺  │  │
│  │  LOD: 18.5 nM     │  │
│  └──────────────────┘  │
│                        │
│  ┌──────────────────┐  │
│  │  🧠 Memory        │  │
│  │  5 directions     │  │
│  │  8 validations    │  │
│  └──────────────────┘  │
│                        │
│  ┌──────────────────┐  │
│  │  ⚙️ Settings      │  │
│  └──────────────────┘  │
│                        │
│  [Home] [🔬] [📝] [⚙️] │
└────────────────────────┘
```

---

## Screen 2: New Goal — Voice/Text Input

```
┌────────────────────────┐
│  ← New Goal            │
│                        │
│  What CD do you want   │
│  to create?            │
│                        │
│  ┌──────────────────┐  │
│  │                  │  │
│  │ Synthesize high- │  │
│  │ QY N,S co-doped  │  │
│  │ carbon dots from │  │
│  │ citric acid and  │  │
│  │ thiourea for Hg²⁺│  │
│  │ sensing          │  │
│  │                  │  │
│  └──────────────────┘  │
│                        │
│  ── OR ──              │
│                        │
│  ┌──────────────────┐  │
│  │  🎤 Voice Input   │  │
│  └──────────────────┘  │
│                        │
│  ── Quick Templates ── │
│  ┌──────────────────┐  │
│  │ 💧 Metal Sensing  │  │
│  └──────────────────┘  │
│  ┌──────────────────┐  │
│  │ 🔬 Bioimaging     │  │
│  └──────────────────┘  │
│  ┌──────────────────┐  │
│  │ ☀️ Photocatalysis │  │
│  └──────────────────┘  │
│                        │
│  ┌──────────────────┐  │
│  │    ▶ Start        │  │
│  └──────────────────┘  │
└────────────────────────┘
```

---

## Screen 3: Live Experiment Monitor

```
┌────────────────────────┐
│  ← N,S-CDs Hg²⁺       │
│                        │
│  Stage Progress        │
│  ┌──────────────────┐  │
│  │ 1✅ 2✅ 3⏳ 4○ 5○  │  │
│  └──────────────────┘  │
│                        │
│  Current: Stage 3      │
│  Characterization      │
│  ┌──────────────────┐  │
│  │                   │  │
│  │  PL Spectrum      │  │
│  │  ┌─┐             │  │
│  │  │ │  /\         │  │
│  │  │ │ /  \        │  │
│  │  │ │/    \       │  │
│  │  │ └──────┘      │  │
│  │  λ_em: 475 nm    │  │
│  │                   │  │
│  │  QY: 52.3% ✅     │  │
│  └──────────────────┘  │
│                        │
│  Live Metrics          │
│  ┌──────────────────┐  │
│  │ QY      52.3% ▲  │  │
│  │ Size    4.2 nm   │  │
│  │ λ_em    475 nm   │  │
│  │ Attempt    2/12  │  │
│  └──────────────────┘  │
│                        │
│  Recent Log            │
│  ┌──────────────────┐  │
│  │ 14:32 QY passed  │  │
│  │ 14:31 PL done    │  │
│  │ 14:28 UV done    │  │
│  │ 14:25 TEM done   │  │
│  └──────────────────┘  │
│                        │
│  [⏸ Pause] [⏹ Stop]   │
└────────────────────────┘
```

---

## Screen 4: Push Notification

```
┌────────────────────────┐
│  auto-cder  now        │
│                        │
│  ┌──────────────────┐  │
│  │ 🔬 Experiment      │  │
│  │ Complete!          │  │
│  │                    │  │
│  │ N,S-CDs from       │  │
│  │ CA+Thiourea        │  │
│  │                    │  │
│  │ ✅ QY: 52.3%       │  │
│  │ ✅ LOD: 18.5 nM    │  │
│  │ ✅ Reproducible    │  │
│  │                    │  │
│  │ [View Report]      │  │
│  └──────────────────┘  │
│                        │
│  ┌──────────────────┐  │
│  │ ⚠️ Stage 4 Failed  │  │
│  │ Selectivity issue │  │
│  │ Fe³⁺ interference │  │
│  │                    │  │
│  │ [Diagnose]         │  │
│  └──────────────────┘  │
│                        │
└────────────────────────┘
```

---

## Screen 5: Memory Browser

```
┌────────────────────────┐
│  ← CD Memory           │
│                        │
│  🔍 Search memory...   │
│                        │
│  Ideation (M_I^CD)     │
│  ┌──────────────────┐  │
│  │ 📈 N,S-CDs high QY│  │
│  │ CA+thiourea 45-55%│  │
│  │ 3 successes       │  │
│  └──────────────────┘  │
│  ┌──────────────────┐  │
│  │ 📈 Red-emissive   │  │
│  │ o-PD λ_em 610-635│  │
│  │ 2 successes       │  │
│  └──────────────────┘  │
│  ┌──────────────────┐  │
│  │ ❌ Dead End       │  │
│  │ CA+thiourea no pH │  │
│  │ No CD formation  │  │
│  └──────────────────┘  │
│                        │
│  Experiment (M_E^CD)   │
│  ┌──────────────────┐  │
│  │ 🔧 Synthesis      │  │
│  │ 5 protocols       │  │
│  └──────────────────┘  │
│  ┌──────────────────┐  │
│  │ 📊 Characterize   │  │
│  │ 4 workflows       │  │
│  └──────────────────┘  │
│  ┌──────────────────┐  │
│  │ 🎯 Application    │  │
│  │ 3 templates       │  │
│  └──────────────────┘  │
└────────────────────────┘
```

---

## Mobile-Specific Features

### 1. Voice Input for Goals
- "Hey Auto-CDer, synthesize N-doped carbon dots from citric acid and urea for copper detection"
- Uses on-device speech-to-text (Siri/Google Assistant integration)

### 2. Push Notification Categories
| Category | Trigger | Action |
|---|---|---|
| Stage Complete | Each of 5 stages passes | Tap to view stage results |
| Experiment Done | Full 5-stage pipeline finishes | View full report |
| Failure Alert | Stage fails after max attempts | Diagnose or adjust parameters |
| Memory Update | CD-IDE/IVE/ESE writes to memory | Review new knowledge |
| QY Milestone | QY exceeds threshold (e.g., >50%) | Celebrate + share |

### 3. Apple Watch Companion
- Glance: Current experiment stage + QY
- Complication: Latest QY value on watch face
- Notification: Stage completion with haptic feedback

### 4. Lab Integration (Future)
- Camera: Photograph CD solution under UV lamp → auto-detect fluorescence color
- BLE: Connect to thermometer/pH meter for real-time synthesis monitoring
- NFC: Tag sample vials with experiment ID for tracking

## Mobile Tech Stack

| Layer | Choice |
|---|---|
| Framework | React Native (Expo) |
| Navigation | Expo Router |
| Charts | Victory Native |
| Notifications | Firebase Cloud Messaging |
| Voice | expo-speech-recognition |
| State | Zustand |
| Backend API | Same FastAPI server as CLI/WebUI |
