from django.db import models
from django.conf import settings



GROUP_CHOICES = (
    ('A', 'Arts'),
    ('C', 'Commerce'),
    ('S', 'Science')
)

RESULT_CHOICES = (

    ('F', 'FAILED'),
    ('P', 'PASSED'),

)

class UserModel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Class_Dakhil(models.Model):
    name = models.CharField(max_length=100)

    arabic = models.CharField(max_length=50)
    bangla = models.CharField(max_length=50)
    english = models.CharField(max_length=50)
    math = models.CharField(max_length=50)

class Class_Alim(models.Model):
    name = models.CharField(max_length=100)

    arabic = models.CharField(max_length=50)
    bangla = models.CharField(max_length=50)
    english = models.CharField(max_length=50)

class Semester(models.Model):
    alim = models.ForeignKey(Class_Alim, on_delete=models.SET_NULL, blank=True, null=True)
    dakhil = models.ForeignKey(Class_Dakhil, on_delete=models.SET_NULL, blank=True, null=True)


class StudentInfo(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                on_delete=models.CASCADE)
    name = models.CharField(max_length=45)
    img = models.ImageField()
    mother_name = models.CharField(max_length=45)
    father_name = models.CharField(max_length=45)
    date_of_birth = models.DateField()
    institute = models.ForeignKey('School', on_delete=models.CASCADE, blank=True, null=True)
    board = models.ForeignKey('Board', on_delete=models.SET_NULL, blank=True, null=True)
    roll = models.IntegerField()

    dept = models.ForeignKey(Semester, on_delete=models.SET_NULL, blank=True, null=True)

    group = models.CharField(choices=GROUP_CHOICES, max_length=1)
    result = models.CharField(choices=RESULT_CHOICES, max_length=1, blank=True)
    gpa = models.FloatField(null=True, blank=True)

    
    def __str__(self):
        return (str(self.roll))


class School(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    address = models.TextField()
    student = models.ManyToManyField(StudentInfo)
    board = models.ForeignKey('Board', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name


class Grade(models.Model):
    name = models.CharField(max_length=20)
    point = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        ordering = ["name"]
        verbose_name = 'Grade'
        verbose_name_plural = 'Grades'

YEARS = (
    (2020, 2020),
    (2019, 2019),
    (2018, 2018),
)


class Exam(models.Model):

    year = models.IntegerField(choices=YEARS)
    name = models.CharField(max_length=40)
    student = models.ManyToManyField(StudentInfo)
    board = models.ForeignKey('Board', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self): 
        return (f"{self.name} of {self.year}")



class Board(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Board'
        verbose_name_plural = 'Boards'



