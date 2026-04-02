# 🚀 Cleya.ai Marketing Crew

A multi-agent AI system built on [crewAI](https://github.com/crewAIInc/crewAI) to run growth and viral marketing operations for [Cleya.ai](https://cleya.ai) — the AI Superconnector for Indian Startups.

## The Crew

| Agent | Role | What It Does |
|-------|------|-------------|
| **Market Intelligence Analyst** | Ecosystem Intel | Monitors Indian startup funding, competitors, trending conversations, and Tier-2 city signals |
| **Growth Strategist** | Head of Growth | Designs acquisition funnels, growth loops, channel strategy, and metrics frameworks |
| **Viral Content Architect** | Content & Social | Creates scroll-stopping content for LinkedIn/Twitter/X with viral mechanics |
| **Community Growth Hacker** | Partnerships | Builds accelerator partnerships, ambassador programs, and WhatsApp referral flows |
| **PLG Engineer** | Product Virality | Designs referral systems, match cards, waitlist gamification, and viral coefficient tracking |

## How It Works

```
Intelligence → Strategy → Content → Community → Product Mechanics
     ↓              ↓          ↓          ↓              ↓
  Market data    Funnels    Calendar   Partners      Referral
  Competitors    Loops      14 days    20 orgs       system
  Trends         KPIs       Hooks      Ambassadors   Viral k>1
```

The crew runs **sequentially** — each agent builds on the previous agent's output, creating a comprehensive marketing operations playbook.

## Quick Start

### 1. Clone & Install

```bash
git clone https://github.com/visheshkhurana/crewAI.git
cd crewAI

# Navigate to the marketing crew
cd cleya_marketing_crew

# Install dependencies
uv pip install -e .
```

### 2. Configure Environment

```bash
cp .env.example .env
# Edit .env with your API keys:
#   OPENAI_API_KEY=sk-...
#   SERPER_API_KEY=...
```

### 3. Run the Crew

```bash
# Using crewAI CLI
crewai run

# Or directly
python src/cleya_marketing_crew/main.py
```

### 4. Check Outputs

The crew generates 5 deliverables in `./output/`:

| File | Contents |
|------|----------|
| `01_ecosystem_intelligence.md` | Funding heatmap, competitor tracker, trending narratives, Tier-2 opportunities |
| `02_growth_strategy.md` | Full acquisition funnel, 3 growth loops, channel strategy, 4-week sprint plan |
| `03_viral_content_calendar.md` | 14-day content calendar, hooks, memes, founder "building in public" posts |
| `04_community_partnerships.md` | 20 partner profiles, city champions program, event strategy, WhatsApp flows |
| `05_product_led_growth.md` | Referral PRD, match card designs, waitlist gamification, viral coefficient model |

## Customizing

### Change Target Segment

Edit `main.py` → `inputs`:

```python
inputs = {
    "target_segment": "investors and VCs looking for deal flow",  # Change this
    "time_period": "Q2 2026",  # Change this
}
```

### Swap LLM Provider

CrewAI supports multiple providers. In your `.env`:

```bash
# Use Anthropic Claude
ANTHROPIC_API_KEY=sk-ant-...
```

Then in `crew.py`, specify the LLM per agent:

```python
@agent
def growth_strategist(self) -> Agent:
    return Agent(
        config=self.agents_config["growth_strategist"],
        llm="anthropic/claude-sonnet-4-20250514",
        tools=[serper_search, file_reader],
    )
```

### Add Custom Tools

Drop new tools in `tools/custom_tool.py`. Two templates included:
- **IndianStartupSearchTool** — augments queries with India ecosystem context
- **ViralScoreCalculatorTool** — calculates k-factor from referral data

## Architecture

```
cleya_marketing_crew/
├── pyproject.toml              # Project config & dependencies
├── .env.example                # Environment variable template
├── README.md                   # This file
└── src/
    └── cleya_marketing_crew/
        ├── __init__.py
        ├── main.py             # Entry point — configure inputs here
        ├── crew.py             # Crew assembly — agents, tasks, process
        ├── config/
        │   ├── agents.yaml     # Agent definitions (roles, goals, backstories)
        │   └── tasks.yaml      # Task definitions (descriptions, expected outputs)
        └── tools/
            ├── __init__.py
            └── custom_tool.py  # Custom tools (startup search, viral calculator)
```

## Training & Testing

```bash
# Train the crew (improves agent performance over iterations)
crewai train -n 5

# Test with evaluation metrics
crewai test -n 3

# Replay from a specific task
crewai replay -t <task_id>
```

## Built With

- [crewAI](https://github.com/crewAIInc/crewAI) — Multi-agent orchestration framework
- [crewai-tools](https://github.com/crewAIInc/crewAI/tree/main/lib/crewai-tools) — SerperDev, web scraper, file tools
- [Cleya.ai](https://cleya.ai) — AI Superconnector for Indian Startups

---

*Built by [Vishesh Khurana](https://github.com/visheshkhurana) for the Cleya.ai growth engine.*
