"""
RAG Chain

This module implements a Retrieval-Augmented Generation (RAG) chain
using LangChain. It combines document retrieval and generation to
provide context-aware responses.
"""

from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
import os


class RAGChain:
    """
    Implements a Retrieval-Augmented Generation (RAG) workflow that retrieves
    relevant documents and generates responses based on them.
    """

    def __init__(self, openai_api_key: str, model: str = "gpt-4", index_path: str = "data/index"):
        """
        Initializes the RAGChain with retrieval and generation capabilities.

        Args:
            openai_api_key (str): OpenAI API key for accessing the LLM.
            model (str): OpenAI model to use. Default is "gpt-4".
            index_path (str): Path to the FAISS index for retrieval.
        """
        self.openai_api_key = openai_api_key
        self.model = model
        self.index_path = index_path

        # Initialize LLM
        self.llm = OpenAI(api_key=openai_api_key, model=model, temperature=0.7)

        # Initialize the retriever
        self.retriever = self.initialize_retriever()

        # Build RAG chain
        self.chain = self.build_rag_chain()

    def initialize_retriever(self):
        """
        Loads the FAISS retriever for document retrieval.

        Returns:
            FAISS retriever object.
        """
        if not os.path.exists(self.index_path):
            raise ValueError(f"Index path '{self.index_path}' does not exist.")

        embeddings = OpenAIEmbeddings(api_key=self.openai_api_key)
        return FAISS.load_local(self.index_path, embeddings)

    def build_rag_chain(self) -> RetrievalQA:
        """
        Builds the RAG chain for combining retrieval and generation.

        Returns:
            RetrievalQA chain object.
        """
        prompt = PromptTemplate(
            input_variables=["context", "query"],
            template=(
                "You are an expert assistant. Use the following context to answer the query:\n"
                "Context: {context}\n"
                "Query: {query}\n"
                "Provide a concise and informative response."
            ),
        )
        return RetrievalQA(
            retriever=self.retriever,
            llm=self.llm,
            prompt=prompt,
            verbose=True,
        )

    def query(self, query_text: str) -> dict:
        """
        Executes a query using the RAG chain.

        Args:
            query_text (str): The input query for retrieval and generation.

        Returns:
            dict: A dictionary containing the response and retrieved documents.
        """
        try:
            response = self.chain.run({"query": query_text})
            return {"response": response}
        except Exception as e:
            return {"error": f"Failed to execute RAG chain: {str(e)}"}


if __name__ == "__main__":
    # Example usage of the RAGChain
    import os

    # Set environment variables or hardcode for testing
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your_openai_api_key_here")
    INDEX_PATH = os.getenv("INDEX_PATH", "data/index")

    # Initialize RAGChain
    rag_chain = RAGChain(openai_api_key=OPENAI_API_KEY, index_path=INDEX_PATH)

    # Example query
    query_text = "What are the latest trends in AI research?"
    result = rag_chain.query(query_text)

    # Print the result
    print("RAG Chain Output:")
    print(result)
