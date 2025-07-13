# services.py
"""
Service for fetching stock data from external sources.
"""
from .models import Ticker, TickerDailyData
from datetime import date
import random

def fetch_all_ticker_daily_data():
    """
    Simulate fetching daily data for all tickers using a mock API response.
    Save the data to the TickerDailyData model.
    Returns a summary dict.
    """
    tickers = Ticker.objects.all()
    today = date.today()
    records = []
    for ticker in tickers:
        base_price = random.uniform(50, 500)
        open_price = round(base_price, 2)
        close_price = round(open_price + random.uniform(-5, 5), 2)
        high_price = round(max(open_price, close_price) + random.uniform(0, 5), 2)
        low_price = round(min(open_price, close_price) - random.uniform(0, 5), 2)
        volume = random.randint(100_000, 10_000_000)
        per = round(random.uniform(10, 30), 2)
        dividend = round(random.uniform(0, 2), 2)
        capital = round(random.uniform(1e7, 1e9), 2)
        analyst_rating = random.choice(['buy', 'hold', 'sell'])

        mock_data = {
            'ticker': ticker,
            'date': today,
            'open': open_price,
            'close': close_price,
            'high': high_price,
            'low': low_price,
            'volume': volume,
            'per': per,
            'dividend': dividend,
            'capital': capital,
            'analyst_feeds': {'rating': analyst_rating},
            'extra_data': {'source': 'mock', 'note': f'Generated for {ticker.symbol}'},
        }
        obj, created = TickerDailyData.objects.update_or_create(
            ticker=ticker, date=today,
            defaults=mock_data
        )
        records.append({'ticker': ticker.symbol, 'created': created})
    return records 