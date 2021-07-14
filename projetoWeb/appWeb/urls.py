from django.urls import path
from appWeb.views import index, javascript, frontend, backend

urlpatterns = [
    path('', index, name="index"),
    path('javascript', javascript, name="javascript"),
    path('frontend', frontend, name="frontend"),
    path('backend', backend, name="backend"),
]
