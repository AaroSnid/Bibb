import time
import win32gui
from datetime import datetime, timezone
from pywin32 import win32con

class Topic:
    """This is to designate different "tasks" or study topics. Definitely adding more variables and methods."""

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

    # This will probably never be run
    def __str__(self):
        return self.action_type + " " + self.name

    # Sets a time spent goal per period, e.g. 5h/week
    def set_time_goal(self, time_goal: float, duration):
        self.goal_time = time_goal
        self.goal_period = duration

    # Adds/Removes an item to/from the application whitelist
    def update_whitelist(self, item: str, state: str):
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

    #First of function call pair
    def pause_time(self):
        self.temp_time = time.time()

    #Second of functino call pair
    def unpause_time(self):
        self.paused_time = time.time() - self.temp_time

    #Allows a description entry addition
    def set_description(self, *args):
        if args:
            self.description = args[0]
        else:
            self.description = input()

    #Returns total time. Is a function since value is always changing
    def get_total_time(self):
        return self.initial_time - self.paused_time

    # Called when user is not on topic, and used to select action
    def on_topic_reminder(self):
        window = get_window_name()

        #Lacks validation since this will be replaced with GUI
        print(f"\n Shouldn't you be {self.summary} right now? \n")
        user_input = int(input("1: Add to whitelist \n 2: Exit \n"))

        #Again, no validation here.
        if user_input == 1:
            self.topic.update_whitelist(window, "add")
        elif user_input == 2:
            win32gui.PostMessage(window, win32con.WM_CLOSE, 0, 0)


def get_window_name():
    window = win32gui.GetForegroundWindow()
    return win32gui.GetWindowText(window)