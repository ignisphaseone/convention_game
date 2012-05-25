What is this?

It's a convention game, a piece of software that helps people run big
events using real people! Infection, zombies, assassins, you name it, this
software is designed to help people run those games. Still working out all
the details on the specific nitty-gritty main structure of everything.

Installing/Running/Testing

This code's been written for Python 2.7.3, and Django 1.4
If you're not using those, no promises for you.

I did my best to rejigger the "settings.py" file so it uses relative paths
instead of absolute paths, to make life easier for collaborating teammates.
(Hi teammates!)

I'm going to make use of Github's wiki too, since a lot of the discussion
and/or decisions and such can be made there.

Questions and Details

It's unlikely anybody will run the software using sqlite3, although I guess
there isn't anything wrong with doing that. It's the easiest way to use a
testing database since there's little to no setup involved. Just make sure
to sync your databases before doing anything, since the database file itself
is excluded from the commits. It'll be hard to test if you don't have a
database file somewhere! =P

Licensing

This software is licensed under the terms of GNU GPL v3,
<http://www.gnu.org/licenses/gpl.html>

I'm not going to re-type the whole thing in here yet, but yeah. It's free
and stuff. I'm hoping for a "business model" to copy our beloved Github,
people can set it up themselves if they like, but hopefully better and more
convenient to use a service we set up.