import datetime
from django.db.models.query import QuerySet
from django.views import generic
from django.http.response import JsonResponse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.conf import settings
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
import stripe
from .models import Order,OrderItem,Item

# TODO add loginrequiredmixin
class CartListView(generic.ListView):
    template_name = "cart.html"
    context_object_name = "items"

    def get_queryset(self):
        user = self.request.user
        cart, created = Order.objects.get_or_create(
            user = self.request.user,
            ordered = False
        )
        queryset = OrderItem.objects.filter(order=cart)
        return queryset
    
class PaymentView(generic.TemplateView):
    template_name = 'stripe.html'


class PaymentSuccessView(generic.TemplateView):
    template_name = "payment_success.html"
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'price': 'price_1Os1cYJDw3WYrLo5D2gQCvfP',
                        'quantity': 1,
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    
    except ValueError as e:
        return HttpResponse(status=400)
    
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        print("Payment was successful.")

    return HttpResponse(status=200)

@csrf_exempt
def add_to_cart(request, id):
    item = get_object_or_404(Item, id=id)
    orderID, created = Order.objects.get_or_create(
        user = request.user,
        ordered = False
    )
    
    orderitems = OrderItem.objects.filter(Order=orderID,item=item).first()

    if orderitems is not None:
        orderitems.quantity +=1
        orderitems.save()
    else:
        OrderItem.objects.create(
            order = orderID,
            item = item,
            quantity = 1
        )
    print("Added!")
    return JsonResponse({'message': 'Item added to cart successfully'})

# def remove_from_cart(request, id):
#     order_item = OrderItem.objects.get(id=id)
#     orderID, created = Order.objects.get_or_create(
#         user = request.user,
#         ordered = False
#     )
    
#     orderitems = OrderItem.objects.filter(Order=orderID,item=item).first()

#     if orderitems is not None:
#         orderitems.quantity +=1
#         orderitems.save()
#     else:
#         OrderItem.objects.create(
#             order = orderID,
#             item = item,
#             quantity = 1
#         )
#     print("Added!")
#     return JsonResponse({'message': 'Item added to cart successfully'})