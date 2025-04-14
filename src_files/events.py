class Event:
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