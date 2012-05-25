The Con Game is a system of webpages, databases, and other such information
that allows players to gather and play offline games together.

The first part is registration. Players who wish to participate in a con game
only need to go to the website and register. Then, they can participate in any
con game that is run on the site.

The relevant databases and objects that involve this game are as follows:
--Users (Django provided)
--Userprofile (Custom, 1-to-1 Foreign with Users)

Any game that is run on the site needs the following databases:
--Players (1-to-1 foreign key with users)
--Actions