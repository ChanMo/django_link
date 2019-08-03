from django.urls import path
from .views import *

urlpatterns = [
        path('<str:label>/', LinkView.as_view())
]
