from django.shortcuts import render, HttpResponse
from servicios.models import Servicio


def home(request):
	return render(request, "ProyectoWebApp/home.html")


# views.py

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')  # Cambia 'home' por la URL a la que quieres redirigir al usuario después del registro
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # Puedes cambiar 'login' por la URL a la que quieres redirigir después del registro
    template_name = 'registration/register.html' 




