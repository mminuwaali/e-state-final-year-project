from . import forms
from django.contrib import auth, messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group, User


def signout_view(request):
    auth.logout(request)
    return redirect(request.GET.get("next", "/"))


def signup_view(request):
    if request.method == "POST":
        role = request.POST.get("role")
        form = forms.RegisterForm(request.POST)

        if form.is_valid():
            user: User = form.save()

            group, _ = Group.objects.get_or_create(name=role)
            user.groups.add(group)

            messages.success(request, "Account created successfully")
            return redirect("account:signin-view")

        [messages.error(request, i[0]) for i in form.errors.values()]
        return redirect("account:signup-view")

    return render(request, "account/signup.html")


def signin_view(request):
    if request.method == "POST":
        user = auth.authenticate(
            request,
            username=request.POST.get("username"),
            password=request.POST.get("password"),
        )

        if user:
            auth.login(request, user)
            return redirect("landing:index-view")

        messages.error(request, "Invalid credentials")
        return redirect("account:signin-view")

    return render(request, "account/signin.html")
