from django.db import models


class MakeShortUrl(models.Model):
    short_code = models.CharField(max_length=6)
    long_url = models.CharField(max_length=400)
    number_of_clicks = models.IntegerField(default=0)

    def __str__(self):
        return self.short_code
