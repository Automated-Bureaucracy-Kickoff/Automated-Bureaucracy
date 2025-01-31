"""
Custom Prompt Library

Defines reusable and specialized prompt templates to support dynamic agent workflows.
"""

from langchain.prompts import PromptTemplate


class CustomPromptLibrary:
    """
    A library of custom prompt templates for diverse use cases.
    """

    @staticmethod
    def generate_task_prompt(task_description: str, context: str = None) -> PromptTemplate:
        """
        Creates a prompt for executing a task.

        Args:
            task_description (str): A description of the task to execute.
            context (str, optional): Additional context for the task.

        Returns:
            PromptTemplate: A LangChain prompt template for task execution.
        """
        template = """
        Task Execution:

        Task Description:
        {task_description}

        Context:
        {context}

        Please provide a detailed step-by-step solution or response to complete the task.
        """
        return PromptTemplate(
            input_variables=["task_description", "context"],
            template=template.strip(),
        )

    @staticmethod
    def generate_brainstorm_prompt(problem_statement: str, constraints: str = None) -> PromptTemplate:
        """
        Generates a brainstorming prompt for creative problem-solving.

        Args:
            problem_statement (str): The problem to brainstorm solutions for.
            constraints (str, optional): Constraints or conditions to consider.

        Returns:
            PromptTemplate: A LangChain prompt template for brainstorming.
        """
        template = """
        Brainstorming Session:

        Problem Statement:
        {problem_statement}

        Constraints:
        {constraints}

        Provide as many innovative and feasible ideas as possible to address the problem.
        Rank the ideas based on their potential impact and feasibility.
        """
        return PromptTemplate(
            input_variables=["problem_statement", "constraints"],
            template=template.strip(),
        )

    @staticmethod
    def generate_analysis_prompt(data_summary: str, key_questions: str) -> PromptTemplate:
        """
        Generates a prompt for analyzing data or information.

        Args:
            data_summary (str): Summary of the data or information to analyze.
            key_questions (str): Key questions to address during the analysis.

        Returns:
            PromptTemplate: A LangChain prompt template for analysis.
        """
        template = """
        Data Analysis:

        Data Summary:
        {data_summary}

        Key Questions:
        {key_questions}

        Analyze the data and answer the key questions. Provide a comprehensive report with insights and recommendations.
        """
        return PromptTemplate(
            input_variables=["data_summary", "key_questions"],
            template=template.strip(),
        )

    @staticmethod
    def generate_training_prompt(training_goal: str, prerequisites: str = None) -> PromptTemplate:
        """
        Generates a prompt for training or educational purposes.

        Args:
            training_goal (str): The goal of the training session.
            prerequisites (str, optional): Prerequisites or prior knowledge required.

        Returns:
            PromptTemplate: A LangChain prompt template for training content generation.
        """
        template = """
        Training Content:

        Training Goal:
        {training_goal}

        Prerequisites:
        {prerequisites}

        Create a training module that covers the goal comprehensively. Include examples, exercises, and step-by-step instructions.
        """
        return PromptTemplate(
            input_variables=["training_goal", "prerequisites"],
            template=template.strip(),
        )

    @staticmethod
    def generate_code_review_prompt(code_snippet: str, review_criteria: str) -> PromptTemplate:
        """
        Generates a prompt for conducting a code review.

        Args:
            code_snippet (str): The code to review.
            review_criteria (str): Criteria for the review.

        Returns:
            PromptTemplate: A LangChain prompt template for code reviews.
        """
        template = """
        Code Review:

        Code Snippet:
        {code_snippet}

        Review Criteria:
        {review_criteria}

        Review the code based on the criteria. Provide feedback on best practices, potential issues, and suggested improvements.
        """
        return PromptTemplate(
            input_variables=["code_snippet", "review_criteria"],
            template=template.strip(),
        )


# Example Usage
if __name__ == "__main__":
    # Task Prompt Example
    task_prompt = CustomPromptLibrary.generate_task_prompt(
        task_description="Optimize the marketing strategy for social media platforms.",
        context="Focus on engagement metrics and budget constraints."
    )
    print("Task Prompt:")
    print(task_prompt.format(
        task_description="Optimize the marketing strategy for social media platforms.",
        context="Focus on engagement metrics and budget constraints."
    ))

    # Brainstorm Prompt Example
    brainstorm_prompt = CustomPromptLibrary.generate_brainstorm_prompt(
        problem_statement="How can we reduce carbon emissions in urban areas?",
        constraints="Solutions must be cost-effective and scalable."
    )
    print("\nBrainstorm Prompt:")
    print(brainstorm_prompt.format(
        problem_statement="How can we reduce carbon emissions in urban areas?",
        constraints="Solutions must be cost-effective and scalable."
    ))

    # Analysis Prompt Example
    analysis_prompt = CustomPromptLibrary.generate_analysis_prompt(
        data_summary="Sales data for the last quarter shows a 10% drop in revenue.",
        key_questions="1. What are the primary causes?\n2. How can we reverse this trend?"
    )
    print("\nAnalysis Prompt:")
    print(analysis_prompt.format(
        data_summary="Sales data for the last quarter shows a 10% drop in revenue.",
        key_questions="1. What are the primary causes?\n2. How can we reverse this trend?"
    ))

    # Training Prompt Example
    training_prompt = CustomPromptLibrary.generate_training_prompt(
        training_goal="Teach the basics of Python programming.",
        prerequisites="Assumes no prior programming knowledge."
    )
    print("\nTraining Prompt:")
    print(training_prompt.format(
        training_goal="Teach the basics of Python programming.",
        prerequisites="Assumes no prior programming knowledge."
    ))

    # Code Review Prompt Example
    code_review_prompt = CustomPromptLibrary.generate_code_review_prompt(
        code_snippet="def add(a, b):\n    return a + b",
        review_criteria="Ensure proper function naming, error handling, and test coverage."
    )
    print("\nCode Review Prompt:")
    print(code_review_prompt.format(
        code_snippet="def add(a, b):\n    return a + b",
        review_criteria="Ensure proper function naming, error handling, and test coverage."
    ))
