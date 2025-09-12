import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
import os
from io import BytesIO
from django.core.files.base import ContentFile
from django.db import models
from django.utils.text import slugify
from PIL import Image as PilImage, ImageDraw, ImageFont

    # ---------- Theme choices ----------
THEME_CHOICES = [
        ("light", "Light"),
        ("dark", "Dark"),
    ]

class CustomUser(AbstractUser):
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        profile_picture = models.ImageField(upload_to="profile/", default="default_male_avatar.png" )
        selected_theme = models.CharField(max_length=100, choices=THEME_CHOICES, default="dark")
        favourites = models.ManyToManyField("Image", through="Favourite", related_name="favourited_by")

        def __str__(self):
            return self.username
        
class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.CharField(max_length=255, default="pixeliowall")
    image_title = models.CharField(max_length=255, unique=True)
    image_short_description = models.CharField(max_length=1000)
    image_detailed_description = models.TextField(blank=True)
    category = models.CharField(max_length=2000)
    original_image = models.ImageField(upload_to="original-images/" , unique=True)
    watermarked_image = models.ImageField(upload_to="watermarked-images/", blank=True, null=True)
    alt_text = models.CharField(max_length=500, default="", blank=True)
    is_paid = models.BooleanField(default=False)
    image_price = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.image_title)

        super().save(*args, **kwargs)

        if self.is_paid and self.original_image and not self.watermarked_image:
            img = PilImage.open(self.original_image).convert("RGBA")
            watermark = PilImage.new("RGBA", img.size, (0, 0, 0, 0))
            draw = ImageDraw.Draw(watermark)

            font_size = max(30, img.size[0] // 15)
            try:
                font = ImageFont.truetype("arial.ttf", font_size)
            except IOError:
                font = ImageFont.load_default()

            text = "Pixeliowall"
            bbox = draw.textbbox((0, 0), text, font=font)
            textwidth = bbox[2] - bbox[0]
            textheight = bbox[3] - bbox[1]

            x_step = int(textwidth * 2.2)
            y_step = int(textheight * 2.2)

            vertical_pad = int(textheight * 0.35)
            for y in range(0, img.size[1], y_step):
                for x in range(0, img.size[0], x_step):
                    temp = PilImage.new("RGBA", (textwidth, textheight + vertical_pad * 2), (0,0,0,0))
                    temp_draw = ImageDraw.Draw(temp)
                    temp_draw.text((0, vertical_pad), text, font=font, fill=(255,255,255,160))
                    rotated = temp.rotate(20, expand=1)
                    offset_x = x + (textwidth if (y//y_step)%2 else 0)
                    watermark.paste(rotated, (offset_x, y), rotated)

            watermarked = PilImage.alpha_composite(img, watermark).convert("RGB")
            buffer = BytesIO()
            watermarked.save(buffer, format="JPEG", quality=90)
            buffer.seek(0)

            file_name = os.path.basename(self.original_image.name)
            wm_file = ContentFile(buffer.read())
            self.watermarked_image.save(f"wm_{file_name}", wm_file, save=False)
            super().save(update_fields=["watermarked_image"])

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