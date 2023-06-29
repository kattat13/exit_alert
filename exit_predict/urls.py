from django.urls import path
from .views import attrition_rate_finder

urlpatterns = [
    path('', attrition_rate_finder, name='home'),
    # path('results-attrition/', results, name='results_show'),
    ]