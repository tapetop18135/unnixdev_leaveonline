from django.db import models
from django.contrib.auth.models import User
from managedb.models import Policy, StatusLeave

class History(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    leaveday_begin = models.DateTimeField()
    leaveday_end = models.DateTimeField()
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE)
    sta_sup = models.ForeignKey(StatusLeave, on_delete=models.CASCADE, related_name='status_sup')
    sta_hr = models.ForeignKey(StatusLeave, on_delete=models.CASCADE, related_name='status_hr')
    sta_user = models.ForeignKey(StatusLeave, on_delete=models.CASCADE, related_name='status_user')

    def __str__(self):
        return self.user
