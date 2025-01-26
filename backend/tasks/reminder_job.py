"""
reminder_job.py

A module to schedule and send reminders for tasks and workflows.
"""

import logging
from datetime import datetime, timedelta
import threading
import time


class ReminderJob:
    """
    Handles scheduling and sending reminders for tasks and workflows.
    """

    def __init__(self, check_interval=60):
        """
        Initialize the ReminderJob instance.

        Args:
            check_interval (int): Interval in seconds to check for reminders.
        """
        self.reminders = []
        self.check_interval = check_interval
        self.logger = logging.getLogger("ReminderJob")
        self.running = False

    def add_reminder(self, reminder_time, message, metadata=None):
        """
        Add a new reminder.

        Args:
            reminder_time (datetime): The time for the reminder.
            message (str): The reminder message.
            metadata (dict, optional): Additional metadata related to the reminder.
        """
        reminder = {
            "time": reminder_time,
            "message": message,
            "metadata": metadata or {},
        }
        self.reminders.append(reminder)
        self.logger.info("Added reminder: %s", reminder)

    def _check_reminders(self):
        """
        Check for due reminders and process them.
        """
        now = datetime.now()
        due_reminders = [r for r in self.reminders if r["time"] <= now]

        for reminder in due_reminders:
            self._send_reminder(reminder)
            self.reminders.remove(reminder)

    def _send_reminder(self, reminder):
        """
        Send the reminder (logs it for simplicity; replace with actual notification logic).

        Args:
            reminder (dict): The reminder to send.
        """
        self.logger.info("Reminder: %s", reminder["message"])
        # Placeholder for actual reminder notification logic, e.g., email, SMS, etc.

    def start(self):
        """
        Start the reminder job loop.
        """
        self.running = True
        self.logger.info("Starting reminder job.")
        threading.Thread(target=self._run, daemon=True).start()

    def stop(self):
        """
        Stop the reminder job loop.
        """
        self.running = False
        self.logger.info("Stopping reminder job.")

    def _run(self):
        """
        Continuously check for reminders while the job is running.
        """
        while self.running:
            self._check_reminders()
            time.sleep(self.check_interval)

    def list_reminders(self):
        """
        List all scheduled reminders.

        Returns:
            list: A list of scheduled reminders.
        """
        return self.reminders

    def clear_reminders(self):
        """
        Clear all scheduled reminders.
        """
        self.reminders = []
        self.logger.info("Cleared all reminders.")


# Example usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    reminder_job = ReminderJob(check_interval=30)

    # Add reminders
    reminder_job.add_reminder(
        reminder_time=datetime.now() + timedelta(seconds=10),
        message="Check workflow approvals.",
    )
    reminder_job.add_reminder(
        reminder_time=datetime.now() + timedelta(seconds=20),
        message="Send compliance report.",
    )

    # Start the reminder job
    reminder_job.start()

    # Let the job run for 60 seconds
    time.sleep(60)
    reminder_job.stop()
