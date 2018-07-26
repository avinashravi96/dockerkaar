from django.db import models
from django.core.validators import *
# Create your models here.

class Finished(models.Model):
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user


class Order(models.Model):
    questions = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    section = models.IntegerField()

    def __str__(self):
        return self.user

# asdsadsssdsadwqewqewqewqewewqeqweqwewqewqsadadds
class Student(models.Model):
    time = models.CharField(max_length = 10, default = "60:00")
    name = models.CharField(max_length = 200 )
    # preference1 = models.CharField(max_length = 200 )
    # preference2 = models.CharField(max_length = 200 )
    regno = models.CharField(max_length = 200, unique=True )
    email = models.EmailField(max_length = 200 )
    number = models.CharField(max_length = 12 )
    altnumber = models.CharField(max_length = 12 )
    mothertoungue = models.CharField(max_length = 200 )
    dob = models.CharField(max_length = 200 )
    gender = models.CharField(max_length = 30 )
    tenth = models.CharField(max_length = 10 )
    twelth = models.CharField(max_length = 10 )
    ugcollege = models.CharField(max_length = 200 )
    ugstream = models.CharField(max_length = 200 )
    undergraduation = models.CharField(max_length = 10 )
    pgcollege = models.CharField(max_length = 200 )
    pgstream = models.CharField(max_length = 200 )
    postgraduation = models.CharField(max_length = 10 )
    zone = models.CharField(max_length = 200 )
    members = models.CharField(max_length = 20 )
    earningmembers = models.CharField(max_length = 20 )
    fatherprof = models.CharField(max_length = 200 )
    motherprof = models.CharField(max_length = 200 )
    written = models.CharField(max_length = 20 )
    spoken = models.CharField(max_length = 20 )
    msoffice = models.CharField(max_length = 20 )
    extracurricular = models.TextField()
    QAscore = models.IntegerField()
    LRscore = models.IntegerField()
    VRscore = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.regno


class Submit(models.Model):
    questions = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    section = models.IntegerField()

    def __str__(self):
        return self.user

class Marked(models.Model):
    questions = models.CharField(max_length=1000)
    user = models.CharField(max_length=100)
    section = models.IntegerField()

    def __str__(self):
        return self.user


class Skip(models.Model):
    questions = models.CharField(max_length=1000)
    user = models.CharField(max_length=100)
    section = models.IntegerField()
    def __str__(self):
        return self.user




class AptQuestion(models.Model):
    text = models.TextField('Question')
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100, db_index = True)
    section = models.IntegerField( db_index = True)
    # section = models.ForeignKey(Section, blank=True,null=True,on_delete = models.CASCADE)

    def __unicode__(self):
        return str(self.section)

    def __str__(self):
        return str(self.section)


class Test(models.Model):

    name = models.CharField('Set', max_length=100)
    # start = models.DateField('Start On', blank=True, null=True)
    # end = models.DateField('End On', blank=True, null=True)
    questions = models.ManyToManyField(AptQuestion, blank=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Answered(models.Model):
    answers= models.TextField()
    # answers= models.CharField(max_length=100,  validators=[validate_comma_separated_integer_list])
    user = models.CharField(max_length=100)
    section = models.IntegerField()

    def __str__(self):
        return self.user
