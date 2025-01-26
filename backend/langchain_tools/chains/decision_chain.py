"""
Decision Chain

This module implements a LangChain-based chain for structured decision-making workflows.
It evaluates input data, processes context, and provides actionable recommendations.
"""

from langchain.chains import SequentialChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI


class DecisionChain:
    """
    A chain that guides decision-making processes by evaluating inputs, analyzing context,
    and recommending actions.
    """

    def __init__(self, openai_api_key: str, model: str = "gpt-4"):
        """
        Initializes the DecisionChain with an LLM and memory.

        Args:
            openai_api_key (str): OpenAI API key for accessing the LLM.
            model (str): OpenAI model to use. Default is "gpt-4".
        """
        self.memory = ConversationBufferMemory(memory_key="decision_chain_history")
        self.llm = OpenAI(api_key=openai_api_key, model=model, temperature=0.7)
        self.chain = self.build_chain()

    def build_chain(self) -> SequentialChain:
        """
        Builds the decision-making workflow chain.

        Returns:
            SequentialChain: A LangChain SequentialChain instance.
        """
        # Step 1: Evaluate Inputs
        evaluation_prompt = PromptTemplate(
            input_variables=["data"],
            template=(
                "Evaluate the following input data: {data}. Identify key factors "
                "relevant to decision-making and classify them as positive, negative, or neutral."
            ),
        )

        # Step 2: Analyze Context
        context_analysis_prompt = PromptTemplate(
            input_variables=["evaluation"],
            template=(
                "Based on the evaluation: {evaluation}, analyze the broader context "
                "and identify potential risks, opportunities, and constraints."
            ),
        )

        # Step 3: Recommend Actions
        recommendation_prompt = PromptTemplate(
            input_variables=["context_analysis"],
            template=(
                "Given the context analysis: {context_analysis}, recommend the best course of action. "
                "Provide a detailed justification for your recommendation."
            ),
        )

        # Create the SequentialChain
        return SequentialChain(
            memory=self.memory,
            chains=[
                evaluation_prompt.to_chain(llm=self.llm),
                context_analysis_prompt.to_chain(llm=self.llm),
                recommendation_prompt.to_chain(llm=self.llm),
            ],
            verbose=True,
        )

    def process_decision(self, data: str) -> dict:
        """
        Processes a decision-making workflow based on input data.

        Args:
            data (str): The input data for the decision-making process.

        Returns:
            dict: A dictionary containing evaluation results, context analysis, and recommended actions.
        """
        try:
            result = self.chain.run({"data": data})
            return {
                "evaluation": result.get("evaluation", "No evaluation available."),
                "context_analysis": result.get("context_analysis", "No context analysis provided."),
                "recommendation": result.get("recommendation", "No recommendation available."),
            }
        except Exception as e:
            return {"error": f"Failed to process decision-making workflow: {str(e)}"}


if __name__ == "__main__":
    # Example usage of DecisionChain
    import os

    # Retrieve the OpenAI API key from environment variables
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your_openai_api_key_here")

    # Initialize the DecisionChain
    decision_chain = DecisionChain(openai_api_key=OPENAI_API_KEY)

    # Example decision-making process
    input_data = (
        "The organization is considering launching a new product line targeting environmentally conscious consumers. "
        "The budget is $500,000, and there are concerns about potential competition in the market."
    )

    response = decision_chain.process_decision(input_data)

    # Print the decision-making results
    print("Decision-Making Workflow Results:")
    print(response)
