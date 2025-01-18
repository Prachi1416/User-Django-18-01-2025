from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    template_name = 'auth_app/register_form.html'
    context = {'form':form}
    return render(request, template_name, context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('unm')
        password = request.POST.get('upass')
        print(username, '----------', password)
        user = authenticate(username = username, password = password)
        print(f'user -----------> {user}')

        if user is not None:
            login(request, user)
            return redirect('pretrive_url')

    template_name = 'auth_app/login_form.html'
    context = {}
    return render(request, template_name, context)


def logout_view(request):
    logout(request)
    return redirect('login_url')