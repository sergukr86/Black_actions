from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField("date of birth")
    subject = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name
