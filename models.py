from django.db import models

# Create your models here.
class DemonSlayer(models.Model):
    first_name = models.CharField(max_length= 50)
    last_name = models.CharField(max_length = 50)
    category = models.CharField(max_length=12)
    age = models.IntegerField(default = 0)
    element_type = models.CharField(max_length = 12)

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name} Category:{self.category}, Age: {self.age}, Element Type: {self.element_type}"
    

class something(models.Model):
    thing = models.ForeignKey(DemonSlayer, on_delete=models.CASCADE)
    text = models.CharField(max_length = 500)

    def _str__(self):
        return self.text
    
class ContactUsNow(models.Model):
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)
    email_address = models.EmailField(max_length=50)
    enquiry = models.CharField(max_length = 1000)

    def __str__(self):
        return f"{self.first_name},{self.last_name}"