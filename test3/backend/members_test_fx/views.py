from django.shortcuts import render
from django.http import HttpResponse
from members_test_fx.models import Members
from members_test_fx.models import Games

# Create your views here.

def hello(request):
    tab_members = Members.objects.all()
    tab_games = Games.objects.all()
    return render(request, "members_test_fx/hello.html", {"tab_members": tab_members, "tab_games": tab_games})
    #return HttpResponse(f"<h1>{tab_members[0].name} joue une {tab_games[1].title}</h1>")
