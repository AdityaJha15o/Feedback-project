from django.shortcuts import render, redirect, get_object_or_404
from .models import Feedback
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# HOME (protected)
@login_required
def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Feedback.objects.create(name=name, email=email, message=message)
        return redirect('home')

    feedbacks = Feedback.objects.all().order_by('-id')
    return render(request, 'home.html', {'feedbacks': feedbacks})


# DELETE
@login_required
def delete_feedback(request, id):
    fb = get_object_or_404(Feedback, id=id)
    fb.delete()
    return redirect('home')


# EDIT
@login_required
def edit_feedback(request, id):
    fb = get_object_or_404(Feedback, id=id)

    if request.method == "POST":
        fb.name = request.POST.get('name')
        fb.email = request.POST.get('email')
        fb.message = request.POST.get('message')
        fb.save()
        return redirect('home')

    return render(request, 'edit.html', {'fb': fb})


# LOGIN
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


# LOGOUT
def user_logout(request):
    logout(request)
    return redirect('login')
