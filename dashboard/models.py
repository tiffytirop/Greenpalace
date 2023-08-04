from django.db import models

class AnalyticsData(models.Model):
    item_name = models.CharField(max_length=100)
    quantity_sold = models.IntegerField(default=0)

    def __str__(self):
        return self.item_name