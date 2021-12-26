import requests

from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST


@login_required
def logout_user(request):
    logout(request)
    redirect_url = '/login/'
    response = redirect(redirect_url)

    if not request.user.is_authenticated:
        for cookie in request.COOKIES:
            response.delete_cookie(cookie)
        request.session.flush()

    return response


@login_required
def profile(request):
    return render(request, 'account/profile.html')


@require_POST
@login_required
def update_profile(request):
    if request.is_ajax:
        user = request.user
        data = request.POST
        for key in data.keys():
            setattr(user, key, data[key])

        user.save()
        return JsonResponse({'data': None}, status=200)

    return JsonResponse({'error': 'There occurred an error'}, status=500)

