from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index),
    path('products', views.myProducts),     
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

]
