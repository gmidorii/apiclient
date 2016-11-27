from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import urllib
from cms.models import Domain

def input_url(request):
    return render(request, 'client/input_url.html')

def form_url(request):
    url = request.POST['access_url']
    parse_url = urllib.parse.urlparse(url)

    domains = Domain.objects.all()
    parsed_ip = ""
    for domain in domains:
        if(parse_url.netloc == domain.name):
            parsed_ip = domain.ip
            break

    if len(parsed_ip) != 0:
        url = "http://" + parsed_ip + parse_url.path + "?" + parse_url.query
        # request url
        print(url)

    json = "{'eroor' : '404' }"
    with urllib.request.urlopen(url) as res:
        json = res.read().decode("utf-8")

    return HttpResponse(json, content_type='application/json; charset=UTF-8')
