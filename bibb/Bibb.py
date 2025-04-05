import win32gui
import time

def main():
    pass


if __name__ == "main":
    main()

#This is to designate different "tasks" or study topics. Defininately adding more variables and methods.
class Event:

    def __init__(self, name, action_type, whitelist):
        self.name = name                # e.g. “Calculus”
        self.action_type = action_type  # e.g. “Studying”
        self.whitelist = whitelist      # Set of permitted applications

    #This will probably never be ran
    def __str__(self):
        return (self.action_type + " " + self.name)

    #Sets a time spent goal per period, e.g. 5h/week
    def set_time_goal(self, goal, duration):
        self.goal_time = goal
        self.goal_period = duration

    #Adds/Removes an item to/from the application whitelist
    def update_whitelist(self, item, state):
        if "remove" in state:
            whitelist.remove(item)
        elif "add" in state:
            whitelist.add(item)

#Returns the name of the window that the user is on
def get_window_name():
    window = win32gui.GetForegroundWindow()
    return win32gui.GetWindowText(window)

#Called when user is not on topic, and used to select action
def on_topic_reminder(Event):
    window = get_window_name()

    #Replace with GUI element
    print(f"\n Shouldn't you be {Event.action_type} {Event.name} right now? \n")
    user_input = int(input("1: Add to whitelist \n 2: Exit \n"))

    #There is no validation here since these will be GUI buttons in the future, but this will do for now
    if user_input == 1:
        Event.update_whitelist(window, "add")
    elif user_input == 2:
        win32gui.PostMessage(window, win32con.WM_CLOSE, 0, 0)

    #Close GUI elements

#This will be ran whenever a session is begun
def event_loop(Event):
    initial_time = time.time()
    paused_time = 0
    
    #GUI Stuff probably

    #Main event loop
    event_running = True
    while(event_running):

        #Checks to make sure the user is on topic
        window = get_window_name()
        if window not in Event.whitelist:
            temp_time = time.time()
            on_topic_reminder(Event)
            paused_time += (time.time() - temp_time)

        #Calculates elapsed time, can be displayed to user
        time_elapsed = initial_time - paused_time
        
    else:
        #Add calendar API call here
        pass
