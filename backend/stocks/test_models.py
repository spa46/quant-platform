from django.test import TestCase
from django.utils import timezone
from stocks.models import Index, Ticker, TickerDailyData

class IndexModelTest(TestCase):
    def setUp(self):
        self.index = Index.objects.create(
            name='S&P 500',
            ticker='SPX',
            region='US',
            etf='SPY',
            timezone='America/New_York'
        )

    def test_index_creation(self):
        """Test Index model creation"""
        self.assertEqual(str(self.index), 'S&P 500 (SPX)')
        self.assertEqual(self.index.name, 'S&P 500')
        self.assertEqual(self.index.region, 'US')
        self.assertIsNotNone(self.index.created_at)


class TickerModelTest(TestCase):
    def setUp(self):
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

    def test_ticker_creation(self):
        """Test Ticker model creation"""
        self.assertEqual(str(self.ticker), 'AAPL (stock)')
        self.assertEqual(self.ticker.symbol, 'AAPL')
        self.assertEqual(self.ticker.type, 'stock')
        self.assertEqual(self.ticker.indexes.count(), 1)
        self.assertEqual(self.ticker.indexes.first().ticker, 'SPX')


class TickerDailyDataModelTest(TestCase):
    def setUp(self):
        self.ticker = Ticker.objects.create(
            symbol='AAPL',
            name='Apple Inc.',
            type='stock',
            region='US'
        )
        self.daily_data = TickerDailyData.objects.create(
            ticker=self.ticker,
            date='2023-01-01',
            open=150.0,
            close=152.0,
            high=153.0,
            low=149.5,
            volume=10000000,
            per=25.5,
            dividend=0.88,
            capital=2500000000.00
        )

    def test_daily_data_creation(self):
        """Test TickerDailyData model creation"""
        self.assertEqual(str(self.daily_data), 'AAPL 2023-01-01')
        self.assertEqual(float(self.daily_data.open), 150.0)
        self.assertEqual(float(self.daily_data.close), 152.0)
        self.assertEqual(self.daily_data.volume, 10000000)
        self.assertEqual(self.daily_data.ticker.symbol, 'AAPL')
        
    def test_meta_options(self):
        """Test TickerDailyData Meta options"""
        meta = TickerDailyData._meta
        self.assertEqual(meta.unique_together, (('ticker', 'date'),))
        self.assertEqual(meta.ordering, ['-date', 'ticker'])
