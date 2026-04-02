#!/usr/bin/env python
"""
Cleya.ai Marketing Crew — Entry Point
======================================

Run the complete marketing crew pipeline:
  $ crewai run

Or directly:
  $ python src/cleya_marketing_crew/main.py

Environment variables required in .env:
  - OPENAI_API_KEY (or other LLM provider key)
  - SERPER_API_KEY (for web search tools)

Customize the inputs below for different runs:
  - target_segment: "founders", "investors", "talent", or "all"
  - time_period: "this week", "Q2 2026", "April 2026", etc.
"""

import sys
import os
from pathlib import Path
from cleya_marketing_crew.crew import CleyaMarketingCrew


def run():
    """
    Run the Cleya.ai Marketing Crew.
    
    Inputs are passed to all agent prompts via {variable} interpolation
    in the YAML task descriptions.
    """
    # Create output directory
    Path("output").mkdir(exist_ok=True)

    inputs = {
        # ── Target Configuration ─────────────────────────────────────
        "target_segment": "all professionals — founders, investors, VCs, operators, engineers, designers, marketers, recruiters, and talent across India's startup and business ecosystem",
        
        # ── Time Period ──────────────────────────────────────────────
        "time_period": "April 2026",
        
        # ── Product Context (available to all agents) ────────────────
        "product_name": "Cleya.ai",
        "product_tagline": "AI Superconnector for Professionals in India",
        "product_url": "https://cleya.ai",
        "social_handle": "@joincleya",
        "product_description": (
            "Cleya.ai is an AI-powered professional networking platform that matches "
            "all kinds of professionals across India — founders, investors, operators, "
            "engineers, designers, marketers, recruiters, freelancers, and anyone building "
            "or scaling companies. Members describe their goals in plain language, and "
            "Cleya's AI finds matches based on skills, intent, industry, role fit, and "
            "professional context — delivering warm introductions with context. "
            "No cold emails. No awkward LinkedIn DMs."
        ),
        "key_differentiators": (
            "1) AI matching with 90%+ accuracy scores across all professional roles, "
            "2) Warm intros with context (not cold outreach), "
            "3) Members-only verified community, "
            "4) Covers ALL professionals — not just founders and investors, "
            "5) India-focused with Tier-2 city coverage, "
            "6) Works for hiring, partnerships, mentorship, co-founding, and deal flow"
        ),
    }

    print("\n" + "=" * 60)
    print("🚀 CLEYA.AI MARKETING CREW — LAUNCHING")
    print("=" * 60)
    print(f"  Target:  {inputs['target_segment']}")
    print(f"  Period:  {inputs['time_period']}")
    print(f"  Output:  ./output/")
    print("=" * 60 + "\n")

    # Kick off the crew
    result = CleyaMarketingCrew().crew().kickoff(inputs=inputs)

    print("\n" + "=" * 60)
    print("✅ CREW EXECUTION COMPLETE")
    print("=" * 60)
    print("\nOutputs saved to ./output/:")
    print("  01_ecosystem_intelligence.md")
    print("  02_growth_strategy.md")
    print("  03_viral_content_calendar.md")
    print("  04_community_partnerships.md")
    print("  05_product_led_growth.md")
    print("  crew_execution.log")
    print("=" * 60)

    return result


def train():
    """
    Train the crew for a given number of iterations.
    Usage: crewai train -n <iterations>
    """
    inputs = {
        "target_segment": "all professionals across India's ecosystem",
        "time_period": "April 2026",
    }

    try:
        n_iterations = int(sys.argv[1]) if len(sys.argv) > 1 else 3
        CleyaMarketingCrew().crew().train(
            n_iterations=n_iterations,
            filename="training_data.pkl",
            inputs=inputs,
        )
    except Exception as e:
        raise Exception(f"Training error: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    Usage: crewai replay -t <task_id>
    """
    try:
        task_id = sys.argv[1] if len(sys.argv) > 1 else None
        CleyaMarketingCrew().crew().replay(task_id=task_id)
    except Exception as e:
        raise Exception(f"Replay error: {e}")


def test():
    """
    Test the crew with evaluation metrics.
    Usage: crewai test -n <iterations>
    """
    inputs = {
        "target_segment": "all professionals across India's ecosystem",
        "time_period": "April 2026",
    }

    try:
        n_iterations = int(sys.argv[1]) if len(sys.argv) > 1 else 2
        CleyaMarketingCrew().crew().test(
            n_iterations=n_iterations,
            openai_model_name="gpt-4o",
            inputs=inputs,
        )
    except Exception as e:
        raise Exception(f"Test error: {e}")


if __name__ == "__main__":
    run()
