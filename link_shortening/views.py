from django.shortcuts import render, redirect
from .models import Url


def create_url(request):
    if request.method == "POST":
        full_url = request.POST.get('full_url')
        obj = Url.create(full_url)
        return render(request, 'link_shortening/home.html', {
            'full_url': obj.full_url,
            'short_url': request.get_host() + '/link_shortening/' + obj.short_url
        })
    return render(request, 'link_shortening/home.html')


def route_to_url(request, key):
    try:
        obj = Url.objects.get(short_url=key)
        return redirect(obj.full_url)
    except:
        return redirect(create_url)
