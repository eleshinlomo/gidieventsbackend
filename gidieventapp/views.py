from django.shortcuts import render


def index(request):
    
    return render(request, 'home.html')

def add(request):
        value1 = int(request.GET["value1"])
        value2 = int(request.GET["value2"])
        res = value1 + value2
        return render(request, 'home.html', {'result': res, 'name': 'Guest', 'title': 'GidiEvent'})
