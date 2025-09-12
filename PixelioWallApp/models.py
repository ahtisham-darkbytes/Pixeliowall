import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


    # ---------- Theme choices ----------
THEME_CHOICES = [
        ("light", "Light"),
        ("dark", "Dark"),
    ]

class CustomUser(AbstractUser):
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        profile_picture = models.ImageField(upload_to="profile/", default="avatar.png")
        selected_theme = models.CharField(max_length=100, choices=THEME_CHOICES, default="dark")
        favourites = models.ManyToManyField("Image", through="Favourite", related_name="favourited_by")

        def __str__(self):
            return self.username
        

class Image(models.Model):
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        author = models.CharField(max_length=255, default="pixeliowall")
        image_title = models.CharField(max_length=255, unique=True) 
        image_short_description = models.CharField(max_length=1000, default="", blank=True)
        image_detailed_description = models.TextField(blank=True)
        category = models.CharField(max_length=2000)
        original_image = models.ImageField(upload_to="original-images/")
        watermarked_image = models.ImageField(upload_to="watermarked-images/", default="none")
        alt_text = models.CharField(max_length=500, default="", blank=True)
        is_paid = models.BooleanField(default=False)
        image_price = models.PositiveIntegerField(default=0)
        created_at = models.DateTimeField(auto_now_add=True)
        slug = models.SlugField(max_length=255, unique=True, blank=True)


        def save(self, *args, **kwargs):
            if not self.slug:
                self.slug = slugify(self.image_title)
            super().save(*args, **kwargs)


        def __str__(self):
            return f"{self.author} - {self.image_short_description[:30]}"


class Favourite(models.Model):  
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="favourite_entries")
        image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="favourite_entries")
        created_at = models.DateTimeField(auto_now_add=True)

        class Meta:
            unique_together = ("user", "image") 

        def __str__(self):
            return f"{self.user.username} → {self.image.id}"