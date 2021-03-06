from django.shortcuts import render


def homepage(request):
    return render(request, 'index.html')


def profile(request):
    user = request.user
    profile_object = user.profile
    return render(request, 'profile.html', {'profile': profile_object})