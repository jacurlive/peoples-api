from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Peoples(models.Model):
    name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    nickname = models.CharField(max_length=155, blank=True, null=True)
    content = models.TextField(blank=True)
    birth_date = models.DateField()
    is_published = models.BooleanField(default=False)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
