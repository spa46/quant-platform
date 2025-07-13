from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from stocks.models import Index, Ticker, TickerDailyData

User = get_user_model()

class BaseTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='test@example.com',
            password='testpass123'
        )
        self.token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        
        # Create test data
        self.index = Index.objects.create(
            name='S&P 500',
            ticker='SPX',
            region='US'
        )
        self.ticker = Ticker.objects.create(
            symbol='AAPL',
            name='Apple Inc.',
            type='stock',
            region='US'
        )
        self.ticker.indexes.add(self.index)
        self.daily_data = TickerDailyData.objects.create(
            ticker=self.ticker,
            date='2023-01-01',
            open=150.0,
            close=152.0,
            high=153.0,
            low=149.5,
            volume=10000000
        )


class IndexViewSetTest(BaseTestCase):
    def test_list_indices(self):
        url = reverse('index-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['ticker'], 'SPX')
    
    def test_retrieve_index(self):
        url = reverse('index-detail', args=[self.index.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['ticker'], 'SPX')


class TickerViewSetTest(BaseTestCase):
    def test_list_tickers(self):
        url = reverse('ticker-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['symbol'], 'AAPL')
    
    def test_filter_tickers_by_region(self):
        url = f"{reverse('ticker-list')}?region=US"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class TickerDailyDataViewSetTest(BaseTestCase):
    def test_list_daily_data(self):
        url = reverse('tickerdailydata-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(float(response.data[0]['open']), 150.0)
    
    def test_filter_daily_data_by_ticker(self):
        url = f"{reverse('tickerdailydata-list')}?ticker__symbol=AAPL"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(float(response.data[0]['close']), 152.0)
