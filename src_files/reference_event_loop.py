"""This file is for reference only, as it contains an early
iteration of the implementation of the main event loop"""

import time
from datetime import datetime, timezone

from src_files.calendars import Calendar
from src_files.events import Event
from src_files.time_tracking import get_window_name, on_topic_reminder


def event_loop(event: Event, user_calendar: Calendar) -> int:
    """This will be run whenever a session is begun"""

    initial_time = time.time()
    event_details = {
        "start": {"datetime": datetime.now(timezone.utc).replace(microsecond=0).isoformat()},
        "summary": f"{event.action_type} {event.name}",
    }
    paused_time = 0
    time_elapsed = 0

    # GUI Stuff probably

    # Main event loop
    event_running = True
    while event_running:

        # Checks to make sure the user is on topic
        window = get_window_name()
        if window not in event.whitelist:
            temp_time = time.time()
            on_topic_reminder(event)
            paused_time += time.time() - temp_time

        # Calculates elapsed time, can be displayed to user
        time_elapsed = initial_time - paused_time

    # After the main event loop ends
    event_details.update(
        {"end": {"dateTime": datetime.now(timezone.utc).replace(microsecond=0).isoformat()}}
    )

    # Ask user if they want to add a description.
    desc = input(
        "Type a description for your event, e.g. subjects studied. Press enter for no description\n"
    )
    if desc:
        event_details.update({"description": desc})

    user_calendar.create_event(event_details)
    return time_elapsed
