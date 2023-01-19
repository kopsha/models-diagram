from django.db import models


LONG_TEXT = 255
SHORT_TEXT = 64



class User(models.Model):

    class Roles(models.TextChoices):
        EMPLOYER = "Employer"
        STAFF = "Staff"
        ADMIN = "Admin"

    email = models.EmailField()
    display_name = models.CharField(max_length=LONG_TEXT)
    role = models.CharField(choices=Roles.choices, default=Roles.EMPLOYER, max_length=SHORT_TEXT)


class Company(models.Model):
    registration_no = models.CharField(max_length=SHORT_TEXT)
    display_name = models.CharField(max_length=LONG_TEXT)
    trading_name = models.CharField(max_length=LONG_TEXT)


class Member(models.Model):
    pps_no = models.CharField(max_length=SHORT_TEXT)
    date_of_birth = models.DateField()
    full_name = models.CharField(max_length=LONG_TEXT)
    email = models.EmailField()


class Employer(models.Model):
    company = models.OneToOneField(Company, on_delete=models.CASCADE)
    members = models.ManyToManyField(Member, through="Employment")
    owner = models.OneToOneField(User, on_delete=models.CASCADE)


class Employment(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    started = models.DateField()
    ended = models.DateField(null=True)
