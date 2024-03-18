from django.shortcuts import render
from django.http import HttpResponse
from members_test_fx.models import Members
from members_test_fx.models import Games

from members_test_fx.forms import FormTest, GamesForm

from django.core.mail import send_mail

from django.shortcuts import redirect

# Create your views here.

def hello(request):
    tab_members = Members.objects.all()
    tab_games = Games.objects.all()
    return render(request, "members_test_fx/hello.html", {"tab_members": tab_members, "tab_games": tab_games})
    #return HttpResponse(f"<h1>{tab_members[0].name} joue une {tab_games[1].title}</h1>")

def subscribe(request):
    tab_members = Members.objects.all()
    tab_games = Games.objects.all()
    print("Le request :", request.POST)
    if request.method == 'POST':
        form = FormTest(request.POST)
        if form.is_valid() :
            send_mail(subject=f'Message', message=f'hello {form.cleaned_data["name"]} ', from_email=form.cleaned_data['email'], recipient_list=['fx.coindreau@gmail.com'])
            return redirect('email-sent')
    else:
        form = FormTest()
    return render(request, "members_test_fx/subscribe.html", {"POST": request.POST, "form": form, "tab_members": tab_members, "tab_games": tab_games})


def hello_details(request, id):
    mem = Members.objects.get(id=id)
    return render(request, 'members_test_fx/hello_details.html', {'mem': mem})

def email_sent(request):
    return HttpResponse(f"<h1>E mail bien sent.</h1>")

def game_create (request):
    if request.method == 'GET':
        form = GamesForm()
    elif request.method == 'POST':
        form = GamesForm(request.POST)
        if form.is_valid():
            Game = form.save()
        return redirect('hello')
    return render(request, "members_test_fx/game_create.html", {'form' : form})

def game_change (request, id):
    game = Games.objects.get(id=id)
    if request.method == 'POST':
        form = GamesForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('hello')
    else:
        form = GamesForm(instance=game)
    return render(request, "members_test_fx/game_change.html" ,{'form' : form})

def game_delete (request, id):
    game = Games.objects.get(id=id)
    if request.method == 'POST':
        game.delete()
        return redirect('hello')


    return render(request, "members_test_fx/game_delete.html", {'game' : game})