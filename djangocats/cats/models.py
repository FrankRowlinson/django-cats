from django.db import models


class Cat(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=250, blank=True)
    photo = models.ImageField(upload_to='pictures/%Y_%m/')
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    time_created = models.DateTimeField(auto_now_add=True)
    time_edited = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.id}) {self.title}"


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name