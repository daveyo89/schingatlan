from django.urls import path
from House.views import Home, SearchView

urlpatterns = [
    path('search', SearchView.as_view(), name="search"),
    path('', Home.as_view(), name="index"),
]
