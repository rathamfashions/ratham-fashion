from django.urls import path
from . import views

urlpatterns = [
    path("",views.collection,name="collection"),
    path("about",views.about,name="about"),
    path("collection/<str:name>",views.collectionview,name="collection"),
    path("collection/<str:name>/<str:pname>",views.product_details,name="product_details"),
]    