from django.urls import path
from . import views
# from teklif.views import index

urlpatterns = [
    # path('', index),
    path('', views.teklif_submit_view, name='teklif_submit_view'),
    path('success/', views.offer_success_view, name='offer_success_view'),
]