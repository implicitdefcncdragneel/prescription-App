import uuid
from django.db import models
from ..user.models import User
from django.core.exceptions import ValidationError



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    q1= models.CharField(max_length=200,unique=False,default=False)
    q2= models.CharField(max_length=200,unique=False,default=False)
    q3= models.CharField(max_length=200,unique=False,default=False)
    q4= models.CharField(max_length=200,unique=False,default=False)
    q5= models.CharField(max_length=200,unique=False,default=False)

    docfile = models.FileField(blank=True, default="",upload_to='documents/%Y/%m/%d')

    imgDoc = models.ImageField(blank=True, default="",upload_to='images/')


    # def __str__(self):
    #     return self.id

    class Meta:
        '''
        to set table name in database
        '''
        db_table = "profile_patient"

class FileUpload(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,)
    datafile = models.FileField()
    imagefile= models.ImageField(null=False)


# class TaskImage(models.Model):
#     task = models.ForeignKey(User, on_delete=models.CASCADE)
#     image = models.FileField(blank=True)















