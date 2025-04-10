import datetime
import os.path

from abc import ABC
from datetime import datetime, timezone
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

'''Only used as a parent for easy access to methods.'''
class Calendar(ABC):

    def __init__(self):
        self.credentials = None

    def get_credentials(self):
        pass

    def create_event(self):
        pass

'''For users that configure for Google Calendar'''
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
        service = build("calendar", "v3", credentials=self.credentials)

        event = {
            'summary': event_details['summary'],
            'description': event_details['description'],
        'start': {
            'dateTime': event_details['start'],
            'timeZone': 'UTC',
        },
        'end': {
            'dateTime': event_details['end'],
            'timeZone': 'UTC',
        },
        }

        event = service.events().insert(calendarId='primary', body=event).execute()
