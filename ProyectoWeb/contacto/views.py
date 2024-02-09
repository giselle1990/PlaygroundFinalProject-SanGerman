from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage

def contacto(request):
    formulario_contacto = FormularioContacto()

    if request.method == "POST":
        formulario_contacto = FormularioContacto(data=request.POST)

        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            email = EmailMessage(
                "Mensaje desde App Django",
                f"El usuario con nombre {nombre} con la dirección {email} escribe lo siguiente:\n\n {contenido}",
                ["gisellesang@hotmail.com"],
                reply_to=[email],
            )

            try:
                email.send()
                return redirect("/contacto/?valido")
            except Exception as e:
                print(e)  # Imprime el error en la consola, para depuración
                return redirect("/contacto/?novalido")
    print(formulario_contacto)
    return render(request, "contacto/contacto.html", {'mi_Formulario': formulario_contacto})


    
                
            



