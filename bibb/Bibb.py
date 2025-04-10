import win32gui
import time
import datetime
import os.path

from datetime import datetime, timezone
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

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

#Class that is only used as a parent for easy access for functions
class Calendar:

    def __init__(self):
        Self.credentials = None

    def get_credentials(self):
        pass

    def create_event(self):
        pass

#Class used by users that configure for Google Calendar
class GoogleCalendar(Calendar):

    def get_credentials(self):
        #The base code for this function comes from the Python Quickstart at https://developers.google.com/workspace/calendar/api/quickstart/python, published under Apatche 2.0 license
        scope = ["https://www.googleapis.com/auth/calendar"]

        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first time.
        if os.path.exists("token.json"):
            self.credentials = Credentials.from_authorized_user_file("token.json", scope)

        # If there are no (valid) credentials available, let the user log in.
        if not self.credentials or not self.credentials.valid:
            if self.credentials and self.credentials.expired and self.credentials.refresh_token:
                self.credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file("credentials.json", scope)
                self.credentials = flow.run_local_server(port=0)

            # Save the credentials for the next run
            with open("token.json", "w") as token:
                token.write(self.credentials.to_json())

    #Creates an event based on the dict event_details
    def create_event(self, event_details):
        service = build("calendar", "v3", credentials=creds)

        event = {
            'summary': event_details['summary'],
            'description': event_details['description'],
        'start': {
            'dateTime': event_details['start_time'],
            'timeZone': 'UTC',
        },
        'end': {
            'dateTime': event_details['end_time'],
            'timeZone': 'UTC',
        },
        }

        event = service.events().insert(calendarId='primary', body=event).execute()

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
def event_loop(Event, Calendar):
    initial_time = time.time()
    event_details = {'start_time' : datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
                     'summary' : Event.action_type + ' ' + Event.name}
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

    #When the main event loop ends
    else:
        event_details.update('end_time' : datetime.now(timezone.utc).replace(microsecond=0).isoformat())

        #Ask user if they want to add a description, GUI pls
        desc = input("Type a description for your event, e.g. subjects studied. Press enter for no description\n")
        if desc:
            event_details.update('description': desc)

        Calendar.create_event()