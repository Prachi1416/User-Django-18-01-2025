from django.shortcuts import render, redirect
from .forms import UserForm, User, ProfileForm, Profile
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='login_url')
def user_create_view(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('uretrive_url')
    template_name = 'user_app/user_create.html'
    context = {'form': form}
    return render(request, template_name, context)

@login_required(login_url='login_url')
def user_retrive_view(request):
    objs = User.objects.all()
    template_name = 'user_app/user_retrive.html'
    context = {'data': objs}
    return render(request, template_name, context)

def user_update_view(request, pk):
    obj = User.objects.get(id = pk)
    form = UserForm(instance=obj)
    if request.method == "POST":
        form = UserForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('uretrive_url')
    template_name = 'user_app/user_update.html'
    context = {'form': form}
    return render(request, template_name, context)

def user_delete_view(request, pk):
    obj = User.objects.get(id = pk)
    if request.method == "POST":
        obj.delete()
        return redirect('uretrive_url')
    template_name = 'user_app/user_delete.html'
    context = {'data': obj}
    return render(request, template_name, context)


@login_required(login_url='login_url')
def profile_create_view(request):
    form = ProfileForm()
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pretrive_url')
    template_name = 'user_app/profile_create.html'
    context = {'form': form}
    return render(request, template_name, context)

@login_required(login_url='login_url')
def profile_retrive_view(request):
    objs = Profile.objects.all()
    template_name = 'user_app/profile_retrive.html'
    context = {'data': objs}
    return render(request, template_name, context)

def profile_update_view(request, pk):
    obj = Profile.objects.get(id = pk)
    form = ProfileForm(instance=obj)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('pretrive_url')
    template_name = 'user_app/profile_update.html'
    context = {'form': form}
    return render(request, template_name, context)

def profile_delete_view(request, pk):
    obj = Profile.objects.get(id = pk)
    if request.method == "POST":
        obj.delete()
        return redirect('pretrive_url')
    template_name = 'user_app/profile_delete.html'
    context = {'data': obj}
    return render(request, template_name, context)



