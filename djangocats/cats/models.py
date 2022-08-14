from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

# ------ MANAGERS ------
class CatManager(models.Manager):
    # newest 'n' pictures
    # don't work as intended if Meta.ordering in Cat is changed!!!
    def new(self, n: int):
        return self.all()[:n]

    def by_category(self, name: str):
        category = Category.objects.get(name=name)
        return self.filter(category=category)


class CategoryManager(models.Manager):
    def names(self):
        return self.all().values_list('name', flat=True)


# ------ MODELS ------
class Cat(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250, blank=True)
    photo = models.ImageField(upload_to='pictures/%Y_%m/')
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    time_created = models.DateTimeField(auto_now_add=True)
    time_edited = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False)
    slug = models.SlugField()

    objects = CatManager()

    def __str__(self) -> str:
        return f"{self.title}"

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, set slug
            self.slug = slugify(self.title)

        super(Cat, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("post", kwargs={"cat_slug": self.slug})
    

    class Meta:
        ordering = ['-time_created']


class Category(models.Model):
    name = models.CharField(max_length=20)

    objects = CategoryManager()

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse("category", kwargs={"name": self.name})

    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
