"""
Approval Prompt Module

Defines a prompt template to facilitate approval workflows.
"""

from langchain.prompts import PromptTemplate

class ApprovalPrompt:
    """
    Generates prompts for approval workflows.
    """

    @staticmethod
    def generate_approval_request_prompt(task_description: str, requester: str, approver: str) -> PromptTemplate:
        """
        Generates a prompt for requesting approval on a task.

        Args:
            task_description (str): The description of the task needing approval.
            requester (str): The person or system requesting approval.
            approver (str): The person or system responsible for approval.

        Returns:
            PromptTemplate: A LangChain prompt template for the approval request.
        """
        template = """
        Task Approval Request:

        Task Description:
        {task_description}

        Requested by:
        {requester}

        Approver:
        {approver}

        Please provide your decision (approve/reject) and a reason for your decision.
        """
        return PromptTemplate(
            input_variables=["task_description", "requester", "approver"],
            template=template.strip(),
        )

    @staticmethod
    def generate_approval_response_prompt(task_description: str, decision: str, reason: str) -> PromptTemplate:
        """
        Generates a prompt for responding to an approval request.

        Args:
            task_description (str): The description of the task being approved/rejected.
            decision (str): The approval decision (approve/reject).
            reason (str): The reason for the decision.

        Returns:
            PromptTemplate: A LangChain prompt template for the approval response.
        """
        template = """
        Approval Response:

        Task Description:
        {task_description}

        Decision:
        {decision}

        Reason for Decision:
        {reason}
        """
        return PromptTemplate(
            input_variables=["task_description", "decision", "reason"],
            template=template.strip(),
        )


# Example Usage
if __name__ == "__main__":
    # Generate a task approval request prompt
    approval_request_prompt = ApprovalPrompt.generate_approval_request_prompt(
        task_description="Review the new marketing strategy for Q2.",
        requester="Marketing Team",
        approver="Operations Manager"
    )
    print("Approval Request Prompt:")
    print(approval_request_prompt.format(
        task_description="Review the new marketing strategy for Q2.",
        requester="Marketing Team",
        approver="Operations Manager"
    ))

    # Generate a task approval response prompt
    approval_response_prompt = ApprovalPrompt.generate_approval_response_prompt(
        task_description="Review the new marketing strategy for Q2.",
        decision="Approved",
        reason="The strategy aligns with company objectives."
    )
    print("\nApproval Response Prompt:")
    print(approval_response_prompt.format(
        task_description="Review the new marketing strategy for Q2.",
        decision="Approved",
        reason="The strategy aligns with company objectives."
    ))
