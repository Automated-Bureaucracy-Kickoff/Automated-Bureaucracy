"""
Compliance Service

This module handles compliance checks and reporting for workflows and tasks within the system.
"""

class ComplianceService:
    """
    Handles compliance-related operations such as rule validation, reporting, and task verification.
    """

    def __init__(self):
        """
        Initializes the ComplianceService with an empty set of rules and a log of compliance checks.
        """
        self.compliance_rules = []
        self.compliance_logs = []

    def add_rule(self, rule_id: str, description: str, validation_function):
        """
        Adds a new compliance rule.

        Args:
            rule_id (str): Unique identifier for the rule.
            description (str): Description of the rule.
            validation_function (callable): Function to validate the rule. It should accept task details and return a boolean.

        Returns:
            dict: Confirmation message with the rule ID.
        """
        self.compliance_rules.append({
            "rule_id": rule_id,
            "description": description,
            "validate": validation_function,
        })
        return {"message": "Compliance rule added successfully.", "rule_id": rule_id}

    def check_compliance(self, task_details: dict):
        """
        Checks compliance for a given task against all registered rules.

        Args:
            task_details (dict): Details of the task to check.

        Returns:
            dict: Compliance results, including passed and failed rules.
        """
        results = {"passed": [], "failed": []}

        for rule in self.compliance_rules:
            is_compliant = rule["validate"](task_details)
            if is_compliant:
                results["passed"].append(rule["rule_id"])
            else:
                results["failed"].append(rule["rule_id"])

            # Log the compliance check
            self.compliance_logs.append({
                "task_details": task_details,
                "rule_id": rule["rule_id"],
                "result": "Passed" if is_compliant else "Failed",
            })

        return results

    def generate_report(self):
        """
        Generates a compliance report based on all logged compliance checks.

        Returns:
            list: List of compliance check logs.
        """
        return self.compliance_logs

    def list_rules(self):
        """
        Lists all registered compliance rules.

        Returns:
            list: List of compliance rules with their descriptions.
        """
        return [{"rule_id": rule["rule_id"], "description": rule["description"]} for rule in self.compliance_rules]
