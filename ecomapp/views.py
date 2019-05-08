from django.shortcuts import render
from .models import Category, Product, CartItem, Cart
from django.http import JsonResponse
from .forms import OrderForm


def base_view(request):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    cart = cart_create(request)
    context = {
        'categories': categories,
        'products': products,
        'cart': cart
    }
    return render(request, 'base.html', context)


def product_view(request, product_slug):
    cart = cart_create(request)
    product = Product.objects.get(slug=product_slug)
    categories = Category.objects.all()
    context = {
        'product': product,
        'categories': categories,
        'cart': cart

    }
    return render(request, 'product.html', context)


def category_view(request, category_slug):
    cart = cart_create(request)
    category = Category.objects.get(slug=category_slug)
    products_of_category = Product.objects.filter(category=category)
    categories = Category.objects.all()
    context = {
        'category': category,
        'products_of_category': products_of_category,
        'categories': categories,
        'cart': cart
    }
    return render(request, 'category.html', context)


def cart_view(request):
    cart = cart_create(request)
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'cart': cart
    }
    return render(request, 'cart.html', context)


def add_to_cart_view(request):
    cart = cart_create(request)
    product_slug = request.GET.get('product_slug')
    product = Product.objects.get(slug=product_slug)
    cart.add_to_cart(product.slug)
    new_cart_total = 0.00
    for item in cart.items.all():
        new_cart_total += float(item.item_total)
    cart.cart_total = new_cart_total
    cart.save()
    return JsonResponse({
        'cart_total': cart.items.count(),
        'cart_total_price': cart.cart_total
    })


def remove_from_cart_view(request):
    cart = cart_create(request)
    product_slug = request.GET.get('product_slug')
    product = Product.objects.get(slug=product_slug)
    cart.remove_from_cart(product.slug)
    new_cart_total = 0.00
    for item in cart.items.all():
        new_cart_total += float(item.item_total)
    cart.cart_total = new_cart_total
    cart.save()
    return JsonResponse({
        'cart_total': cart.items.count(),
        'cart_total_price': cart.cart_total
    })


def change_item_qty(request):
    cart = cart_create(request)
    qty = request.GET.get('qty')
    item_id = request.GET.get('item_id')
    cart.change_qty(qty, item_id)
    cart_item = CartItem.objects.get(id=int(item_id))
    return JsonResponse({
        'cart_total': cart.items.count(),
        'item_total': cart_item.item_total,
        'cart_total_price': cart.cart_total
    })


def checkout_view(request):
    cart = cart_create(request)
    context = {
        'cart': cart
    }
    return render(request, 'checkout.html', context)


def cart_create(request):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    return cart


def order_create_view(request):
    form = OrderForm(request.POST or None)
    context = {
        'form': form
    }
    return render(request, 'order.html', context)





