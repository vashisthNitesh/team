from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from filer.fields.image import FilerImageField


class TeamMember(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True)
    role = models.CharField(max_length=100)
    photo = FilerImageField(
        verbose_name='Profile Photo',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    tagline = models.CharField(max_length=200, blank=True)
    short_bio = models.TextField(blank=True)
    full_bio = models.TextField(help_text='Rich text from django CMS text plugin is supported in templates.')
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True, verbose_name='X / Twitter')
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('core:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return f'{self.name} – {self.role}'


class Skill(models.Model):
    member = models.ForeignKey(TeamMember, related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    percentage = models.PositiveSmallIntegerField(default=75, validators=[MinValueValidator(0), MaxValueValidator(100)])
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f'{self.name} ({self.percentage}%)'
