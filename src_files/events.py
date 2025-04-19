"""Logic for managing event creation and description."""

import time
import win32gui # pylint: disable=import-error
from datetime import datetime, timezone
from pywin32 import win32con # pylint: disable=import-error

class Topic:
    """This is to designate different "tasks" or study topics.

    Definitely adding more variables and methods."""

    def __init__(self, name: str, action_type: str, whitelist: set, **kwargs):
        self.name = name  # e.g. “Calculus”
        self.action_type = action_type  # e.g. “Studying”
        self.whitelist = whitelist  # Set of permitted applications

        # Args to be used if class is made from database information.
        if kwargs:
            self.goal_period = kwargs.get("goal_period")
            self.goal_time = kwargs.get("goal_time")
            self.whitelist = kwargs.get("whitelist")
            self.time_spent = kwargs.get("time_spent")
        else:
            self.goal_period = None
            self.goal_time = None
            self.whitelist = None
            self.time_spent = None

    def __str__(self):
        """This will probably never be run."""
        return self.action_type + " " + self.name

    def set_time_goal(self, time_goal: float, duration):
        """Sets a time spent goal per period, e.g. 5h/week."""
        self.goal_time = time_goal
        self.goal_period = duration

    def update_whitelist(self, item: str, state: str):
        """Adds/Removes an item to/from the application whitelist"""
        if "remove" in state:
            self.whitelist.remove(item)
        elif "add" in state:
            self.whitelist.add(item)

class Event:
    """Contains information relevant to the current event"""

    def __init__(self, topic : Topic):
        self.topic = topic
        self.summary = f"{topic.action_type} {topic.name}"
        self.start_time = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
        self.end_time = None
        self.description = " "
        self.initial_time = time.time()
        self.paused_time = 0
        self.temp_time = 0

    def pause_time(self):
        """First of time stop function call pair"""
        self.temp_time = time.time()

    def unpause_time(self):
        """Second of time stop function call pair"""
        self.paused_time = time.time() - self.temp_time

    def set_description(self, *args):
        """Used to add a description for the event"""
        if args:
            self.description = args[0]
        else:
            self.description = input()

    def get_total_time(self):
        """Returns total time. Is a function since value is always changing"""
        return self.initial_time - self.paused_time

    def on_topic_reminder(self):
        """Called when user is not on topic, and used to select action."""
        window = get_window_name()

        # Lacks validation since this will be replaced with GUI
        print(f"\n Shouldn't you be {self.summary} right now? \n")
        user_input = int(input("1: Add to whitelist \n 2: Exit \n"))

        # Again, no validation here.
        if user_input == 1:
            self.topic.update_whitelist(window, "add")
        elif user_input == 2:
            win32gui.PostMessage(window, win32con.WM_CLOSE, 0, 0)


def get_window_name():
    """Returns the name of the window that the user is on."""
    window = win32gui.GetForegroundWindow()
    return win32gui.GetWindowText(window)