from django.contrib import admin
from .models import MotivationalQuote, Link, Click


@admin.register(MotivationalQuote)
class MotivationalQuoteAdmin(admin.ModelAdmin):
    list_display = ("id", "text")


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    # Use ONLY real fields from your Link model
    # (slug, destination, created_at, visits – adjust if needed)
    list_display = ("slug", "destination", "created_at")
    search_fields = ("slug", "destination")


@admin.register(Click)
class ClickAdmin(admin.ModelAdmin):
    # Use ONLY real fields from your Click model
    # (link, device, country, ip, created_at – adjust if needed)
    list_display = ("link", "device", "country", "ip", "created_at")
    list_filter = ("device", "country", "created_at")
    search_fields = ("ip", "user_agent")
