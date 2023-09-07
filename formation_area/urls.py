from django.urls import path
from .views import *

urlpatterns = [
    path('', FormationAreaList.as_view()),
    path('program', ProgramList.as_view()),
    path('<slug:formation_area_slug>', FormationAreaDetail.as_view()),
    path('<slug:formation_area_slug>/<slug:program_type>/<slug:program_slug>', ProgramDetail.as_view()),
]
