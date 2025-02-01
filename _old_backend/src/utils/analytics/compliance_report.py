import datetime
from typing import List, Dict, Any


class ComplianceReport:
    """
    Generates compliance reports for agent activity and system adherence
    to regulatory and ethical standards.
    """

    def __init__(self):
        self.reports: List[Dict[str, Any]] = []

    def generate_report(self, agent_logs: Dict[str, List[Dict[str, Any]]], compliance_rules: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Generates a compliance report based on agent logs and predefined rules.

        Args:
            agent_logs (Dict[str, List[Dict[str, Any]]]): Logs of agent activities.
            compliance_rules (List[Dict[str, Any]]): A list of compliance rules to check.

        Returns:
            Dict[str, Any]: The generated compliance report.
        """
        report = {
            "timestamp": datetime.datetime.now().isoformat(),
            "total_agents": len(agent_logs),
            "violations": [],
        }

        # Check each agent's logs against the compliance rules
        for agent_name, logs in agent_logs.items():
            for rule in compliance_rules:
                violations = self._check_compliance(agent_name, logs, rule)
                if violations:
                    report["violations"].extend(violations)

        # Store the report
        self.reports.append(report)
        return report

    def _check_compliance(self, agent_name: str, logs: List[Dict[str, Any]], rule: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Checks compliance for a specific rule.

        Args:
            agent_name (str): Name of the agent.
            logs (List[Dict[str, Any]]): Logs for the agent.
            rule (Dict[str, Any]): A single compliance rule.

        Returns:
            List[Dict[str, Any]]: Violations of the rule.
        """
        violations = []
        for log in logs:
            # Example rule check: action not allowed
            if rule["type"] == "prohibited_action" and rule["value"] in log["activity"]:
                violations.append({
                    "agent_name": agent_name,
                    "rule": rule,
                    "log": log,
                    "message": f"Prohibited action detected: {rule['value']}",
                })

            # Example rule check: time threshold exceeded
            if rule["type"] == "time_threshold" and log.get("duration", 0) > rule["value"]:
                violations.append({
                    "agent_name": agent_name,
                    "rule": rule,
                    "log": log,
                    "message": f"Duration exceeded threshold: {log.get('duration')} > {rule['value']}",
                })

        return violations

    def list_reports(self) -> List[Dict[str, Any]]:
        """
        Lists all previously generated compliance reports.

        Returns:
            List[Dict[str, Any]]: A list of compliance reports.
        """
        return self.reports

    def save_report(self, report: Dict[str, Any], file_path: str):
        """
        Saves a compliance report to a file.

        Args:
            report (Dict[str, Any]): The compliance report to save.
            file_path (str): Path to save the report.
        """
        with open(file_path, "w") as file:
            import json
            json.dump(report, file, indent=4)
        print(f"Report saved to {file_path}")
