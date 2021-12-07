from django.db import models

class team_inv(models.Model):
    title = models.CharField(max_length=600)
    def __str__(self):
        return self.title

class vgr_token(models.Model):
    title = models.CharField(max_length=200)
    amount = models.BigIntegerField()
    ownership = ManyToManyField(team_inv)    
    def __str__(self):
        return self.title

class item_1(models.Model):
    title = models.CharField(max_length=300)
    amount = models.BigIntegerField()
    description = models.CharField(max_length=1000)
    ownership = ManyToManyField(team_inv)    
    def __str__(self):
        return self.title

class item_2(models.Model):
    title = models.CharField(max_length=300)
    amount = models.BigIntegerField()
    description = models.CharField(max_length=1000)
    ownership = ManyToManyField(team_inv)   
    def __str__(self):
        return self.title

class item_3(models.Model):
    title = models.CharField(max_length=300)
    amount = models.BigIntegerField()
    description = models.CharField(max_length=1000)
    ownership = ManyToManyField(team_inv)   
    def __str__(self):
        return self.title



# Create your models here.
