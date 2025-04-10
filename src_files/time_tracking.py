import win32gui
import time

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