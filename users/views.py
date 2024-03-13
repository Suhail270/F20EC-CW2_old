from django.views import generic
from django.http.response import JsonResponse
import string
import csv
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from .forms import CustomUserCreationForm

# Create your views here.

class LandingPageView(generic.TemplateView):
    template_name = "landing.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("services")
        return super().dispatch(request, *args, **kwargs)

class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")

class ServicesView(generic.TemplateView):
    template_name = "services.html"

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class VisionView(generic.TemplateView):
    template_name = "vision.html"
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class OurTeamView(generic.TemplateView):
    template_name = "team.html"
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class ProductListView(generic.TemplateView):
    template_name = "products-display.html"
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
class MembershipPlanView(generic.TemplateView):
    template_name = "plan.html"
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class PaymentView(generic.TemplateView):
    template_name = "payment.html"
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
class PaymentSuccessView(generic.TemplateView):
    template_name = "payment_success.html"
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class TrialSuccessView(generic.TemplateView):
    template_name = "freeTrial.html"
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)