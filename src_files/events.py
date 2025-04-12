import calendars
import time_tracking

from datetime import datetime, timezone
import time

class Event:
    """This is to designate different "tasks" or study topics. Definitely adding more variables and methods."""

    def __init__(self, name: str, action_type: str, whitelist: set, *args):
        self.name = name  # e.g. “Calculus”
        self.action_type = action_type  # e.g. “Studying”
        self.whitelist = whitelist  # Set of permitted applications

        # Args to be used if class is made from database information.
        if args:
            self.goal_period = args[0]
            self.goal_time = args[1]
            self.whitelist = args[2]
            self.time_spent = args[3]
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


def event_loop(event : Event, user_calendar : calendars.Calendar):
    """This will be run whenever a session is begun"""

    initial_time = time.time()
    event_details = {
        "start": {
            "datetime": datetime.now(timezone.utc).replace(microsecond=0).isoformat()
        },
        "summary": f"{event.action_type} {event.name}"
    }
    paused_time = 0

    # GUI Stuff probably

    # Main event loop
    event_running = True
    while event_running:

        # Checks to make sure the user is on topic
        window = time_tracking.get_window_name()
        if window not in event.whitelist:
            temp_time = time.time()
            time_tracking.on_topic_reminder(Event)
            paused_time += (time.time() - temp_time)

        # Calculates elapsed time, can be displayed to user
        time_elapsed = initial_time - paused_time

    # When the main event loop ends
    else:
        event_details.update({'end': {'dateTime': datetime.now(timezone.utc).replace(microsecond=0).isoformat()}})

        # Ask user if they want to add a description.
        desc = input("Type a description for your event, e.g. subjects studied. Press enter for no description\n")
        if desc:
            event_details.update({'description': desc})

        user_calendar.create_event(event_details)
