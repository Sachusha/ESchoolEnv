from datetime import date
from django.db import models
from django.utils import timezone
from user_settings.models import Mothertongue, State, Relation, Religion,Caste
from academic_settings.models import AcademicYear, Standard, ExamMark,ClassDivision


class Student(models.Model):
    STUD_GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')
    )
    BLOOD_GROUP = (
        (1, 'A+'),
        (2, 'A-'),
        (3, 'B+'),
        (4, 'B-'),
        (5, 'O+'),
        (6,'O-'),
        (7, 'AB+'),
        (8, 'AB-'),
    )
    stud_admno = models.CharField(max_length=15)
    standard = models.ForeignKey(Standard, on_delete=models.RESTRICT)
    stud_regdate = models.DateField(default=date.today)
    stud_name = models.CharField(max_length=100)
    stud_address = models.CharField(max_length=300)
    state = models.ForeignKey(State, on_delete=models.RESTRICT)
    stud_email = models.EmailField(max_length=30)
    stud_adharno = models.CharField(max_length=12)
    religion = models.ForeignKey(Religion, on_delete=models.RESTRICT, default=None)
    caste = models.ForeignKey(Caste, on_delete=models.RESTRICT,  default=None)
    stud_nationality = models.CharField(max_length=30)
    mothertongue = models.ForeignKey(Mothertongue, on_delete=models.RESTRICT)
    stud_dob = models.DateField(default=date.today)
    stud_guardian = models.IntegerField(default=None)
    stud_bloodgroup = models.IntegerField(choices=BLOOD_GROUP, default=None)
    stud_gender = models.CharField(choices=STUD_GENDER, max_length=1, default=None)


    def __str__(self):
        return self.stud_admno
        # return "%s %s" % (self.stud_admno, str(self.standard))

class StudentAcademic(models.Model):
    student = models.ForeignKey(Student, on_delete=models.RESTRICT)
    classdivision = models.ForeignKey(ClassDivision, on_delete=models.RESTRICT)
    academicyear = models.ForeignKey(AcademicYear, on_delete=models.RESTRICT)

    def __str__(self):
        return self.student


class StudentMarks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.RESTRICT)
    exammark = models.ForeignKey(ExamMark, on_delete= models.RESTRICT)
    studmark_obtained = models.IntegerField()

    def __str__(self):
        return self.student


class Parent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.RESTRICT)
    relation = models.ForeignKey(Relation, on_delete=models.RESTRICT)
    parent_name = models.CharField(max_length=100)
    parent_permaddress = models.CharField(max_length=300)
    parent_commaddress = models.CharField(max_length=300)
    parent_contactno = models.CharField(max_length=13)
    parent_email = models.CharField(max_length=30)
    parent_adharno = models.CharField(max_length=12)
    parent_occupation = models.CharField(max_length=300)
    parent_bloodgroup = models.IntegerField()

    def __str__(self):
        return self.student








