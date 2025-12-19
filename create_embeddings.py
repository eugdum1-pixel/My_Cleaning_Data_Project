# ==============================================================================
# PROJECT: End-to-End AI Data Pipeline (UK Industry Insights)
# STAGE: 3 - Neural Vectorization (Semantic Embeddings)
# DESCRIPTION: 
#   Transforms enriched text units into 384-dimensional dense vectors.
#   Uses the 'all-MiniLM-L6-v2' model for local inference.
#   These embeddings enable semantic search (RAG) and AI context matching.
# ==============================================================================

import json
import os
import numpy as np
from sentence_transformers import SentenceTransformer

def generate_embeddings(input_path, output_file):
    """
    Reads enriched JSON files and generates a vector representation for each unit.
    Outputs a compressed .npz file containing the vectors and unit IDs.
    """
    # Load a lightweight, high-performance local model
    print("🧠 Loading Neural Embedding Model...")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    files = [f for f in os.listdir(input_path) if f.endswith('.json')]
    all_text = []
    all_ids = []

    print(f"📂 Reading enriched data from: {input_path}")
    for file_name in files:
        with open(os.path.join(input_path, file_name), 'r', encoding='utf-8') as f:
            data = json.load(f)
            for unit in data:
                # We embed the 'text_preview' field which contains the core content
                if "text_preview" in unit:
                    all_text.append(unit["text_preview"])
                    all_ids.append(unit.get("id", "unknown"))

    print(f"⚡ Generating embeddings for {len(all_text)} units. This may take a moment...")
    # This is the 'Neural Work' - converting text to numbers
    embeddings = model.encode(all_text, show_progress_bar=True)

    # Save as a compressed numpy file for high-speed loading in Stage 4
    np.savez_compressed(output_file, embeddings=embeddings, ids=all_ids)
    print(f"✅ Stage 3 Complete! Vectors saved to: {output_file}")

if __name__ == "__main__":
    SOURCE_DIR = r"C:\DataScienceBootcamp\scripts\PROGRES_SIGUR_ENRICHED"
    OUTPUT_DATA = r"C:\DataScienceBootcamp\scripts\Project_Final\semantic_vectors.npz"
    generate_embeddings(SOURCE_DIR, OUTPUT_DATA)