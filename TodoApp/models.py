from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    content=models.TextField()
    added_date=models.DateField(auto_now_add=True)
    due_date=models.DateField()
    options=(
        ("pending","pending"),
        ("completed","completed")
    )
    status=models.CharField(max_length=50,default="pending",choices=options)