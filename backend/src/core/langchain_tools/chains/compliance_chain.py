"""
Compliance Chain

This module implements a LangChain-based chain for compliance checks. It ensures that actions
or processes adhere to predefined policies and regulatory standards.
"""

from langchain.chains import SequentialChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI


class ComplianceChain:
    """
    A chain that automates compliance checks, evaluates adherence to policies,
    and suggests remediation steps when non-compliance is detected.
    """

    def __init__(self, openai_api_key: str, model: str = "gpt-4"):
        """
        Initializes the ComplianceChain with an LLM and memory.

        Args:
            openai_api_key (str): OpenAI API key for accessing the LLM.
            model (str): OpenAI model to use. Default is "gpt-4".
        """
        self.memory = ConversationBufferMemory(memory_key="compliance_history")
        self.llm = OpenAI(api_key=openai_api_key, model=model, temperature=0.5)
        self.chain = self.build_chain()

    def build_chain(self) -> SequentialChain:
        """
        Builds the compliance workflow chain.

        Returns:
            SequentialChain: A LangChain SequentialChain instance.
        """
        # Step 1: Validate Input Against Policies
        validation_prompt = PromptTemplate(
            input_variables=["input_data", "policies"],
            template=(
                "Validate the following input against the provided policies:\n"
                "Input: {input_data}\n"
                "Policies: {policies}\n"
                "Return 'Compliant' or 'Non-Compliant' with reasons if non-compliant."
            ),
        )

        # Step 2: Risk Analysis
        risk_analysis_prompt = PromptTemplate(
            input_variables=["validation_result", "input_data"],
            template=(
                "Based on the validation result: {validation_result}, analyze the risks associated with "
                "the input: {input_data}. Provide a summary of potential risks and their severity levels."
            ),
        )

        # Step 3: Remediation Suggestions
        remediation_prompt = PromptTemplate(
            input_variables=["risk_analysis"],
            template=(
                "Given the risk analysis: {risk_analysis}, suggest specific remediation steps "
                "to bring the input into compliance with policies."
            ),
        )

        # Create the SequentialChain
        return SequentialChain(
            memory=self.memory,
            chains=[
                validation_prompt.to_chain(llm=self.llm),
                risk_analysis_prompt.to_chain(llm=self.llm),
                remediation_prompt.to_chain(llm=self.llm),
            ],
            verbose=True,
        )

    def check_compliance(self, input_data: str, policies: str) -> dict:
        """
        Processes compliance checks for the provided input and policies.

        Args:
            input_data (str): The data or action to evaluate for compliance.
            policies (str): The policies to check compliance against.

        Returns:
            dict: A dictionary containing validation results, risk analysis, and remediation suggestions.
        """
        try:
            result = self.chain.run({"input_data": input_data, "policies": policies})
            return {
                "validation": result.get("validation_result", "Unknown"),
                "risk_analysis": result.get("risk_analysis", "No risk analysis provided."),
                "remediation": result.get("remediation_steps", "No suggestions available."),
            }
        except Exception as e:
            return {"error": f"Failed to process compliance check: {str(e)}"}


if __name__ == "__main__":
    # Example usage of the ComplianceChain
    import os

    # Retrieve the OpenAI API key from environment variables
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your_openai_api_key_here")

    # Initialize the ComplianceChain
    compliance_chain = ComplianceChain(openai_api_key=OPENAI_API_KEY)

    # Example compliance check
    input_data = "Approve a $10,000 budget for a new marketing campaign targeting minors."
    policies = (
        "1. Budgets over $5,000 require two levels of approval.\n"
        "2. Marketing campaigns targeting minors must comply with COPPA regulations.\n"
    )

    response = compliance_chain.check_compliance(input_data, policies)

    # Print the compliance check results
    print("Compliance Check Results:")
    print(response)
