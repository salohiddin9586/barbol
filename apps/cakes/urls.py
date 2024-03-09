from django.urls import include, path

from apps.cakes.views import CakeListView, about, CakeDetailView


urlpatterns = [
    path('', CakeListView.as_view(), name='cake_list'),
    # path('cake/<str:slug>', CakeDetailView.as_view(), name='product_detail'),
    # path('about/', about, name='about'),
]


