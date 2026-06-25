# Auto-CDer Core Skills

This directory contains the minimal viable set of skills for autonomous carbon dot research. Each skill is self-contained but designed to compose with others.

## Skill Pipeline

```
User Goal G^CD
     │
     ▼
┌─────────────────┐
│  cd-literature   │  ← Literature grounding & gap analysis
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  cd-synthesis    │  ← Hypothesis generation & protocol design
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│cd-characterization│ ← Optical, structural, surface chemistry
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  cd-application  │  ← Sensing, bioimaging, catalysis validation
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   cd-memory      │  ← Persistent learning (CD-IDE, CD-IVE, CD-ESE)
└─────────────────┘
         │
         └──────────────→ feeds back into cd-literature + cd-synthesis
```

## Skill Format

Each skill follows the EvoScientist skill convention:

```
skills/<skill-name>/
├── README.md       # Skill description, stages, output format, integration
├── skill.json      # Metadata manifest (name, version, dependencies, tier)
└── prompt.md       # LLM prompt template with domain knowledge
```

## Creating a New Skill

1. Create a directory: `skills/cd-<name>/`
2. Write `README.md` describing the skill, its stages, outputs, and integrations
3. Write `skill.json` with metadata (follow existing skills for format)
4. Write `prompt.md` with the LLM prompt template using `{{variable}}` placeholders

## Installing Skills

From the auto-cder CLI:
```
/install-skill auto-cder/skills@cd-synthesis
/install-skill auto-cder/skills@cd-characterization
/install-skill auto-cder/skills@cd-application
/install-skill auto-cder/skills@cd-memory
/install-skill auto-cder/skills@cd-literature
```

Or install all core skills:
```
/install-skill auto-cder/skills@core-bundle
```
