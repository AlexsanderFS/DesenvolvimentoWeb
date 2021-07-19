from django.urls import path
from appWeb.views import index, w3c, html, css, javascript, frontend, backend, contato

urlpatterns = [
    path('', index, name="index"),
    path('w3c', w3c, name="w3c"),
    path('css', css, name="css"),
    path('html', html, name="html"),
    path('javascript', javascript, name="javascript"),
    path('frontend', frontend, name="frontend"),
    path('backend', backend, name="backend"),
    path('contato', contato, name="contato"),
]
