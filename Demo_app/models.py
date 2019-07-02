from django.db import models

# Create your models here.

STATUS_CHOICES = [
    ('Yes', 'True'),
    ('No','False'),
]

class Create(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=100)
    completed = models.CharField(max_length=10, choices=STATUS_CHOICES,default='No')

    def __str__(self):
        return self.name
    class Meta:
        db_table = "create"
