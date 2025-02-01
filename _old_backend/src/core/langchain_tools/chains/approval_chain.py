"""
Approval Chain

This module implements a LangChain-based chain for approval workflows. It processes
requests through a sequence of validation and decision-making steps.
"""

from langchain.chains import SequentialChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI


class ApprovalChain:
    """
    A chain that processes approval workflows, integrating input validation, context analysis,
    and final decision-making steps.
    """

    def __init__(self, openai_api_key: str, model: str = "gpt-4"):
        """
        Initializes the ApprovalChain with an LLM and memory.

        Args:
            openai_api_key (str): OpenAI API key for accessing the LLM.
            model (str): OpenAI model to use. Default is "gpt-4".
        """
        self.memory = ConversationBufferMemory(memory_key="approval_history")
        self.llm = OpenAI(api_key=openai_api_key, model=model, temperature=0.7)
        self.chain = self.build_chain()

    def build_chain(self) -> SequentialChain:
        """
        Builds the approval workflow chain.

        Returns:
            SequentialChain: A LangChain SequentialChain instance.
        """
        # Step 1: Input Validation
        validation_prompt = PromptTemplate(
            input_variables=["request"],
            template="You are responsible for validating this request: {request}.\n"
                     "Check if it meets all the required criteria and output 'Valid' or 'Invalid'.\n"
                     "If invalid, provide reasons for rejection.",
        )

        # Step 2: Context Analysis
        context_prompt = PromptTemplate(
            input_variables=["validation_result", "request"],
            template="Given the validation result: {validation_result}, analyze the context of this request:\n"
                     "{request}.\nProvide a detailed explanation of the implications of approving or rejecting this.",
        )

        # Step 3: Decision Making
        decision_prompt = PromptTemplate(
            input_variables=["context_analysis"],
            template="Based on the context analysis: {context_analysis}, make a decision:\n"
                     "Should this request be approved or rejected? Provide a concise explanation of your decision.",
        )

        # Create the SequentialChain
        return SequentialChain(
            memory=self.memory,
            chains=[
                validation_prompt.to_chain(llm=self.llm),
                context_prompt.to_chain(llm=self.llm),
                decision_prompt.to_chain(llm=self.llm),
            ],
            verbose=True,
        )

    def process_request(self, request: str) -> dict:
        """
        Processes an approval request through the chain.

        Args:
            request (str): The input request to process.

        Returns:
            dict: A dictionary containing validation results, context analysis, and final decision.
        """
        try:
            result = self.chain.run({"request": request})
            return {
                "validation": result.get("validation_result", "Unknown"),
                "context_analysis": result.get("context_analysis", "No context provided."),
                "decision": result.get("decision", "Decision not available."),
            }
        except Exception as e:
            return {"error": f"Failed to process request: {str(e)}"}


if __name__ == "__main__":
    # Example usage of the ApprovalChain
    import os

    # Retrieve the OpenAI API key from environment variables
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your_openai_api_key_here")

    # Initialize the ApprovalChain
    approval_chain = ApprovalChain(openai_api_key=OPENAI_API_KEY)

    # Example request
    request_text = "Request to approve budget increase for Q1 marketing initiatives."
    response = approval_chain.process_request(request_text)

    # Print the response
    print("Approval Workflow Result:")
    print(response)
