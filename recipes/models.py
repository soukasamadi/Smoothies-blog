from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from cloudinary.models import CloudinaryField
from django.urls import reverse


STATUS = ((0, "Draft"), (1, "Published"))
User = get_user_model()


class Profile(models.Model):
    """
    Model for user profil
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image')

    def __str__(self):
        return f'{self.user.username}  Profile'


class Category(models.Model):
    """
    Model for category
    """
    class Meta:
        verbose_name_plural = 'Categories'
    title = models.CharField(max_length=20)
    category_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.title


class Author(models.Model):
    """
    Model for author
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    author_picture = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.user.username


class Recipe(models.Model):
    """
    Model for post recipe
    """
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    comment_count = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    categories = models.ManyToManyField(Category)
    time_to_prepar = models.IntegerField(default=0)
    featured_image = CloudinaryField('image', default='placeholder')
    stars = models.PositiveIntegerField(
        default=3,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)])
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)
    featured = models.BooleanField()

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('recipe_detail', kwargs={
            'id': self.id
        })


class Comment(models.Model):
    """
    Model for post comments
    """
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["timestamp"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

    def get_absolute_url(self):
        """Sets absolute URL"""
        return reverse('recipe_detail', args=[self.recipe.slug])
