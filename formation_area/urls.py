from django.urls import path
from .views import FormationAreaList

urlpatterns = [
    path('', FormationAreaList.as_view())
]
