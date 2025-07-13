from django.db import models

class IndexDailyData(models.Model):
    date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=64)
    ticker = models.CharField(max_length=32)
    etf = models.CharField(max_length=32, blank=True, null=True)
    region = models.CharField(max_length=8)
    data = models.JSONField()

    class Meta:
        unique_together = ("date", "ticker")
        ordering = ["-date", "name"]

    def __str__(self):
        return f"{self.date} - {self.name} ({self.ticker})"
