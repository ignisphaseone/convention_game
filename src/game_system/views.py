from game_system.models import Action, Game
from usercontact.models import UserProfile
from django.core.mail import send_mail
from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context, loader, RequestContext

# Create your views here.
def myhelp(request):
    return render_to_response('myhelp.html', {})

def player(request, player_id):
    return render_to_response('placeholder.html', {})
    
def game(request, game_id):
    return render_to_response('gameinfo.html', {})
    if request.method == 'POST':
        g = Game(name=request.POST['game_name'])
        g.save()
    elif request.method == 'GET':
        g = get_object_or_404(Game, pk=game_id)
    return render_to_response('game.html', {'game':g},
                                  context_instance=RequestContext(request))

def gamelist(request):
    return render_to_response('gamelist.html', {})
    next_id = Game.objects.count() + 1
    return render_to_response('gamelist.html', {'next_id':next_id},
                              context_instance=RequestContext(request))

def rules(request, game_id):
    return render_to_response('gamerules.html', {})