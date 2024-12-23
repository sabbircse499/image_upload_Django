from django.db import models

class product(models.Model):
    title =models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True, null=True)
    discount=models.IntegerField(blank=True,null=True)
    price=models.IntegerField(blank=True,null=True)
    newprice=models.IntegerField(blank=True,null=True)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id} - {self.description}"