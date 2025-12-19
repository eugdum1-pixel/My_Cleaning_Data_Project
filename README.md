<p align="center"> <h1>🚀 LOCAL AI ARCHITECTURE: MCP vs. RAG</h1> <h3>Architecting Intelligence from Raw Data Units</h3> </p>

> **Project Status:** Production-Ready | **Data Integrity:** 99.90% | **Architecture:** RAG-Enabled

### 📖 The Engineering Mission
This repository documents the end-to-end transformation of high-volume, unstructured industry data into a semantically-aware AI knowledge system. Processing a total of **13,952 data units** extracted from UK industry reports, this project bridges the gap between raw information and actionable intelligence.

### 🏗️ Pipeline Architecture at a Glance
The system is built on a four-stage industrial pipeline:
1. **Validation:** A rigorous "Gatekeeper" phase ensuring a **99.90% integrity rate** across 139 JSON data chunks.
2. **Enrichment:** A semantic taxonomy layer that categorizes data into **Public Policy**, **Business Impact**, and **Future of Work** sectors.
3. **Vectorization:** Deployment of a local **Sentence-Transformer** model to map 13,938 validated units into a 384-dimensional neural space.
4. **Retrieval (RAG):** A custom-built query engine that provides context-filtered, high-precision search results using Cosine Similarity.

*This project serves as a blueprint for local-first AI architectures, prioritizing data privacy, technical rigor, and semantic accuracy.*


📌 Project Overview
This project demonstrates the end-to-end engineering required to transform raw data into a professional AI knowledge system. Whether working with a custom dataset (in this project: 13,938 data units extracted from UK industry reports) or your own proprietary data, this repository provides the blueprint for two distinct integration paths:

MCP (Model Context Protocol): Direct tool-based connection.

RAG (Retrieval-Augmented Generation): Semantic vector-based memory.

The objective is to guide a Junior Data Analyst through the transition from raw, fragmented files to a production-ready AI context.

<p align="center"> <h2>🛠 THE 5-STAGE ENGINEERING PIPELINE</h2> </p>

<details> <summary><b>Click to expand the 5-Stage Curriculum details</b></summary>

Stage 1: Data Validation & Schema Enforcement
Raw data is often noisy. This stage focuses on Data Wrangling. We implement scripts to ensure every data unit adheres to a strict schema, removing duplicates and correcting encoding errors.

Stage 2: Semantic Metadata Enrichment
To improve retrieval accuracy, data must be contextualized. We programmatically tag chunks with relevant metadata (e.g., Sector, Source, or Region).

Stage 3: Vectorization & Neural Embeddings
Text is converted into high-dimensional vectors. This enables Semantic Search—finding information based on meaning rather than just keywords.

Stage 4: Vector Database Implementation
We utilize specialized databases like ChromaDB to store these embeddings locally, optimizing for sub-second retrieval speeds.

Stage 5: Inference & Pipeline Integration
The final stage connects the local inference engine (e.g., Ollama) to the data, allowing models like Qwen or DeepSeek to generate grounded answers.

</details>

<p align="center"> <h2>🔌 INTEGRATION PATHS: MCP vs. RAG</h2> </p>

🧩 Path A: The MCP Approach (Standardized Connection)
The Model Context Protocol (MCP) allows AI models to securely access local data and tools via a standardized server interface.

The Workflow:

Step 1: Initialize an MCP Server using Python or TypeScript.

Step 2: Expose your data directory as a Resource within the server.

Step 3: Define Tools — custom scripts that allow the AI to search or filter through your files (in this project: searching the 139 JSON files).

Step 4: The AI "calls" these tools dynamically to fetch only the necessary data.

🧠 Path B: The RAG Approach (Deep Memory)
Retrieval-Augmented Generation (RAG) involves pre-processing data into a "Vector Store" to allow the AI to "remember" vast amounts of information.

The Workflow:

Step 1: Data Ingestion (Chunking → Embedding → Storage).

Step 2: Vector Indexing (Creating a mathematical map of the data).

Step 3: Semantic Retrieval (Finding data based on the "intent" of a query).

