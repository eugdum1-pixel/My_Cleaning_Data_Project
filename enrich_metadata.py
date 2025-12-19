# ==============================================================================
# PROJECT: End-to-End AI Data Pipeline (UK Industry Insights)
# STAGE: 2 - Metadata Enrichment & Categorization (ABC Strategy)
# AUTHOR: [Gigel Dumitru - GitHub Profile: https://github.com/eugdum1-pixel]
# DATE: 2025-12-19
# DESCRIPTION: 
#   Scans 'text_preview' for industry-specific keywords and assigns 
#   each unit to Zone A (Public), Zone B (Business), or Zone C (Labor).
# ==============================================================================

import json
import os

# Define our Keyword Strategy for the Drawers (Sertare)
ZONES = {
    "A": ["policy", "regulation", "government", "safety", "nhs", "ethical", "public", "standard"],
    "B": ["investment", "market", "startups", "revenue", "sector", "industry", "business", "economy"],
    "C": ["jobs", "skills", "automation", "workforce", "education", "training", "employment"]
}

def enrich_data(input_path, output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    files = [f for f in os.listdir(input_path) if f.endswith('.json')]
    print(f"🛠️ Starting Enrichment for {len(files)} files...")

    for file_name in files:
        with open(os.path.join(input_path, file_name), 'r', encoding='utf-8') as f:
            data = json.load(f)

        enriched_data = []
        for unit in data:
            text = unit.get("text_preview", "").lower()
            assigned_zone = "Uncategorized"

            # Simple Keyword Matching Logic
            for zone, keywords in ZONES.items():
                if any(kw in text for kw in keywords):
                    assigned_zone = zone
                    break # Assign to the first matching zone
            
            unit["metadata"] = {"zone": assigned_zone}
            enriched_data.append(unit)

        # Save to the new "Enriched" folder
        with open(os.path.join(output_path, file_name), 'w', encoding='utf-8') as f:
            json.dump(enriched_data, f, indent=4)

    print(f"✅ Enrichment Complete! Files saved in: {output_path}")

if __name__ == "__main__":
    SOURCE = r"C:\DataScienceBootcamp\scripts\PROGRES_SIGUR_CHUNK"
    DESTINATION = r"C:\DataScienceBootcamp\scripts\PROGRES_SIGUR_ENRICHED"
    enrich_data(SOURCE, DESTINATION)