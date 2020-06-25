from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth import login, authenticate
from accounts.forms import RegistrationForm
from django.urls import reverse_lazy


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            account = authenticate(email=email,username= username, password=password)
            login(request, account)
            return redirect("index.html")
            
        else:
            context["registration_form"] = form

    else:
        form = RegistrationForm()
        context["registration_form"] = form
    return render(request, "account/signup.html", context)
 