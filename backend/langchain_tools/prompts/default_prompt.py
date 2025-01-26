"""
Default Prompt Module

Provides a standard set of default prompts for various LangChain workflows.
"""

from langchain.prompts import PromptTemplate


class DefaultPrompt:
    """
    A collection of reusable default prompts for common use cases.
    """

    @staticmethod
    def default_agent_prompt() -> PromptTemplate:
        """
        Generates a default system prompt for an agent.

        Returns:
            PromptTemplate: A prompt template for general agent behavior.
        """
        template = """
        You are a highly intelligent and versatile agent designed to assist with a wide variety of tasks.

        Guidelines:
        1. Be concise yet thorough in your responses.
        2. Provide examples or detailed steps when necessary.
        3. Always prioritize accuracy and clarity.
        4. Adhere to the context and objectives provided in each task.

        Task Context:
        {context}

        Provide your output below:
        """
        return PromptTemplate(
            input_variables=["context"],
            template=template.strip(),
        )

    @staticmethod
    def default_conversation_prompt() -> PromptTemplate:
        """
        Generates a default conversation prompt for chat-based tasks.

        Returns:
            PromptTemplate: A prompt template for conversation workflows.
        """
        template = """
        You are participating in a dynamic and engaging conversation. Your goal is to:
        - Respond intelligently and empathetically.
        - Keep the conversation informative and engaging.
        - Ensure your responses are coherent and contextually relevant.

        Conversation Context:
        {conversation_context}

        Current User Input:
        {user_input}

        Provide your response below:
        """
        return PromptTemplate(
            input_variables=["conversation_context", "user_input"],
            template=template.strip(),
        )

    @staticmethod
    def default_task_prompt() -> PromptTemplate:
        """
        Generates a default task execution prompt.

        Returns:
            PromptTemplate: A prompt template for executing tasks.
        """
        template = """
        Task Execution Instructions:
        - Review the task description carefully.
        - Ensure all outputs align with the provided objectives.
        - Be thorough and precise in your solution.

        Task Description:
        {task_description}

        Provide your detailed response below:
        """
        return PromptTemplate(
            input_variables=["task_description"],
            template=template.strip(),
        )

    @staticmethod
    def default_fallback_prompt() -> PromptTemplate:
        """
        Generates a default fallback prompt for handling unknown requests.

        Returns:
            PromptTemplate: A prompt template for fallback behavior.
        """
        template = """
        The input request is not recognized or falls outside of your standard capabilities.
        Please do the following:
        1. Identify the core intent of the input.
        2. Provide any relevant information or suggest alternatives.

        Input Received:
        {input_data}

        Provide your output below:
        """
        return PromptTemplate(
            input_variables=["input_data"],
            template=template.strip(),
        )


# Example Usage
if __name__ == "__main__":
    # Example of Default Agent Prompt
    agent_prompt = DefaultPrompt.default_agent_prompt()
    print("Agent Prompt Example:")
    print(agent_prompt.format(context="Assist with summarizing the latest research on renewable energy."))

    # Example of Default Conversation Prompt
    conversation_prompt = DefaultPrompt.default_conversation_prompt()
    print("\nConversation Prompt Example:")
    print(conversation_prompt.format(
        conversation_context="A discussion about the impact of AI on healthcare.",
        user_input="What are the most promising applications of AI in medicine?"
    ))

    # Example of Default Task Prompt
    task_prompt = DefaultPrompt.default_task_prompt()
    print("\nTask Prompt Example:")
    print(task_prompt.format(task_description="Analyze the trends in e-commerce sales over the past decade."))

    # Example of Default Fallback Prompt
    fallback_prompt = DefaultPrompt.default_fallback_prompt()
    print("\nFallback Prompt Example:")
    print(fallback_prompt.format(input_data="Query: How to repair a microwave?"))
