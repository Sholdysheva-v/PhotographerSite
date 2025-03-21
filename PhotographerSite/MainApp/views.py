from django.http import HttpResponse, Http404, HttpResponseNotFound
from datetime import datetime
from django.shortcuts import redirect

def index(request):
    return HttpResponse("Здесь можно будет посмотреть фотоработы")

def order(request, order_id):
    if order_id > 1000:
        raise Http404()
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Заявка фотосессии</h1><p>ID: {order_id}</p>")

def date_order(request, date):
    date_error = '2025-03-20'
    if date < datetime.strptime(date_error, '%Y-%m-%d'):
        return redirect('/')
    return HttpResponse(f"<h1>Фотосессия назначена на {date}</h1>")

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Такой страницы не существует</h1>')

