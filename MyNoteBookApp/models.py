from django.db import models

class MyNoteBookModel(models.Model):
    title=models.CharField(max_length=256)
    complete=models.BooleanField(default=False)
    update=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
