# LangChain Tools: Chains

## Overview

This directory contains the implementation of various **LangChain-based chains** that facilitate modular workflows for the **Automated Bureaucracy** project. Chains in this context are designed to handle specific tasks by combining **retrieval**, **generation**, and **decision-making** capabilities using LangChain's robust framework.

Chains encapsulate multi-step workflows into reusable and extensible modules, enabling complex functionality to be implemented in a simple, composable manner.

---

## Contents

### **Files**
- **`approval_chain.py`**  
  Handles automated approval workflows based on predefined rules and criteria. This chain is particularly useful for automating tasks that require hierarchical approvals or decision-making.

- **`compliance_chain.py`**  
  Implements compliance checks by analyzing data or text input against a set of predefined rules. This chain ensures processes adhere to organizational or regulatory requirements.

- **`custom_chain.py`**  
  A customizable chain designed to handle user-defined workflows. This chain can be tailored to specific use cases, such as unique business logic or advanced interactions.

- **`decision_chain.py`**  
  Focuses on structured decision-making processes. It evaluates inputs, analyzes contexts, and generates actionable recommendations based on predefined workflows.

- **`rag_chain.py`**  
  Implements a **Retrieval-Augmented Generation (RAG)** workflow that retrieves relevant documents and generates context-aware responses. Ideal for use cases requiring both data retrieval and interpretation.

- **`retrieval_chain.py`**  
  A simplified chain for efficient document retrieval using a vector store like **FAISS**. This chain serves as the foundation for fetching relevant data for other workflows.

---

## Key Concepts

### **1. Modular Design**
Each chain is a standalone module that can be used independently or integrated into larger systems. This approach enables flexibility and scalability in the system architecture.

### **2. Reusability**
Chains leverage LangChain's `SequentialChain` and `RetrievalQA` to encapsulate workflows. They are designed to be reused across multiple agents or services.

### **3. Customization**
Chains such as `custom_chain.py` and `approval_chain.py` allow users to define task-specific logic and rules, ensuring adaptability to unique workflows.

### **4. Integration**
All chains integrate seamlessly with:
- **LLMs (OpenAI, HuggingFace, etc.)**
- **Vector Stores (FAISS, Pinecone)**
- **Custom Tools (e.g., Notepad, Internet Search)**

---

## Usage

### **How to Use a Chain**
1. **Initialize the Chain**  
   Each chain requires specific parameters such as API keys, model settings, or vector store paths. Refer to the corresponding file for detailed instructions.

   Example (for `rag_chain.py`):
   ```python
   from langchain_tools.chains.rag_chain import RAGChain

   rag_chain = RAGChain(
       openai_api_key="your_openai_api_key",
       index_path="data/index"
   )

   response = rag_chain.query("What are the key trends in AI?")
   print(response)
