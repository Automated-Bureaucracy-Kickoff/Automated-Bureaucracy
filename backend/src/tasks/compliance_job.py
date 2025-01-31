"""
compliance_job.py

This module defines a compliance job that checks workflows and documents for compliance against predefined rules.
"""

from datetime import datetime
from backend.services.workflows.compliance_service import ComplianceService
from backend.analytics.compliance_report import ComplianceReport
import logging

class ComplianceJob:
    """
    A class that defines a scheduled compliance job for workflows and documents.
    """

    def __init__(self):
        """
        Initialize the ComplianceJob with required services.
        """
        self.compliance_service = ComplianceService()
        self.compliance_report = ComplianceReport()
        self.logger = logging.getLogger("ComplianceJob")

    def run(self):
        """
        Run the compliance job.

        This job retrieves workflows and documents, checks them for compliance, and generates a compliance report.
        """
        self.logger.info("Starting compliance job at %s", datetime.now())
        try:
            # Fetch workflows and documents for compliance checks
            workflows = self.compliance_service.get_all_workflows()
            documents = self.compliance_service.get_all_documents()

            # Check compliance for workflows
            workflow_results = []
            for workflow in workflows:
                result = self.compliance_service.check_workflow_compliance(workflow)
                workflow_results.append({"workflow_id": workflow["id"], "compliant": result})

            # Check compliance for documents
            document_results = []
            for document in documents:
                result = self.compliance_service.check_document_compliance(document)
                document_results.append({"document_id": document["id"], "compliant": result})

            # Generate a compliance report
            report = self.compliance_report.generate_report(
                {"workflows": workflow_results, "documents": document_results},
                rules=self.compliance_service.get_active_rules()
            )
            self.logger.info("Compliance report generated: %s", report)

        except Exception as e:
            self.logger.error("Error running compliance job: %s", str(e))
            raise

        self.logger.info("Compliance job completed at %s", datetime.now())
