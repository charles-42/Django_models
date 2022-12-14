from django.db import models

class User(models.Model):
    
    name = models.fields.CharField(max_length=100)
    age = models.fields.IntegerField()
    email = models.fields.EmailField()
    mdp = models.fields.CharField(max_length=100)

    def __str__(self):
        return self.name

    def for_test_method_name_length(self):
        return len(self.name)