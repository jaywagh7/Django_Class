from django.db import models



class ModelName(models.Model): #id  (update, delete)
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=50, blank=True, null=True, help_text="enter name your lastname")
    age = models.IntegerField()
    date_of_birth = models.DateField()
    def __str__(self):
        return self.Firstname, self.Lastname, self.age, self.date_of_birth
        
class College(models.Model):
    Student_name = models.CharField(max_length=100)
    Dept_name = models.CharField(max_length=200)
    Roll_no = models.IntegerField()




    




