from django.db import models


class Trip(models.Model):
    owner_id = models.CharField(max_length=36)  # this will be a uuid for now
    name = models.CharField(max_length=200)

    class Meta:
        indexes = [models.Index(fields=["owner_id"])]

    def __str__(self):
        return f"{self.name}"
