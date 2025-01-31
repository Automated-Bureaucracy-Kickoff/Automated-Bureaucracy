"""
Compliance Prompt Module

Defines prompt templates to support compliance-related workflows.
"""

from langchain.prompts import PromptTemplate

class CompliancePrompt:
    """
    Generates prompts for compliance-related tasks.
    """

    @staticmethod
    def generate_compliance_check_prompt(task_description: str, rules: str) -> PromptTemplate:
        """
        Generates a prompt to perform a compliance check.

        Args:
            task_description (str): Description of the task or process to check.
            rules (str): Compliance rules or guidelines.

        Returns:
            PromptTemplate: A LangChain prompt template for compliance checks.
        """
        template = """
        Compliance Check:

        Task Description:
        {task_description}

        Compliance Rules:
        {rules}

        Based on the given rules, evaluate the compliance of the task.
        Provide a detailed report indicating:
        - Whether the task complies with the rules.
        - Specific rule violations, if any.
        - Suggestions for achieving compliance.
        """
        return PromptTemplate(
            input_variables=["task_description", "rules"],
            template=template.strip(),
        )

    @staticmethod
    def generate_compliance_summary_prompt(agent_logs: str, rules: str) -> PromptTemplate:
        """
        Generates a prompt to summarize compliance findings.

        Args:
            agent_logs (str): Logs or activities to evaluate for compliance.
            rules (str): Compliance rules or guidelines.

        Returns:
            PromptTemplate: A LangChain prompt template for compliance summaries.
        """
        template = """
        Compliance Summary:

        Logs/Activities:
        {agent_logs}

        Compliance Rules:
        {rules}

        Generate a summary of compliance findings:
        - Highlight activities that adhered to the rules.
        - Identify areas where compliance was lacking.
        - Provide actionable recommendations for improvement.
        """
        return PromptTemplate(
            input_variables=["agent_logs", "rules"],
            template=template.strip(),
        )

    @staticmethod
    def generate_violation_notification_prompt(violation_details: str, corrective_actions: str) -> PromptTemplate:
        """
        Generates a prompt for notifying about a compliance violation.

        Args:
            violation_details (str): Details of the compliance violation.
            corrective_actions (str): Suggested actions to resolve the issue.

        Returns:
            PromptTemplate: A LangChain prompt template for violation notifications.
        """
        template = """
        Compliance Violation Notification:

        Violation Details:
        {violation_details}

        Corrective Actions:
        {corrective_actions}

        Notify the relevant stakeholders about the violation and outline the corrective measures.
        Emphasize the importance of adherence to compliance rules to prevent recurrence.
        """
        return PromptTemplate(
            input_variables=["violation_details", "corrective_actions"],
            template=template.strip(),
        )


# Example Usage
if __name__ == "__main__":
    # Example: Compliance Check Prompt
    compliance_check_prompt = CompliancePrompt.generate_compliance_check_prompt(
        task_description="Evaluate the privacy policy implementation for GDPR compliance.",
        rules="1. Data processing must have a lawful basis.\n2. Users must have access to opt-out options."
    )
    print("Compliance Check Prompt:")
    print(compliance_check_prompt.format(
        task_description="Evaluate the privacy policy implementation for GDPR compliance.",
        rules="1. Data processing must have a lawful basis.\n2. Users must have access to opt-out options."
    ))

    # Example: Compliance Summary Prompt
    compliance_summary_prompt = CompliancePrompt.generate_compliance_summary_prompt(
        agent_logs="User data logs from 2025-01-24 indicate access without consent.",
        rules="1. Data must not be accessed without user consent.\n2. Logs must be encrypted."
    )
    print("\nCompliance Summary Prompt:")
    print(compliance_summary_prompt.format(
        agent_logs="User data logs from 2025-01-24 indicate access without consent.",
        rules="1. Data must not be accessed without user consent.\n2. Logs must be encrypted."
    ))

    # Example: Violation Notification Prompt
    violation_notification_prompt = CompliancePrompt.generate_violation_notification_prompt(
        violation_details="User consent logs are missing for data processing from 2025-01-24.",
        corrective_actions="1. Implement user consent checks.\n2. Audit logs for gaps."
    )
    print("\nViolation Notification Prompt:")
    print(violation_notification_prompt.format(
        violation_details="User consent logs are missing for data processing from 2025-01-24.",
        corrective_actions="1. Implement user consent checks.\n2. Audit logs for gaps."
    ))
