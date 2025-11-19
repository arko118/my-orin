from django.db import models

class details(models.Model):
    Name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='profile-pic/')
    profession = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    Adress = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=200)
    summary = models.CharField(max_length=400)
    about_me = models.CharField(max_length=500)

    def __str__(self):
        return self.Name
    

class skills(models.Model):

    skill = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.skill
    
class education(models.Model):

    degree_title = models.CharField(max_length=200)
    institute =  models.CharField(max_length=200)
    starting_year = models.DateField()
    ending_year = models.DateField()
    
    def __str__(self):
        return self.degree_title
    
class experience(models.Model):

    job_title = models.CharField(max_length=200)
    company =  models.CharField(max_length=200)
    starting_year = models.DateField()
    ending_year = models.DateField()
    about  = models.CharField(max_length=500)

    def __str__(self):
        return self.job_title


