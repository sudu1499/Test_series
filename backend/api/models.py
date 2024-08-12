from django.db import models



class qbank(models.Model):

    answer=models.CharField(max_length=20)
    qtype=models.CharField(max_length=20)
    image=models.ImageField(upload_to="api/images",null=True)