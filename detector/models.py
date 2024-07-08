from django.db import models

class Image(models.Model):
    image = models.ImageField(null=False, blank=False, upload_to="images/")
    def __str__(self):
        return self.image
