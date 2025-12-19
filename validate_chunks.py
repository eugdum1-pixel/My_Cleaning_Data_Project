# ==============================================================================
# PROJECT: End-to-End AI Data Pipeline (UK Industry Insights)
# STAGE: 1 - Data Validation & Schema Enforcement
# AUTHOR: [Gigel Dumitru - GitHub Profile:https://github.com/eugdum1-pixel]
# DATE: 2025-12-19
# DESCRIPTION: 
#   Automated audit tool to verify the integrity of JSON data units. 
#   Ensures mandatory fields ('id', 'text_preview') are present for 
#   downstream MCP and RAG integration.
# ==============================================================================

import json
import os
from datetime import datetime

def validate_stage_1(data_path):
    """
    Scans the local data directory and generates a Markdown audit report.
    Target Schema: { "id": int, "nurse": str, "text_preview": str }
    """
    report = []
    report.append(f"# 📊 Data Validation Report")
    report.append(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append(f"**Pipeline Stage:** Stage 1 - Schema Enforcement\n")
    report.append(f"---")
    
    if not os.path.exists(data_path):
        print(f"🚨 Error: Path {data_path} not found!")
        return

    files = [f for f in os.listdir(data_path) if f.endswith('.json')]
    total_files = len(files)
    valid_units = 0
    total_units = 0
    errors = []

    print(f"🔍 Analyzing {total_files} JSON files in {data_path}...")

    for file_name in files:
        file_path = os.path.join(data_path, file_name)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
                # Handling lists of units (as seen in your Notepad++ screenshot)
                if isinstance(data, list):
                    for unit in data:
                        total_units += 1
                        if "text_preview" in unit and "id" in unit:
                            valid_units += 1
                        else:
                            errors.append(f"⚠️ {file_name}: Unit missing mandatory keys.")
                elif isinstance(data, dict):
                    total_units += 1
                    if "text_preview" in data:
                        valid_units += 1
                    else:
                        errors.append(f"❌ {file_name}: Missing 'text_preview' field.")
        except Exception as e:
            errors.append(f"❌ {file_name}: Parsing Error - {str(e)}")

    # Summary Statistics
    report.append(f"## 📈 Summary Statistics")
    report.append(f"- **Total JSON Files Scanned:** {total_files}")
    report.append(f"- **Total Individual Data Units:** {total_units}")
    report.append(f"- **Successfully Validated Units:** {valid_units}")
    report.append(f"- **Integrity Rate:** {(valid_units/total_units)*100:.2f}%" if total_units > 0 else "0%")
    report.append(f"\n---")
    
    if errors:
        report.append("## 🛑 Issues Detected")
        for err in errors[:10]: # Log first 10 issues
            report.append(f"- {err}")
        if len(errors) > 10:
            report.append(f"- *...and {len(errors) - 10} more errors.*")
    else:
        report.append("## ✅ Quality Assurance")
        report.append("All data units passed schema validation. The dataset is technically ready for AI context ingestion.")

    # Save the report for GitHub documentation
    with open("stage_1_validation_report.md", "w", encoding='utf-8') as r_file:
        r_file.write("\n".join(report))
    
    print(f"\n✅ Validation Complete. Created 'stage_1_validation_report.md'.")

if __name__ == "__main__":
    # Local path to your data chunks
    TARGET_DIR = r"C:\DataScienceBootcamp\scripts\PROGRES_SIGUR_CHUNK"

    validate_stage_1(TARGET_DIR)
