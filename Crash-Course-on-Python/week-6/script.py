"""
Imagine that you're an IT specialist working in a medium-sized company, your manager wants to create a daily report that
tracks the use of machines. Specifically, she wants to know which users are currently connected to which machines, it's
your job to create the report. In your company, there's a system that collects every event that happens on the machines
on the network. Among the many events collected it records each time a user logs in or out of a computer.
With this information, we want to write a script that generates a report of which users are logged in to which machines
at that time. Before we jump into solving that problem, we need to know what information we'll use as input and what
information we'll have as output. We can work this out by looking at the rest of the system where our script will live.
In our report scenario, the input is a list of events, each event is an instance of the event class. An event class
contains the date when the event happened, the name of the machine where it happened, the user involved, and the event
type. In this scenario, we care about the login and logout event type. All right, that's good to know. But we need to
know exact names of the attributes, otherwise, we won't be able to access them. The attributes are called date, user,
 machine, and type. The event types are strings and the ones we care about are login and logout. With that we should
 have enough information about the input of our script. Our script will receive a list of event objects and we'll access
 the events attributes. We'll then use that information to know if a user is currently logged into a machine or not.
 Let's talk about the output. We want to generate a report that lists all the machine names and for each machine, lists
 of the users that are currently logged in. We then want this information printed on the screen. We've been tasked with
 generating a report and we can decide exactly how we want that report to look. One option would be to print the name of
 the machine at the beginning of the line and then list the current users on separate lines and indent it to the right,
 or we could print the machine name followed by a colon and then the usernames separated by commas all in the same line,
 and we can probably come up with something even more fancy. When formatting a report, it's easy to get caught up in the
 making it look good part. I've fallen into that trap but what really matters is how well the script solves the problem.
 So it's better to first focus on making the program work. You can always spend time making the report look nice later.
 Let's keep it simple for now and we'll go with the approach of printing the machine name followed by all the current
 users separated by commas. Okay, we now have a pretty good idea of what we need to do. We've identified our problem
 statement which is we need to process a list of event objects using their date, type, machine, and user attributes to
 generate a report that lists all users currently logged into the machines. We're off to a great start. The next step
 we're going to do is some research to work out how to best actually do this.
"""



"""
Hello, coders! Below we have code similar to what we wrote in the last video. Go ahead and run the following cell that
defines our get_event_date, current_users and generate_report methods.
"""

def get_event_date(event):
  return event.date

def current_users(events):
  events.sort(key=get_event_date)
  machines = {}
  for event in events:
    if event.machine not in machines:
      machines[event.machine] = set()
    if event.type == "login":
      machines[event.machine].add(event.user)
    elif event.type == "logout":
      machines[event.machine].remove(event.user)
  return machines

def generate_report(machines):
  for machine, users in machines.items():
    if len(users) > 0:
      user_list = ", ".join(users)
      print("{}: {}".format(machine, user_list))


class Event:
  def __init__(self, event_date, event_type, machine_name, user):
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user


events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]

users = current_users(events)
print(users)

generate_report(users)
