"""
task_scheduler.py

A task scheduler for managing and executing various tasks in the system.
"""

import logging
import threading
import time
from datetime import datetime, timedelta
from queue import PriorityQueue


class ScheduledTask:
    """
    Represents a scheduled task with a priority, execution time, and callable function.
    """

    def __init__(self, execute_time, task_func, task_name=None, args=None, kwargs=None):
        """
        Initialize a scheduled task.

        Args:
            execute_time (datetime): The time to execute the task.
            task_func (callable): The function to execute.
            task_name (str, optional): A name for the task.
            args (list, optional): Positional arguments for the task function.
            kwargs (dict, optional): Keyword arguments for the task function.
        """
        self.execute_time = execute_time
        self.task_func = task_func
        self.task_name = task_name or "Unnamed Task"
        self.args = args or []
        self.kwargs = kwargs or {}

    def __lt__(self, other):
        """
        Comparison for priority queue. Earlier execution times have higher priority.
        """
        return self.execute_time < other.execute_time

    def execute(self):
        """
        Execute the task function with its arguments.
        """
        self.task_func(*self.args, **self.kwargs)


class TaskScheduler:
    """
    A scheduler to manage and execute tasks at specified times.
    """

    def __init__(self, check_interval=1):
        """
        Initialize the TaskScheduler.

        Args:
            check_interval (int): How often (in seconds) to check for tasks to execute.
        """
        self.tasks = PriorityQueue()
        self.running = False
        self.check_interval = check_interval
        self.logger = logging.getLogger("TaskScheduler")

    def add_task(self, execute_time, task_func, task_name=None, args=None, kwargs=None):
        """
        Schedule a new task.

        Args:
            execute_time (datetime): The time to execute the task.
            task_func (callable): The function to execute.
            task_name (str, optional): A name for the task.
            args (list, optional): Positional arguments for the task function.
            kwargs (dict, optional): Keyword arguments for the task function.
        """
        task = ScheduledTask(execute_time, task_func, task_name, args, kwargs)
        self.tasks.put(task)
        self.logger.info("Task scheduled: %s at %s", task.task_name, execute_time)

    def _process_tasks(self):
        """
        Check for and execute due tasks.
        """
        while not self.tasks.empty():
            task = self.tasks.queue[0]  # Peek at the first task
            now = datetime.now()

            if task.execute_time <= now:
                self.tasks.get()  # Remove the task from the queue
                self.logger.info("Executing task: %s", task.task_name)
                try:
                    task.execute()
                except Exception as e:
                    self.logger.error("Task %s failed: %s", task.task_name, e)
            else:
                break

    def start(self):
        """
        Start the task scheduler in a background thread.
        """
        if self.running:
            self.logger.warning("TaskScheduler is already running.")
            return

        self.running = True
        self.logger.info("TaskScheduler started.")
        threading.Thread(target=self._run, daemon=True).start()

    def stop(self):
        """
        Stop the task scheduler.
        """
        self.running = False
        self.logger.info("TaskScheduler stopped.")

    def _run(self):
        """
        Continuously process tasks while the scheduler is running.
        """
        while self.running:
            self._process_tasks()
            time.sleep(self.check_interval)


# Example usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    def example_task(task_name):
        print(f"Task executed: {task_name}")

    scheduler = TaskScheduler()

    # Add tasks
    scheduler.add_task(
        execute_time=datetime.now() + timedelta(seconds=5),
        task_func=example_task,
        task_name="Task 1",
        args=["Task 1"],
    )
    scheduler.add_task(
        execute_time=datetime.now() + timedelta(seconds=10),
        task_func=example_task,
        task_name="Task 2",
        args=["Task 2"],
    )

    # Start the scheduler
    scheduler.start()

    # Let it run for 15 seconds
    time.sleep(15)

    # Stop the scheduler
    scheduler.stop()
