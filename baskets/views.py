from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from products.models import Product
from baskets.models import Basket


@login_required
def basket_add(request, product_id):

    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        baskets = baskets.first()
        baskets.quantity == 1
        baskets.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def basket_remove(request, id):
    Basket.objects.get(id=id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))