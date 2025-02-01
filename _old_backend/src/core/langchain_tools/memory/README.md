### **File: README.md**

---

# **LangChain Tools: Memory Module**

## **Overview**
The `memory` module within the LangChain tools package implements memory systems for AI agents to store, manage, and retrieve contextual data. These tools are essential for enabling agents to perform stateful interactions, remember past interactions, and build meaningful context over time.

---

## **Memory Implementations**

### **1. Document Context Memory**
- **File**: `document_context_memory.py`
- **Purpose**: 
  - Manages contextual information extracted from documents.
  - Stores and retrieves document-specific data for task-specific interactions.
- **Features**:
  - Add, retrieve, delete, and list document contexts.
  - Converts stored contexts into LangChain-compatible prompts.
- **Use Cases**:
  - Academic research retrieval.
  - Customer support document referencing.

### **2. Long-Term Memory**
- **File**: `long_term_memory.py`
- **Purpose**: 
  - Provides a persistent memory store that spans across agent sessions.
  - Designed to store historical knowledge and enable better decision-making.
- **Features**:
  - CRUD operations for memory entries.
  - Search stored data using keywords.
  - JSON-based persistent storage.
- **Use Cases**:
  - Retaining knowledge over time for an evolving AI system.
  - Historical analysis and reporting.

### **3. Vector Memory**
- **File**: `vector_memory.py`
- **Purpose**: 
  - Uses vector embeddings for semantic search and contextual retrieval.
  - Leverages FAISS for scalable and efficient similarity-based memory operations.
- **Features**:
  - Add, search, delete, and list vectorized memory entries.
  - Semantic similarity search with top-k results.
  - Persistent FAISS index storage.
- **Use Cases**:
  - Knowledge graph integration.
  - Semantic document and interaction retrieval.

---

## **How It Works**

Each memory implementation leverages different techniques:
1. **Document Context Memory**: Focuses on text and metadata organization for contextual relevance.
2. **Long-Term Memory**: Uses JSON storage to ensure data persists across sessions.
3. **Vector Memory**: Utilizes embeddings and vector similarity to perform sophisticated semantic search.

The modular design allows seamless integration into LangChain workflows, enabling agents to incorporate memory as part of their stateful operations.

---

## **Getting Started**

### **Setup**
1. Ensure the necessary dependencies are installed:
   ```bash
   pip install langchain faiss-cpu openai
   ```
2. Review and configure paths for:
   - Persistent JSON storage (`long_term_memory.py`).
   - FAISS index paths (`vector_memory.py`).

### **Usage Example**
```python
from memory.vector_memory import VectorMemory

# Initialize vector memory
vector_memory = VectorMemory()

# Add data
vector_memory.add_memory("AI will shape the future.", {"source": "Tech Blog"})

# Search for data
results = vector_memory.search_memory("Future of AI")
for text, score, metadata in results:
    print(f"Text: {text}, Score: {score}, Metadata: {metadata}")
```

---

## **Customization**
- **Extend Functionality**:
  - Add new memory storage backends like databases (SQL, NoSQL).
  - Integrate additional embedding models or APIs.
- **Optimize Search**:
  - Customize vector similarity thresholds for specific applications.

---

## **Contributing**
This module is part of the larger Automated Bureaucracy project, developed with the assistance of AI to optimize and enhance agent intelligence. Contributions are welcomed to expand functionality or address edge cases.

For issues or contributions, visit the main [GitHub repository](https://github.com/automatedbureaucracy).

---