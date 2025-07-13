from django.db import models

class Index(models.Model):
    name = models.CharField(max_length=128)
    ticker = models.CharField(max_length=32)
    region = models.CharField(max_length=8)
    etf = models.CharField(max_length=32, blank=True, null=True)
    timezone = models.CharField(max_length=32, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.ticker})"

class Ticker(models.Model):
    symbol = models.CharField(max_length=32)
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=16)  # 'index', 'etf', 'stock'
    region = models.CharField(max_length=8)
    indexes = models.ManyToManyField(Index, related_name='tickers', blank=True)
    timezone = models.CharField(max_length=32, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.symbol} ({self.type})"

class TickerDailyData(models.Model):
    ticker = models.ForeignKey(Ticker, on_delete=models.CASCADE)
    date = models.DateField()
    open = models.DecimalField(max_digits=18, decimal_places=4, null=True, blank=True)
    close = models.DecimalField(max_digits=18, decimal_places=4, null=True, blank=True)
    high = models.DecimalField(max_digits=18, decimal_places=4, null=True, blank=True)
    low = models.DecimalField(max_digits=18, decimal_places=4, null=True, blank=True)
    volume = models.BigIntegerField(null=True, blank=True)
    per = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    dividend = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    capital = models.DecimalField(max_digits=18, decimal_places=4, null=True, blank=True)
    analyst_feeds = models.JSONField(null=True, blank=True)
    extra_data = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("ticker", "date")
        ordering = ["-date", "ticker"]

    def __str__(self):
        return f"{self.ticker.symbol} {self.date}"

