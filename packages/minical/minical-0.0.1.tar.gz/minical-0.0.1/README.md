A simple calendar driven by text files, with an optional web UI.

You can add/edit/remove events using the text tools of your choice, or use the scripts or web UI.

Events look something like:

```
$ cat events/medical_procedure

name: medical_procedure
date: 2020-10-09
start_time: 15:00
duration_minutes: 1
notes: address goes here
recurs: monthly
recurs_until: 2099-01-01
skip_dates: 2020-11-09,2021-03-09
```

To remove an event, use "rm", or the web UI.

## Basic command examples
```
# This uses Flask's built-in server. See further below on using gunicorn
# Use "src.minical" if running from project root and not an installed package
MINICAL_PORT=5132 python -m minical.app

# List upcoming events
python -m minical.whats_next -s bday -a

# Point to events living somewhere else.
# This is one way to maintain separate calendars
MINICAL_EVENTS_DIR=/some/path/events python -m minical.whats_next

# There is an "entrypoint" if you install the package, just a CLI shorthand
# Equivalent to `python -m minical.app`
MINICAL_PORT=5132 minical-web
```

The "whats_next" CLI script shows something like:

```
2021-05-29 (Sun), 01:01, friend_drinks (in 3 days)
2021-06-03 (Fri), 17:00, some_wedding (in 8 days)
2021-06-06 (Mon), 15:00, dr_foo_appt (in 11 days)
2022-05-17 (Wed), 01:01, some_birthday (in 356 days)
2022-08-01 (Tue), 01:01, award_ceremony (in 432 days)
2023-05-17 (Fri), 01:01, some_birthday (in 722 days)
```

## Building the package

WIP - haven't done this in a long time
```
# Make an env wherever, outside of project dir,
# to make sure you're not importing files from same dir
python -m venv minical_build_test
source minical_build_test/bin/activate
# This is a tool from pypa
pip install build
# Go back into project dir with the setup.cfg. This command will make a 'dist' folder
python -m build
# Install the thing from the dist folder
pip install file:///home/.../dist/path/to/thing.tar.gz
```

## Running with gunicorn

```
# If installed
gunicorn -b 127.0.0.1:5132 minical.app:app
# If working with source
gunicorn -b 127.0.0.1:5132 src.minical.app:app
```

## Other features
There are none! No reminders or sharing. You shouldn't be so busy!
