from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm 
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')

    else:
        form = UserCreationForm()
        
    context = {'form': form}
    return render(request, 'register/register.html', context)



