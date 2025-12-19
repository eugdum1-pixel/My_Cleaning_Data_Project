# ==============================================================================
# PROJECT: End-to-End AI Data Pipeline (UK Industry Insights)
# STAGE: 4 - Semantic Query Engine (RAG Core) with Heuristic Filtering
# DESCRIPTION: 
#   Searches the neural vector space to find relevant data units.
#   Includes a noise filter to bypass technical boilerplate (Copyrights/Licenses)
#   ensuring high-quality retrieval of industry-specific intelligence.
# ==============================================================================

import json
import os
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def run_query(query_text, top_k=3):
    """
    Finds the most similar data units, filtering out technical boilerplate.
    """
    # 1. Load the Model and the Vector Store
    print("🧠 Initializing Neural Engine...")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    if not os.path.exists('semantic_vectors.npz'):
        print("🚨 Error: 'semantic_vectors.npz' not found. Please run Stage 3 first.")
        return

    data_store = np.load('semantic_vectors.npz')
    embeddings = data_store['embeddings']
    ids = data_store['ids']

    # 2. Encode the user's question into the same 384-D space
    query_vector = model.encode([query_text])

    # 3. Calculate Cosine Similarity
    similarities = cosine_similarity(query_vector, embeddings).flatten()
    
    # 4. Expand search range to 20 candidates to allow for filtering noise
    candidate_indices = similarities.argsort()[-20:][::-1]

    print(f"\n🔍 REFINED SEMANTIC MATCHES FOR: '{query_text}'")
    print("="*60)

    # 5. Connect back to Enriched Data
    enriched_path = r"C:\DataScienceBootcamp\scripts\PROGRES_SIGUR_ENRICHED"
    
    if not os.path.exists(enriched_path):
        print(f"🚨 Error: Path {enriched_path} not found.")
        return

    files = [f for f in os.listdir(enriched_path) if f.endswith('.json')]
    
    found_count = 0
    for idx in candidate_indices:
        if found_count >= top_k:
            break
            
        target_id = ids[idx]
        score = similarities[idx]
        
        # Search JSON files for the matching unit
        match_found = False
        for file_name in files:
            if match_found: break
            
            with open(os.path.join(enriched_path, file_name), 'r', encoding='utf-8') as f:
                units = json.load(f)
                for unit in units:
                    if str(unit.get("id")) == str(target_id):
                        text = unit.get('text_preview', '')
                        
                        # --- THE NOISE FILTER ---
                        # Skips units containing standard code boilerplate
                        noise_keywords = ["Copyright", "Licensed under", "http://", "NVIDIA", "Apache", "coding=utf-8"]
                        if any(kw in text for kw in noise_keywords):
                            continue 
                        
                        # --- DISPLAY RESULTS ---
                        zone = unit.get("metadata", {}).get("zone", "N/A")
                        print(f"📍 [ZONE {zone}] (Match Score: {score:.4f})")
                        print(f"📄 Content: {text[:450]}...")
                        print("-" * 40)
                        
                        found_count += 1
                        match_found = True
                        break

    if found_count == 0:
        print("⚠️ No high-quality matches found after filtering. Try a different query.")

if __name__ == "__main__":
    # Ensure the script is clean and interactive
    print("--- UK Industry Insights: Semantic Query Engine ---")
    user_input = input("❓ What would you like to ask the dataset? ")
    
    if user_input.strip():
        run_query(user_input)
    else:
        print("❌ Please enter a valid question.")