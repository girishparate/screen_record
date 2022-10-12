from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ticket(models.Model):
    data_obj = models.CharField(max_length=100)
    file_video = models.FileField(upload_to='screen_record', null=True, blank=True)
    video_stop = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.data_obj