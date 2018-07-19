from django.db import models

# Create your models here.
class info(models.Model):               # created the first model/database of info
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    year = models.PositiveSmallIntegerField(default = 2018)
    message = models.TextField(max_length=500)

    def __str__(self):              # tell what to return whhen asked 
        return self.first_name
