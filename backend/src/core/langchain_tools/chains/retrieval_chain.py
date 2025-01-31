"""
Retrieval Chain

This module implements a chain focused solely on document retrieval. 
It enables efficient fetching of relevant information from a vector store or database.
"""

from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
import os


class RetrievalChain:
    """
    A LangChain-based chain for efficient document retrieval.
    """

    def __init__(self, openai_api_key: str, index_path: str = "data/index", model: str = "gpt-4"):
        """
        Initializes the RetrievalChain with an LLM and a vector store for retrieval.

        Args:
            openai_api_key (str): OpenAI API key for accessing the LLM.
            index_path (str): Path to the FAISS index for retrieval.
            model (str): OpenAI model to use. Default is "gpt-4".
        """
        self.openai_api_key = openai_api_key
        self.index_path = index_path
        self.model = model

        # Initialize the LLM
        self.llm = OpenAI(api_key=openai_api_key, model=model, temperature=0)

        # Initialize the retriever
        self.retriever = self.initialize_retriever()

        # Build RetrievalQA chain
        self.chain = self.build_retrieval_chain()

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

    def build_retrieval_chain(self) -> RetrievalQA:
        """
        Builds the retrieval chain for fetching relevant documents.

        Returns:
            RetrievalQA chain object.
        """
        prompt = PromptTemplate(
            input_variables=["context", "query"],
            template=(
                "You are a document retrieval assistant. Use the context below to answer the query:\n"
                "Context: {context}\n"
                "Query: {query}\n"
                "Provide a precise and relevant response."
            ),
        )
        return RetrievalQA(
            retriever=self.retriever,
            llm=self.llm,
            prompt=prompt,
            verbose=True,
        )

    def retrieve(self, query_text: str) -> dict:
        """
        Executes a retrieval query.

        Args:
            query_text (str): The input query for retrieving documents.

        Returns:
            dict: A dictionary containing the response and retrieved documents.
        """
        try:
            response = self.chain.run({"query": query_text})
            return {"response": response}
        except Exception as e:
            return {"error": f"Failed to execute retrieval chain: {str(e)}"}


if __name__ == "__main__":
    # Example usage of RetrievalChain
    import os

    # Set environment variables or hardcode for testing
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your_openai_api_key_here")
    INDEX_PATH = os.getenv("INDEX_PATH", "data/index")

    # Initialize RetrievalChain
    retrieval_chain = RetrievalChain(openai_api_key=OPENAI_API_KEY, index_path=INDEX_PATH)

    # Example query
    query_text = "What are the key benefits of using renewable energy?"
    result = retrieval_chain.retrieve(query_text)

    # Print the result
    print("Retrieval Chain Output:")
    print(result)
