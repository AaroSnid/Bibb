import calendars.py
import time_tracking.py

import win32gui
import time

'''This is to designate different "tasks" or study topics. Defininately adding more variables and methods.'''


class Event:

    def __init__(self, name, action_type, whitelist):
        self.name = name  # e.g. “Calculus”
        self.action_type = action_type  # e.g. “Studying”
        self.whitelist = whitelist  # Set of permitted applications

    # This will probably never be ran
    def __str__(self):
        return (self.action_type + " " + self.name)

    # Sets a time spent goal per period, e.g. 5h/week
    def set_time_goal(self, goal, duration):
        self.goal_time = goal
        self.goal_period = duration

    # Adds/Removes an item to/from the application whitelist
    def update_whitelist(self, item, state):
        if "remove" in state:
            whitelist.remove(item)
        elif "add" in state:
            whitelist.add(item)


'''This will be ran whenever a session is begun'''


def event_loop(Event, Calendar):
    initial_time = time.time()
    event_details = {'start': {'dateTime': datetime.now(timezone.utc).replace(microsecond=0).isoformat()},
                     'summary': Event.action_type + ' ' + Event.name}
    paused_time = 0

    # GUI Stuff probably

    # Main event loop
    event_running = True
    while (event_running):

        # Checks to make sure the user is on topic
        window = get_window_name()
        if window not in Event.whitelist:
            temp_time = time.time()
            on_topic_reminder(Event)
            paused_time += (time.time() - temp_time)

        # Calculates elapsed time, can be displayed to user
        time_elapsed = initial_time - paused_time

    # When the main event loop ends
    else:
        event_details.update({'end': {'dateTime': datetime.now(timezone.utc).replace(microsecond=0).isoformat()}})

        # Ask user if they want to add a description, GUI pls
        desc = input("Type a description for your event, e.g. subjects studied. Press enter for no description\n")
        if desc:
            event_details.update({'description': desc})

        Calendar.create_event()
