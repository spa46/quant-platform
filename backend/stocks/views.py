from rest_framework import viewsets, permissions
from .models import Index, Ticker, TickerDailyData
from .serializers import IndexSerializer, TickerSerializer, TickerDailyDataSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from .services.fetch_daily_data import fetch_and_store_daily_data

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

    @action(detail=False, methods=['post'], url_path='fetch')
    def fetch_daily_data(self, request):
        ticker_symbols = request.data.get('symbols')  # Optional: list of symbols
        results = fetch_and_store_daily_data(ticker_symbols)
        return Response({
            'status': 'success',
            'fetched': len(results),
            'details': results
        })
