from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from datetime import datetime



def index(request):
    return render(request, 'index.html', {
        'title': 'Фотоуслуги',
        'current_year': datetime.now().year,
    })

def order(request, order_id):
    if order_id == 1:
        order_data = {
            'order_id': order_id,
            'order_exists': True,
            'order_date': '25.04.2025',
            'order_status': 'Фотографии в обработке',
            'delivery_address': 'г. Новосибирск, ул. Фрунзе, д. 19',
            'items': [
                {'name': 'Фотосессия питомца', 'quantity': 1, 'price': 4000},
                {'name': 'Ландшафтная съемка"', 'quantity': 1, 'price': 2000},
            ],
            'total_price': 6000,
        }
    else:
        raise Http404("Заказ не найден")
    return render(request, 'order.html', order_data)


def date_delivery(request, year, month, day):
    delivery_date = datetime(year, month, day)
    min_date = datetime(2023, 5, 10)  # Минимальная дата доставки
    
    if delivery_date < min_date:
        return redirect('index')
    
    return HttpResponse(f"Фотосъемка назначена на {day}.{month}.{year}")

def page_not_found(request, exception):
    return render(request, '404.html', {
        'error_message': str(exception)
    }, status=404)