Step 4: Context Injection (Feeding the retrieved data into the LLM prompt).

<p align="center"> <h2>📊 ARCHITECTURAL COMPARISON</h2> </p>

<details> <summary><b>Click to view: Why choose one over the other?</b></summary>

Feature	MCP (Model Context Protocol)	RAG (Retrieval-Augmented)
Data Access	Direct / Real-time	Pre-processed / Vectorized
Setup Complexity	Medium (Server-based)	High (Pipeline-based)
Primary Use Case	Interacting with local files/tools	Querying large knowledge bases
Flexibility	High (Executes local code)	Low (Queries static index)

</details>

<p align="center"> <h2>🚀 GETTING STARTED: STAGE 1 EXECUTION</h2> </p>

Regardless of the path chosen, Data Validation is the mandatory first step. We must ensure that the dataset (in this project: the 139 "Diamonds" JSON files) is technically sound.

Technical Task: validate_chunks.py
This script acts as the "Gatekeeper" for the pipeline, performing three critical checks:

JSON Syntax Verification: Prevents parsing errors during AI ingestion.

Schema Integrity: Confirms mandatory fields (e.g., text, id) are present.

UTF-8 Compliance: Ensures the text is readable by modern LLMs without encoding crashes.

Python

### validate_chunks.py - Pipeline Initialization
import json
import os

def validate_data_integrity(target_path):
    """Scan and validate JSON files for schema compliance."""
    # Implementation details follow in the Stage 1 module
    pass

if __name__ == "__main__":
    # Path to the data directory (Adjust to your local path)
    DATA_DIR = "./data/chunks" 
    validate_data_integrity(DATA_DIR)

## 🏷️ Stage 2: Semantic Taxonomy

To transform raw data into a structured knowledge base, we categorize each unit into one of three thematic "Zones":

| Zone | Category | Logic / Keywords | Goal |
| :--- | :--- | :--- | :--- |
| **Zone A** | **Public & Policy** | Government, NHS, Ethics, Safety | Regulatory guardrails. |
| **Zone B** | **Business Impact** | Investment, Market, Revenue, Startups | Economic growth. |
| **Zone C** | **Future of Work** | Skills, Automation, Jobs, Training | Labor evolution. |

### 📊 Latest Audit Statistics
- **Total Individual Data Units:** 13,952
- **Successfully Validated:** 13,938
- **Integrity Rate:** 99.90%
---

### 📂 Stage 2 Tooling
* **Enrichment Engine:** [`enrich_metadata.py`](./Project_Final/enrich_metadata.py)
* **Audit Utility:** [`audit_enrichment.py`](./Project_Final/audit_enrichment.py)



<p align="center">
  <h2>🧠 STAGE 3: NEURAL VECTORIZATION</h2>
</p>

To enable semantic search and AI context-awareness, the enriched dataset was transformed into dense vector embeddings. This allows the system to retrieve information based on **meaning** rather than just keyword matching.

### 🔬 Technical Specifications
| Attribute | Specification |
| :--- | :--- |
| **Model** | `all-MiniLM-L6-v2` (Sentence-Transformers) |
| **Dimensionality** | 384-dimensional dense vectors |
| **Total Vectors** | 13,938 |
| **Format** | Compressed NumPy Archive (.npz) |

### 📂 Stage 3 Assets
* **Vectorization Script:** [`create_embeddings.py`](./Project_Final/create_embeddings.py)
* **Neural Weight Store:** `semantic_vectors.npz` (Local binary storage)

> [!NOTE]
> This stage represents the "Neural Mapping" of the project. By converting text to numbers, we prepare the pipeline for integration into high-performance Vector Databases or direct MCP tool-calling.


### ✅ Final Validation & Results
The pipeline successfully processed **13,952 total units** with a **99.90% integrity rate**. 

**Example Query Success:**
When asked about *'Government safety standards for AI'*, the RAG engine successfully bypassed technical code noise to retrieve high-relevance policymaking evidence from **Zone A**, citing responsibilities from international bodies like the **OECD**.
