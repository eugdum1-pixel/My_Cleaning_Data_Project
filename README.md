<p align="center">
  <h1><b>🚀 Local RAG System: Architecting Intelligence from Raw Data</b></h1>
</p>
*📌 Project Overview*
This project demonstrates the end-to-end engineering required to transform 13,938 raw data units (derived from UK industry reports) into a functional RAG (Retrieval-Augmented Generation) system. By leveraging local Large Language Models (LLMs) such as Qwen and DeepSeek, this system allows for high-precision, context-aware querying of specialized datasets without relying on cloud infrastructure.

The objective is to bridge the gap between "Raw Data" and "Actionable Insights" through a structured 5-stage Data Engineering pipeline.

🛠 The 5-Stage Engineering Curriculum

Stage 1: Data Validation & Schema Enforcement
Raw data is often noisy and inconsistent. This stage focuses on Data Wrangling. We implement validation scripts to ensure every JSON chunk adheres to a strict schema, removing duplicates and correcting encoding errors.

Key Deliverable: A "Golden Dataset" ready for high-performance indexing.

Stage 2: Semantic Metadata Enrichment
To improve the "retrieval" part of RAG, data must be contextualized. We programmatically tag chunks with relevant metadata (e.g., Sector: Public/Business, Source: OECD/Gov.uk). This allows the AI to filter information geographically or by industry.

Key Deliverable: Enriched JSON objects with searchable attributes.

Stage 3: Vectorization & Neural Embeddings
Text cannot be mathematically queried in its raw form. Using local embedding models (e.g., sentence-transformers), we convert text into high-dimensional vectors. This enables Semantic Search—finding information based on meaning rather than just keywords.

Key Deliverable: A vectorized representation of the entire knowledge base.

Stage 4: Vector Database Implementation
Managing thousands of vectors requires a specialized database. We utilize ChromaDB (or FAISS) to store these embeddings locally. This stage involves optimizing index structures for sub-second retrieval speeds.

Key Deliverable: A persistent local Vector Store.

Stage 5: RAG Pipeline & LLM Integration
The final stage connects the Ollama inference engine to our Vector Store. We implement the "Retrieve-and-Generate" logic: the system fetches the most relevant data chunks and provides them to Qwen/DeepSeek as a grounded context for answering user queries.

Key Deliverable: A private, local AI agent with zero-hallucination tendencies.

Getting Started: Stage 1 Execution
The first practical step in this curriculum is verifying the integrity of the data chunks. Below is the technical approach for Data Validation.

Technical Task: validate_chunks.py
Before processing, we must verify that all 139 JSON files contain valid structures. This script performs:

JSON Syntax Check: Ensures files are not corrupted.

Schema Check: Confirms the presence of mandatory fields (e.g., text, id).

Encoding Verification: Ensures characters are UTF-8 compliant for UK-based reporting.

Implementation Guide
The following script is designed to be the first tool in the pipeline. It scans the local repository and generates a status report.

### Python

### validate_chunks.py
### Purpose: Stage 1 Data Integrity Check
import json
import os

def validate_data_directory(directory_path):
    print(f"--- Starting Validation for: {directory_path} ---")
    # Logic to iterate and validate JSON structure
    # [Code to be expanded in the next session]
    pass

if __name__ == "__main__":
    # Path to the data chunks
    target_dir = "./04_Tools_and_Assets/Diamonds_Shortcut"
    validate_data_directory(target_dir)
