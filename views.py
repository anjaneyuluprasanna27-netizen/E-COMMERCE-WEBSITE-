import json
from decimal import Decimal
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Product, Order, OrderItem


def index(request):
    products = Product.objects.filter(in_stock=True).order_by('id')
    genres = Product.GENRE_CHOICES
    return render(request, 'store/index.html', {
        'products': products,
        'genres': genres,
    })


@require_POST
def cart_add(request):
    data = json.loads(request.body or '{}')
    product_id = str(data.get('product_id'))
    product = get_object_or_404(Product, id=product_id)

    cart = request.session.setdefault('cart', {})
    cart[product_id] = cart.get(product_id, 0) + 1
    request.session.modified = True

    return JsonResponse(_cart_payload(request.session))


@require_POST
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        return JsonResponse({'error': 'Your crate is empty'}, status=400)

    order = Order.objects.create(status='paid')

    products_by_id = {str(p.id): p for p in Product.objects.filter(id__in=cart.keys())}
    for pid, qty in cart.items():
        product = products_by_id.get(pid)
        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=qty,
            price_at_purchase=product.price,
        )

    order.recalculate_total()
    request.session['cart'] = {}
    request.session.modified = True

    return JsonResponse({
        'order_id': order.id,
        'total': float(order.total),
        'message': 'Order placed — thanks for shopping the crate!',
    })


def _cart_payload(session):
    cart = session.get('cart', {})
    items, subtotal = [], Decimal('0.00')
    products = Product.objects.filter(id__in=cart.keys())
    products_by_id = {str(p.id): p for p in products}

    for pid, qty in cart.items():
        product = products_by_id.get(pid)
        if not product:
            continue
        subtotal += product.price * qty
        items.append({
            'id': product.id, 'title': product.title, 'artist': product.artist,
            'price': float(product.price), 'emoji': product.emoji,
            'bg': product.bg_color, 'quantity': qty,
        })

    return {'items': items, 'count': sum(cart.values()), 'subtotal': float(subtotal)}
