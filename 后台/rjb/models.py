from django.db import models

# Create your models here.

class tagHistroy(models.Model):
    hid = models.BigIntegerField()
    htag = models.CharField(max_length = 50)
    user = models.ForeignKey('User', on_delete = models.CASCADE)

class tagsAndFrequence(models.Model):
    tag = models.CharField(max_length = 50)
    frequent = models.BigIntegerField()
    user = models.ForeignKey('User', on_delete = models.CASCADE)

class ptagsInfo(models.Model):
    tag = models.CharField(max_length = 50)
    frequent = models.BigIntegerField()
    pic = models.ForeignKey('Picture', on_delete = models.CASCADE)

    def __str__(self):
        return self.tag

class User(models.Model):
    '''
    sex -1 unknown 0 man 1 woman
    '''
    uname = models.CharField(max_length = 50)
    upwd = models.CharField(max_length = 50)
    uemail = models.EmailField()
    utel = models.CharField(max_length = 20)
    ubirthday = models.DateField()
    uidentity = models.CharField(max_length = 50)
    usex = models.SmallIntegerField()
    uhonesty = models.FloatField()
    uadmin = models.BooleanField()
    uidcard = models.CharField(max_length = 20)
    urealname = models.CharField(max_length = 20)

    def __str__(self):
        return '\nuname:' + self.uname + '\nuemail: ' + self.uemail + '\n'

class Picture(models.Model):
    pimg = models.ImageField(upload_to='img')
    owner = models.ForeignKey('User', on_delete = models.CASCADE)
    finished = models.BooleanField()
    result = models.TextField()

class Face(models.Model):
    pimg = models.ImageField(upload_to='face')
    owner = models.ForeignKey('User', on_delete=models.CASCADE)