from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .box import Box
from .form import BoxAddProductForm

@require_POST
def box_add(request, product_id):
    box = Box(request)
    product = get_object_or_404(Product, id=product_id)
    form = BoxAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        box.add(product=product, quantity=cd['收藏数量'], update_quantity=cd['update'])
    return redirect('box:box_detail')


def box_remove(request, product_id):
    box = Box(request)
    product = get_object_or_404(Product, id=product_id)
    box.remove(product)
    return redirect('box:box_detail')

def box_detail(request):
    box = Box(request)
    for item in box:
        item['update_quantity_form'] = BoxAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'box/detail.html', {'box': box})

