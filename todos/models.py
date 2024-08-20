from django.db import models

class Todo(models.Model):
    class Priority(models.IntegerChoices):
        LOW = 0, 'Low'
        MEDIUM = 1, 'Medium'
        HIGH = 2, 'High'

    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    priority = models.IntegerField(choices=Priority.choices, default=Priority.LOW)

    def __str__(self):
        return self.title
