from django.db import models

# Create your models here.

class account(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,blank=True,
    #                          blank=True, on_delete=models.CASCADE)
    student_name=models.CharField(max_length=300,null=True,blank=True)
    fees_type = models.CharField(max_length=300, null=True, blank=True)
    amount=models.IntegerField(max_length=300, null=True, blank=True)
    date=models.DateField(max_length=300,null=True,blank=True)
        

