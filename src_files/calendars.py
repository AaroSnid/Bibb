"""Logic for interacting with calendar APIs."""

import datetime
import os.path
from abc import ABC

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from O365 import Account, FileSystemTokenBackend


class Calendar(ABC):
    """Only used as a parent for easy access to methods."""

    def __init__(self):
        self.credentials = None

    def get_credentials(self):
        """Authenticate the application to access calendar data on behalf of the user."""

    def get_events(self, amount: int) -> list:
        """Fetches events from the calendar api."""

    def create_event(self, event_details: dict):
        """Makes a request to the calendar API to create an event."""


class GoogleCalendar(Calendar):
    """For users that configure for Google Calendar"""

    def get_credentials(self):
        """The base code for this function comes from the Python Quickstart at
        https://developers.google.com/workspace/calendar/api/quickstart/python,
        published under Apache 2.0 license"""
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
            with open("token.json", "w", encoding="utf-8") as token:
                token.write(self.credentials.to_json())

    def get_events(self, amount : int) -> list:
        """Gets the next {amount} events in the users calendar"""

        service = build("calendar", "v3", credentials=self.credentials)

        now = datetime.datetime.now(tz=datetime.timezone.utc).isoformat()
        events_result = (
            service.events()  # pylint: disable=no-member
            .list(
                calendarId="primary",
                timeMin=now,
                maxResults=amount,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
        events = events_result.get("items", [])
        return events

    def create_event(self, event_details: dict):
        """Creates an event based on the dict event_details"""

        service = build("calendar", "v3", credentials=self.credentials)

        event = {
            "summary": event_details["summary"],
            "description": event_details["description"],
            "start": {
                "dateTime": event_details["start"],
                "timeZone": "UTC",
            },
            "end": {
                "dateTime": event_details["end"],
                "timeZone": "UTC",
            },
        }
        # pylint: disable=no-member
        event = service.events().insert(calendarId="primary", body=event).execute()

class OutlookCalendar(Calendar):
    """For users that configure for Outlook Calendar"""

    def get_credentials(self):

        # Defines the API credentials, and sets up automatic token reading/refresh
        api_credentials = ('286c9124-1061-4b2c-afe0-20ee80d9301d', '')
        token_backend = FileSystemTokenBackend(token_path='.', token_filename='o365_token.txt')

        # Passes relevant credentials, and attempts to authenticate with the token.
        account = Account(api_credentials, token_backend=token_backend)

        # Prompts authentication if token auth was unsuccessful
        if not account.is_authenticated:
            account.authenticate(scopes=['basic', 'calendar_all'])

        self.credentials = account

    def get_events(self, amount : int) -> list:
        # Get the calendar and schedule
        schedule = self.credentials.schedule()
        calendar = schedule.get_default_calendar()

        # Required to define a time range, 30 days should be enough
        start = datetime.datetime.now()
        end = start + datetime.timedelta(days=30)

        # Get events in that time range
        query = calendar.new_query('start').greater_equal(start)
        query.chain('and').on_attribute('end').less_equal(end)

        return calendar.get_events(query=query, limit=amount)

    def create_event(self, event_details:dict):

        # Sets the calendar that the event will be created in
        # Could be updated to allow user to select a specific calendar
        schedule = self.credentials.schedule()
        calendar = schedule.get_default_calendar()

        # Create a new event
        event = calendar.new_event()

        # Set the event parameters
        event.subject = event_details['summary']
        event.body = event_details['description']
        event.start = datetime.datetime.fromisoformat(event_details['start'])
        event.end = datetime.datetime.fromisoformat(event_details['end'])

        # Creates the event in the users calendar
        event.save()