from django.views import generic
from django.http.response import JsonResponse
import string
import csv
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
import math
from operator import itemgetter
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor


class CartView(generic.TemplateView):
    template_name = "cart.html"

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