# ==============================================================================
# PROJECT: End-to-End AI Data Pipeline
# TOOL: Stage 2 Enrichment Auditor
# DESCRIPTION: Quickly counts the units in each Zone to update the README.
# ==============================================================================
import json
import os

PATH = r"C:\DataScienceBootcamp\scripts\PROGRES_SIGUR_ENRICHED"
stats = {"A": 0, "B": 0, "C": 0, "Uncategorized": 0}

if os.path.exists(PATH):
    files = [f for f in os.listdir(PATH) if f.endswith('.json')]
    for file_name in files:
        with open(os.path.join(PATH, file_name), 'r', encoding='utf-8') as f:
            data = json.load(f)
            for unit in data:
                zone = unit.get("metadata", {}).get("zone", "Uncategorized")
                stats[zone] = stats.get(zone, 0) + 1

    print("\n📊 ENRICHMENT SUMMARY FOR GITHUB:")
    print(f"Zone A: {stats['A']} units")
    print(f"Zone B: {stats['B']} units")
    print(f"Zone C: {stats['C']} units")
    print(f"Uncategorized: {stats['Uncategorized']} units")
else:
    print("🚨 Path not found!")