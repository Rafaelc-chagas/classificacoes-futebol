from django.urls import path
from django.views.generic import RedirectView
from . import views


urlpatterns = [
    path('', RedirectView.as_view(url='ratings/', permanent=False)),
    path('ratings/', views.RatingView.as_view(), name='ratings'),
]
