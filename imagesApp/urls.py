from django.urls import path
from .views import Home, CreateForm

urlpatterns = [
    path('', Home.as_view(), name = "home"),
    path('post/', CreateForm.as_view(), name = "post")
]