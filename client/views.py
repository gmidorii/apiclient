from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import urllib
from cms.models import Domain

def input_url(request):
    return render(request, 'client/input_url.html')

def form_url(request):
    parse_url = urllib.parse.urlparse(request.POST['access_url'])
    # query = parse.parse_qs(parse_url.query)

    domains = Domain.objects.all()
    parsed_ip = ""
    for domain in domains:
        if(parse_url.netloc == domain.name):
            # parse_url.netloc = domain.name
            parsed_ip = domain.ip

    url = request.POST['access_url']
    if len(parsed_ip) != 0:
        url = "http://" + parsed_ip + parse_url.path + "?" + parse_url.query
        print(url)

    json = "{'eroor' : '404' }"
    with urllib.request.urlopen(url) as res:
        json = res.read().decode("utf-8")

    return HttpResponse(json, content_type='application/json; charset=UTF-8')
