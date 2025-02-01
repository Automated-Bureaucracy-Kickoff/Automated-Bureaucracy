"""
priority_task_queue.py

A module that implements a priority-based task queue to manage and execute tasks efficiently.
"""

import heapq
import logging
from datetime import datetime

class Task:
    """
    Represents a task with a priority, name, and optional metadata.
    """
    def __init__(self, priority, name, metadata=None):
        """
        Initialize a Task instance.

        Args:
            priority (int): Priority level of the task (lower value indicates higher priority).
            name (str): Name of the task.
            metadata (dict, optional): Additional metadata related to the task.
        """
        self.priority = priority
        self.name = name
        self.metadata = metadata or {}
        self.timestamp = datetime.now()

    def __lt__(self, other):
        """
        Define comparison for priority queue (min-heap).

        Tasks with the same priority are compared based on their timestamp.
        """
        return (self.priority, self.timestamp) < (other.priority, other.timestamp)

    def __repr__(self):
        """
        Represent the task for debugging and logging purposes.
        """
        return f"Task(name={self.name}, priority={self.priority}, timestamp={self.timestamp})"


class PriorityTaskQueue:
    """
    A priority-based task queue implemented using a min-heap.
    """

    def __init__(self):
        """
        Initialize the priority task queue.
        """
        self.task_queue = []
        self.logger = logging.getLogger("PriorityTaskQueue")

    def add_task(self, task):
        """
        Add a task to the queue.

        Args:
            task (Task): The task to add.
        """
        heapq.heappush(self.task_queue, task)
        self.logger.info("Task added: %s", task)

    def get_next_task(self):
        """
        Retrieve and remove the highest-priority task from the queue.

        Returns:
            Task: The highest-priority task.
        """
        if self.is_empty():
            self.logger.warning("Attempted to retrieve a task from an empty queue.")
            return None
        task = heapq.heappop(self.task_queue)
        self.logger.info("Task retrieved: %s", task)
        return task

    def peek_next_task(self):
        """
        Peek at the highest-priority task without removing it.

        Returns:
            Task: The highest-priority task or None if the queue is empty.
        """
        if self.is_empty():
            self.logger.warning("Attempted to peek at a task in an empty queue.")
            return None
        return self.task_queue[0]

    def is_empty(self):
        """
        Check if the task queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self.task_queue) == 0

    def get_task_count(self):
        """
        Get the number of tasks in the queue.

        Returns:
            int: The number of tasks.
        """
        return len(self.task_queue)

    def clear(self):
        """
        Clear all tasks from the queue.
        """
        self.task_queue = []
        self.logger.info("All tasks cleared from the queue.")

    def list_tasks(self):
        """
        List all tasks in the queue.

        Returns:
            list: A list of tasks in the queue, sorted by priority.
        """
        return sorted(self.task_queue)

    def log_status(self):
        """
        Log the current status of the task queue.
        """
        if self.is_empty():
            self.logger.info("Task queue is empty.")
        else:
            self.logger.info("Task queue contains %d tasks: %s", len(self.task_queue), self.list_tasks())
