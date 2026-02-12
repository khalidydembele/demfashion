from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    image = models.ImageField(upload_to='products/images/')
    video = models.FileField(upload_to='products/videos/', blank=True, null=True)

    def __str__(self):
        return self.name

class Highlight(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='highlights/')
    
    def __str__(self):
        return self.title