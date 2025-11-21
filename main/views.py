from datetime import datetime

from django.db.models import Count
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404

from .models import MotivationalQuote, Link, Click


# --------------- TASK DASHBOARD ----------------
def task_view(request):
    quote_obj = MotivationalQuote.objects.order_by("?").first()

    topics = [
        "Database handling",
        "CRUD operations on database",
        "Django ORM (Object-Relational Mapper)",
        "Django Models & Model Fields",
        "Django Admin & Superuser",
        "URL Shortener & Analytics",
    ]

    context = {
        "internship_title": "🌐 Django Internship - URL Shortener",
        "student_name": "Vamshika Wagangeri",
        "message": "Welcome to your personalized Django Internship dashboard!",
        "today": datetime.now(),
        "quote": quote_obj.text if quote_obj else "Keep coding, the best is yet to come! 💻",
        "topics": topics,
    }
    return render(request, "main/task.html", context)


# --------------- LANDING / SHORTENER PAGE ---------------
def index(request):
    if request.method == "POST":
        slug = request.POST.get("slug", "").strip()
        dest = request.POST.get("destination", "").strip()

        if not slug or not dest:
            return HttpResponseBadRequest("Slug & Destination required")

        Link.objects.update_or_create(slug=slug, defaults={"destination": dest})
        return redirect("analytics", slug=slug)

    return render(request, "main/index.html")


# --------------- REDIRECT + CLICK TRACKING ---------------
def go(request, slug):
    link = get_object_or_404(Link, slug=slug)

    user_agent = request.META.get("HTTP_USER_AGENT", "") or ""
    device = "mobile" if "Mobi" in user_agent else "desktop"
    ip = request.META.get("REMOTE_ADDR")
    country = "India" if ip else "Unknown"  # simple placeholder

    Click.objects.create(
        link=link,
        ip=ip,
        user_agent=user_agent,
        device=device,
        country=country,
    )
    return redirect(link.destination)


# --------------- ALL LINKS ANALYTICS ---------------
def all_analytics(request):
    links = Link.objects.annotate(total=Count("clicks")).order_by("-total", "-created_at")
    return render(request, "main/all-analytics.html", {"links": links})


# --------------- SINGLE LINK ANALYTICS ---------------
def analytics(request, slug):
    link = get_object_or_404(Link, slug=slug)

    by_country = list(
        link.clicks.values_list("country").annotate(c=Count("id")).order_by("-c")
    )
    countries = [c for c, _ in by_country] or ["No data"]
    clicks = [n for _, n in by_country] or [0]

    desktop = link.clicks.filter(device="desktop").count()
    mobile = link.clicks.filter(device="mobile").count()

    ctx = {
        "slug": slug,
        "link": link,
        "total_clicks": link.clicks.count(),
        "countries": countries,
        "clicks": clicks,
        "desktop": desktop,
        "mobile": mobile,
    }
    return render(request, "main/analytics.html", ctx)
def learn(request):
    sections = [
        {
            "title": "Database Handling",
            "points": [
                "We work with a relational database made of tables.",
                "Each table has rows and columns.",
                "We usually talk to the DB using SQL (Structured Query Language).",
            ],
        },
        {
            "title": "CRUD Operations",
            "points": [
                "Create – insert new rows into the table.",
                "Read – fetch data using queries and filters.",
                "Update – modify existing rows.",
                "Delete – remove rows from the table.",
            ],
        },
        {
            "title": "Django ORM",
            "points": [
                "ORM = Object-Relational Mapper.",
                "You write Python classes instead of raw SQL.",
                "Django converts your queries to SQL behind the scenes.",
            ],
        },
        {
            "title": "Django Models",
            "points": [
                "A model class maps to a single database table.",
                "Fields like CharField, IntegerField, URLField represent columns.",
                "Migrations keep the database schema in sync with models.",
            ],
        },
        {
            "title": "Django Admin & Superuser",
            "points": [
                "Admin uses your models to create a powerful dashboard.",
                "You create a superuser with `python manage.py createsuperuser`.",
                "You can create, edit and delete objects from `/admin/`.",
            ],
        },
        {
            "title": "Must-Do Commands",
            "points": [
                "`python manage.py makemigrations` – prepare DB changes.",
                "`python manage.py migrate` – apply migrations to DB.",
            ],
        },
    ]
    return render(request, "main/learn.html", {"sections": sections})

