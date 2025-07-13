from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'indices', views.IndexViewSet)
router.register(r'tickers', views.TickerViewSet)
router.register(r'daily-data', views.TickerDailyDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
