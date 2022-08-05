from django.db import models
from django.urls import reverse


class Cat(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=250, blank=True)
    photo = models.ImageField(upload_to='pictures/%Y_%m/')
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    time_created = models.DateTimeField(auto_now_add=True)
    time_edited = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        ordering = ['time_created']


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse("category", kwargs={"name": self.name})

    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
