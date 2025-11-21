from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("task/", views.task_view, name="task"),
    path("learn/", views.learn, name="learn"),  # 👈 new page
    path("r/<slug:slug>/", views.go, name="go"),
    path("all-analytics/", views.all_analytics, name="all_analytics"),
    path("analytics/<slug:slug>/", views.analytics, name="analytics"),
]
