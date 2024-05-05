from django.shortcuts import render, redirect
from . import models
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .coreutils import cf_integration, generate_diplomo
# from json import loads
# from django.http.response import JsonResponse


def main(request):
    users = models.User.objects.all()
    competizions = models.Competition.objects.all()[:3]

    for competizion in competizions:
        date = competizion.start_time.strftime('%d.%m.%Y')
        time = competizion.start_time.strftime('%H:%M')
        competizion.start_time = competizion.start_time.strftime('%d.%m.%Y в %H:%M')
        competizion.end_time = competizion.end_time.strftime('%d.%m.%Y в %H:%M')
        competizion.description = date
        competizion.created = time

    context = {'users': users, 'competitions': competizions}
    return render(request, 'base/main.htm', context=context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('main')

    form = forms.CustomUserCreationForm

    if request.method == 'POST' and "login_btn":
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        # noinspection PyBroadException
        try:
            login(request, user)
            return redirect('main')
        except BaseException:
            messages.error(request, "Email address or password is incorrect")

    if request.method == 'POST' and "reg_btn":
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            form.save()
            login(request, user)
            return redirect('main')
        else:
            messages.error(request, "Your password is weak or Fields are filled incorrectly")

    context = {'form': form}
    return render(request, 'base/login.htm', context=context)


@login_required(login_url='login')
def logout_page(request):
    logout(request)
    return redirect('main')


def competition(request):
    competitions = models.Competition.objects.all()

    for competition in competitions:
        date = competition.start_time.strftime('%d.%m.%Y')
        time = competition.start_time.strftime('%H:%M')
        competition.start_time = competition.start_time.strftime('%d.%m.%Y в %H:%M')
        competition.end_time = competition.end_time.strftime('%d.%m.%Y в %H:%M')
        competition.description = date
        competition.created = time

    context = {'competitions': competitions}
    return render(request, 'base/competition.htm', context=context)


def profile(request):
    user = models.User.objects.get(id=request.user.id)

    context = {'data': cf_integration(user.codeforce)}
    return render(request, 'base/profile.htm', context=context)


def edit_profile(request):
    user = models.User.objects.get(id=request.user.id)
    form = forms.UserEditForm(request.POST or None, instance=user)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('profile')

    context = {'form': form}
    return render(request, 'base/edit_profile.htm', context=context)


def monitor_unique(request, pk):
    competitionX = models.Competition.objects.get(id=pk)
    unique_history = models.History.objects.filter(competition=competitionX)

    competitionX.start_time = competitionX.start_time.strftime('%d.%m.%Y в %H:%M')
    competitionX.end_time = competitionX.end_time.strftime('%d.%m.%Y в %H:%M')

    lastIndexHist = len(unique_history)
    for hist in unique_history:
        hist.updated = hist.updated.strftime('%d.%m.%Y в %H:%M')
        hist.created = lastIndexHist
        lastIndexHist = lastIndexHist - 1

    context = {'competition': competitionX, 'history': unique_history}
    return render(request, 'base/monitor.htm', context=context)


def codeforce(request):
    user = models.User.objects.get(id=request.user.id)

    if request.method == 'POST':
        try:
            user.codeforce = request.POST.get('name_nick')
            user.save()
            return redirect('profile')
        except BaseException:
            raise redirect('main')


def task(request, pk):
    task_ = models.Tasks.objects.get(id=pk)

    context = {'task': task_}
    return render(request, 'base/single_task.htm', context=context)


def task_log(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        # competition_id = models.Competition.objects.get(pk=task_id) # fixme

        models.History.objects.create(
            text=request.POST.get('text'),
            # competition=models.Competition.objects.get(pk=competition_id.id), # fixme
            task=models.Tasks.objects.get(id=task_id),
            user=models.User.objects.get(id=request.user.id)
        )

    return redirect('competition')
