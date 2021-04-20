from django.urls import path
from django.urls.resolvers import URLPattern
from .views import ListarCrearAnimalesController, CRUDAnimalesController

urlpatterns = [
  path('animales',ListarCrearAnimalesController.as_view()),
  path('animales/<int:pk>', CRUDAnimalesController.as_view())
]