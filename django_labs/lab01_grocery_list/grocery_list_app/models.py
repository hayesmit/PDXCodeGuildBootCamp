from django.db import models
import datetime
from django.utils import timezone


class GroceryItem(models.Model):
    item_description = models.CharField(max_length=200)
    date_added = models.DateTimeField('date added')
    date_purchased = models.DateTimeField('date purchase', null=True, blank=True)
    was_purchased = models.BooleanField(default=False)

    def __str__(self):
        return self.item_description
    #
    # def has_been_purchased(self):
    #     self.date_purchased = timezone.now()
    #     self.was_purchased = True


