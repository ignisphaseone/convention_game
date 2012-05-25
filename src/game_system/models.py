from django.db import models

class Game(models.Model):
    GAME_STATUS_OPTIONS = {}
    name = models.CharField("Game Name", max_length = 50, unique=True)
    status = models.CharField(max_length = 15)

class Player(models.Model):
    def user(self):
        return self.userprofile.user
    def myid(self):
        return self.userprofile.id
    # A Foreignkey to a User object, and its corresponding Userprofile object.
    userprofile = models.ForeignKey('usercontact.UserProfile', unique=True)
    game = models.ManyToManyField(Game)

# Create your models here.

# Action has a few things:
# --Source: Player that owns the action.
# --Type: What action that indicates.
# --Data: what data the action stores.
class Action(models.Model):
    def parse(self):
        # Parse takes in data stored in an Action, and understands how to both
        # analyze it, display it, etc.
        return 'This is a parsed action.'
    game = models.ForeignKey(Game)
    owner = models.ForeignKey(Player)
    time = models.DateTimeField('Timestamp', auto_now_add = True)
    data = models.CharField(max_length = 200)