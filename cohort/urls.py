from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('cohorts',views.CohortView)
urlspatterns = [
    path('', include(router.urls))
]