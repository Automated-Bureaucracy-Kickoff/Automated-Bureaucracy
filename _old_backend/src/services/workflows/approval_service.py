"""
Approval Service

This module handles the logic for managing and processing approval workflows within the system.
"""

class ApprovalService:
    """
    Handles the approval workflow logic, including submission, review, and approval/rejection of tasks.
    """

    def __init__(self):
        """
        Initializes the ApprovalService with an empty list of approval requests.
        """
        self.approval_requests = {}

    def submit_request(self, request_id: str, user: str, task_details: dict):
        """
        Submits a new approval request.

        Args:
            request_id (str): Unique identifier for the request.
            user (str): User submitting the request.
            task_details (dict): Details of the task requiring approval.

        Returns:
            dict: Confirmation message with the request ID.
        """
        if request_id in self.approval_requests:
            raise ValueError(f"Request with ID '{request_id}' already exists.")

        self.approval_requests[request_id] = {
            "user": user,
            "task_details": task_details,
            "status": "Pending",
            "reviewer": None,
            "comments": None,
        }
        return {"message": "Request submitted successfully.", "request_id": request_id}

    def review_request(self, request_id: str, reviewer: str, approve: bool, comments: str = None):
        """
        Reviews an approval request.

        Args:
            request_id (str): ID of the request to review.
            reviewer (str): Name of the reviewer.
            approve (bool): Whether the request is approved.
            comments (str, optional): Additional comments from the reviewer.

        Returns:
            dict: Updated status of the request.
        """
        if request_id not in self.approval_requests:
            raise ValueError(f"Request with ID '{request_id}' not found.")

        request = self.approval_requests[request_id]
        if request["status"] != "Pending":
            raise ValueError(f"Request with ID '{request_id}' has already been reviewed.")

        request["status"] = "Approved" if approve else "Rejected"
        request["reviewer"] = reviewer
        request["comments"] = comments or "No additional comments."

        return {
            "message": f"Request '{request_id}' has been {'approved' if approve else 'rejected'}.",
            "status": request["status"],
        }

    def get_request_status(self, request_id: str):
        """
        Retrieves the status of a specific approval request.

        Args:
            request_id (str): ID of the request to retrieve.

        Returns:
            dict: Details of the approval request.
        """
        if request_id not in self.approval_requests:
            raise ValueError(f"Request with ID '{request_id}' not found.")

        return self.approval_requests[request_id]

    def list_requests(self, status_filter: str = None):
        """
        Lists all approval requests, optionally filtered by status.

        Args:
            status_filter (str, optional): Status to filter requests by (e.g., "Pending", "Approved", "Rejected").

        Returns:
            list: List of approval requests matching the filter.
        """
        if not status_filter:
            return list(self.approval_requests.values())

        return [
            request for request in self.approval_requests.values()
            if request["status"].lower() == status_filter.lower()
        ]
