from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import urllib
from urllib import parse,request
from cms.models import Domain,ConvertParam

def input_url(request):
    return render(request, 'client/input_url.html')

def form_url(request):
    url = request.POST['access_url']
    parse_url = parse.urlparse(url)

    domains = Domain.objects.all()
    parsed_ip = parse_url.netloc
    for domain in domains:
        if(parsed_ip == domain.name):
            parsed_ip = domain.ip
            break

    params = ConvertParam.objects.all()
    parsed_params = parse.parse_qs(parse_url.query)
    for param in params:
        if len(parsed_params[param.param]) != 0:
            # パラメータ重複に未対応
            del parsed_params[param.param][:]
            parsed_params[param.param].append(param.value)

    query_map = dict()
    for key in parsed_params.keys():
        query_map[key] = parsed_params[key][0]

    url = "http://" + parsed_ip + parse_url.path + "?" + parse.urlencode(query_map)

    json = url + "\n"
    print("[DEBUG]:" + json)
    with urllib.request.urlopen(url) as res:
        json += res.read().decode("utf-8")

    return HttpResponse(json, content_type='application/json; charset=UTF-8')
