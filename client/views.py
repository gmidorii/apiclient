from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import urllib
from urllib import parse,request
from cms.models import Domain,ConvertParam
from urllib.error import URLError

def input_url(request):
    return render(request, 'client/input_url.html')

def form_url(request):
    parse_url = parse.urlparse(request.POST['access_url'])

    domains = Domain.objects.all()
    parsed_ip = parse_url.netloc
    for domain in domains:
        if parsed_ip.find(domain.name) != -1 :
            parsed_ip = domain.ip
            break

    convert_params = ConvertParam.objects.all()
    parsed_params = parse.parse_qs(parse_url.query)
    for convert_param in convert_params:
        if convert_param.key in parsed_params:
            # initialize
            del parsed_params[convert_param.key][:]
            parsed_params[convert_param.key].append(convert_param.value)

    query_map = dict()
    for key in parsed_params.keys():
        query_map[key] = parsed_params[key][0]

    url = parse.urlunparse((parse_url[0],
                            parsed_ip,
                            parse_url[2],
                            parse_url[3],
                            parse.urlencode(query_map),
                            parse_url[5]))

    json = url + "\n"
    print("[DEBUG]:" + json)
    try:
        result = urllib.request.urlopen(url)
        json += result.read().decode("utf-8")
    except URLError as e:
        json += "{'error': '接続できませんでした'}"

    return HttpResponse(json, content_type='application/json; charset=UTF-8')
