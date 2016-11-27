from django.shortcuts import render, get_object_or_404, redirect


def input_url(request):
    return render(request, 'client/input_url.html')

def form_url(request):
    url = request.POST['access_url']
    return redirect('input_url')
