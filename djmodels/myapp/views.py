from django.http import HttpResponse
from django.shortcuts import render
from myapp.models import User

from myapp.forms import UserForm, NameForm
from django.shortcuts import redirect  


def hello(request):

    return HttpResponse(f"""
        <h1>Hello Django !</h1>
""")


def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « User » et la sauvegarder dans la db
            user = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('user-detail', user.id)

    else:
        form = UserForm()

        return render(request,
            'myapp/user_create.html',
            {'form': form})





def user_list(request):  # renommer la fonction de vue
   users = User.objects.all()
   return render(request,
           'myapp/user_list.html',  # pointe vers le nouveau nom de modèle
           {'users': users})

def user_detail(request, id):
  user = User.objects.get(id=id)  # nous insérons cette ligne pour obtenir le Band avec cet id
  return render(request,
          'myapp/User_detail.html',
          {'user': user}) # nous mettons à jour cette ligne pour passer le groupe au gabarit


def session(request):
    if request.method == 'GET':
        
        form = NameForm()

        if "your_name" in request.session:   
            your_name = request.session["your_name"]
        else:
            your_name = "pas de nom enregistré" 

        return render(request,
            'myapp/session.html',
            {'form': form,"your_name" : your_name})

    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["your_name"]:
                request.session["your_name"] = form.cleaned_data["your_name"]
            return redirect('session')
        else:
            print("formulaire non valide")
