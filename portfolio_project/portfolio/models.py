from django.db import models

class Education(models.Model):
    school = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.school} - {self.course}"

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField(blank=True, null=True) 
    order = models.PositiveIntegerField(default=0)  # Field to determine order

    class Meta:
        ordering = ['order']  # Order by the 'order' field

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)  # Field to determine order

    class Meta:
        ordering = ['order']  # Order by the 'order' field

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


# portfolio/models.py

class Coursework(models.Model):
    course_name = models.CharField(max_length=200)
    grade_received = models.CharField(max_length=10)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)  # Field to determine order

class WorkExperience(models.Model):
    job_title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  # End date can be optional
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['start_date']  # Order by start_date (or any other field you prefer)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"


