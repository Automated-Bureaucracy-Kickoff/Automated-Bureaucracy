"""
Compliance Checker Tool
This module defines the ComplianceCheckerTool class, which validates tasks and workflows against predefined compliance rules.
"""

from typing import List, Dict, Any


class ComplianceCheckerTool:
    """
    Tool to check compliance of tasks and workflows against predefined rules.
    """

    def __init__(self, rules: List[Dict[str, Any]]):
        """
        Initialize the compliance checker tool.

        Args:
            rules (List[Dict[str, Any]]): List of compliance rules to validate against.
        """
        self.rules = rules

    def validate_task(self, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate a single task against the compliance rules.

        Args:
            task_data (Dict[str, Any]): The task data to validate.

        Returns:
            Dict[str, Any]: Validation result with a compliance status and details.
        """
        violations = []
        for rule in self.rules:
            if not self._check_rule(task_data, rule):
                violations.append(rule)

        return {
            "task_name": task_data.get("task_name", "Unknown Task"),
            "is_compliant": len(violations) == 0,
            "violations": violations,
        }

    def validate_workflow(self, workflow_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Validate a workflow (list of tasks) against the compliance rules.

        Args:
            workflow_data (List[Dict[str, Any]]): The workflow data to validate.

        Returns:
            Dict[str, Any]: Validation result for the entire workflow with compliance status.
        """
        workflow_result = []
        for task in workflow_data:
            result = self.validate_task(task)
            workflow_result.append(result)

        non_compliant_tasks = [task for task in workflow_result if not task["is_compliant"]]

        return {
            "is_compliant": len(non_compliant_tasks) == 0,
            "details": workflow_result,
            "non_compliant_tasks": non_compliant_tasks,
        }

    def _check_rule(self, data: Dict[str, Any], rule: Dict[str, Any]) -> bool:
        """
        Check if a piece of data complies with a specific rule.

        Args:
            data (Dict[str, Any]): The data to check.
            rule (Dict[str, Any]): The rule to validate against.

        Returns:
            bool: True if compliant, False otherwise.
        """
        rule_type = rule.get("type")
        rule_field = rule.get("field")
        rule_value = rule.get("value")

        if rule_type == "equals":
            return data.get(rule_field) == rule_value
        elif rule_type == "greater_than":
            return data.get(rule_field, 0) > rule_value
        elif rule_type == "less_than":
            return data.get(rule_field, 0) < rule_value
        elif rule_type == "contains":
            return rule_value in data.get(rule_field, [])
        else:
            return True  # Unknown rule types are treated as valid for now.

    def add_rule(self, rule: Dict[str, Any]) -> None:
        """
        Add a new compliance rule.

        Args:
            rule (Dict[str, Any]): The rule to add.
        """
        self.rules.append(rule)

    def list_rules(self) -> List[Dict[str, Any]]:
        """
        List all compliance rules.

        Returns:
            List[Dict[str, Any]]: The compliance rules.
        """
        return self.rules


# Example Usage
if __name__ == "__main__":
    # Define some compliance rules
    compliance_rules = [
        {"type": "greater_than", "field": "budget", "value": 1000},
        {"type": "equals", "field": "department", "value": "Finance"},
        {"type": "contains", "field": "tags", "value": "urgent"},
    ]

    # Initialize the tool with rules
    tool = ComplianceCheckerTool(rules=compliance_rules)

    # Define a task
    task = {
        "task_name": "Approve Budget",
        "budget": 1500,
        "department": "Finance",
        "tags": ["urgent", "high-priority"],
    }

    # Validate the task
    result = tool.validate_task(task)
    print("Task Validation Result:", result)

    # Define a workflow
    workflow = [
        {
            "task_name": "Approve Budget",
            "budget": 1500,
            "department": "Finance",
            "tags": ["urgent", "high-priority"],
        },
        {
            "task_name": "Plan Event",
            "budget": 500,
            "department": "Marketing",
            "tags": ["low-priority"],
        },
    ]

    # Validate the workflow
    workflow_result = tool.validate_workflow(workflow)
    print("Workflow Validation Result:", workflow_result)

    # List all compliance rules
    print("Compliance Rules:", tool.list_rules())
