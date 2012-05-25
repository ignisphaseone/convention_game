from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'usercontact.views.index'),
    url(r'^login$', 'usercontact.views.login'),
    url(r'^register$', 'usercontact.views.register'),
    url(r'^user/$', 'usercontact.views.userinfo'),
    url(r'^admin', include(admin.site.urls)),
)

urlpatterns += patterns('game_system.views',
    url(r'^game/$', 'gamelist'),
    url(r'^game/(?P<game_id>\d+)$', 'game'),
    url(r'^game/(?P<game_id>\d+)/rules$', 'rules'),
    url(r'^player/(?P<player_id>\d+/$', 'player'),
    url(r'^info/$', 'myhelp')
)