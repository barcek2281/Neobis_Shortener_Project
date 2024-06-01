from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view, permission_classes

from .serializers import UrlSerializer


def index(request):
    return render(request, 'index.html')


@api_view(['POST'])
def create(request):
    url = request.POST['link']
    new_url = Url(link=url)
    if new_url.is_valid():
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=url, uuid=uid, )
        new_url.save()
        return JsonResponse({'valid': True, 'link': new_url.uuid})
    return JsonResponse({'valid': False})


def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect(url_details.link)