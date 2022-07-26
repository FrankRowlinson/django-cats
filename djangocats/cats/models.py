from django.db import models


class Cat(models.Model):
    FUNNY = 'funny'
    SERIOUS = 'serious'
    CUTE = 'cute'
    CATEGORY_CHOICES = [
        (FUNNY, 'Funny :>'),
        (SERIOUS, 'Serious cat :|'),
        (CUTE, 'Very cute OwO')
    ]
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=250, blank=True)
    photo = models.ImageField(upload_to='pictures/%Y_%m/')
    category = models.CharField(
        max_length=7, 
        choices=CATEGORY_CHOICES, 
        default=FUNNY
        )
    time_created = models.DateTimeField(auto_now_add=True)
    time_edited = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.id}) {self.title}"