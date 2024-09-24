from django.urls import path
from .views import HomePageView, ModulesPageView, ProfilePageView

urlpatterns = [
    path('modules/', ModulesPageView.as_view(), name='modules'),
    path('profile/', ProfilePageView.as_view(), name='profile'),
    path('', HomePageView.as_view(), name='home'),
]