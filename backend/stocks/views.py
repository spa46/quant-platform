from rest_framework import viewsets, permissions
from .models import Index, Ticker, TickerDailyData
from .serializers import IndexSerializer, TickerSerializer, TickerDailyDataSerializer

class IndexViewSet(viewsets.ModelViewSet):
    queryset = Index.objects.all()
    serializer_class = IndexSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class TickerViewSet(viewsets.ModelViewSet):
    queryset = Ticker.objects.all()
    serializer_class = TickerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ['symbol', 'type', 'region']

class TickerDailyDataViewSet(viewsets.ModelViewSet):
    queryset = TickerDailyData.objects.all()
    serializer_class = TickerDailyDataSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filterset_fields = ['ticker__symbol', 'date']
