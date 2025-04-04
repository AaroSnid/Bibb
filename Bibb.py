import win32gui
import time

#This is to designate different "tasks" or study topics. Defininately adding more variables and methods.
class Event:

    def __init()__(self, name, action_type, blacklist):
        self.name = name
        self.action_type = action_type
        self.blacklist = blacklist

    def __str()__():
        print(action_type + " " + name)

    def set_time_goal(goal, duration):
        self.goal_time = goal
        self.goal_period = duration

    def update_blacklist(item, state)
        if "remove" in state:
            blacklist.remove(item)
        else:
            blacklist.add(item)

#This will be ran whenever a session is begun
def event_loop(Event):
    initial_time = time.time()

    #GUI Stuff probably

    while():
        window = Event.get_window_name()
        if window in Event.blacklist:
            #function to handle reminder

    time_spent = time.time() - initial_time
    

#Returns the name of the window that the user is on
def get_window_name():
    window = win32gui.GetForegroundWindow()
    return win32gui.GetWindowText(window)
