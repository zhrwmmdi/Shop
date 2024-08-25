from django.db.models import Sum
from django.http import Http404, JsonResponse

from app.models import Order


def checkout(request, order_pk):
    try:
        order = Order.objects.get(pk=order_pk)
    except Order.DoesNotExist:
        raise Http404

    total_price = Sum(item.product.price * item.quantity for item in order.items.all)
    return JsonResponse({'total_price', total_price})



