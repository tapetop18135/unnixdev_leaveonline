from django.db import models
from django.contrib.auth.models import User
from managedb.models import Department, Position, Policy

class Suppervisor(models.Model):
    
    dep_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    sup_name = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("dep_name","sup_name"),)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dep_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    pos_name = models.ForeignKey(Position, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = (("user"),)

class Remainleavedays(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE)
    remain_days = models.IntegerField(default=0)

    class Meta:
        unique_together = (("user","policy"),)
