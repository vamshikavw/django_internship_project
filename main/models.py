from django.db import models
from django.utils import timezone


class MotivationalQuote(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class Link(models.Model):
    slug = models.CharField(max_length=50, unique=True)
    destination = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def visits(self):
        return self.clicks.count()

    def __str__(self):
        return self.slug


class Click(models.Model):
    link = models.ForeignKey(Link, on_delete=models.CASCADE, related_name="clicks")
    ip = models.CharField(max_length=50, null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)
    device = models.CharField(max_length=50, default="unknown")
    country = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.link.slug} — {self.device} — {self.country}"

