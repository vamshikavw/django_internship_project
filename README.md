# Django URL Shortener & Analytics Dashboard

A mini web application built with **Django** as part of the **O(1) Coding Club Internship**.  
It lets you:

- Create **custom short URLs** (like `my-link`) for any long URL  
- Track **click analytics** (countries & device types)  
- View a **summary dashboard** with a motivational quote and internship details  

---

## 🚀 Features

### 🧩 1. URL Shortener
- Convert any **long URL** into a **short, readable** link
- Use your own custom **slug** (e.g. `cc-ranklist`, `my-portfolio`)
- Duplicate slugs are handled safely by updating or showing analytics

### 📊 2. Analytics Dashboard
For each short link, you can see:

- Total clicks
- Clicks grouped by **country**
- **Device breakdown**: Desktop vs Mobile
- Visualized using **Chart.js** bar & pie charts

There is also a **“All Links Analytics”** page that shows:
- All created short links
- Their destination URL
- Total number of clicks
- Quick link to each link’s analytics page

### 🎨 3. Internship Task Dashboard (`/task/`)
A custom-designed **Task Dashboard page** that includes:

- Internship title and student name  
- Current date & time  
- A **random motivational quote** from the database  
- Topics covered in the project  
- Quick navigation buttons:
  - Open URL shortener landing page
  - Open all analytics page
  - Open example analytics for a known slug

The dashboard uses **CSS animations, gradients, and a card layout** to feel like a modern product page.

---

## 🛠 Tech Stack

- **Backend:** Django 5.x (Python)
- **Frontend:** HTML, CSS, Bootstrap, Chart.js
- **Database:** SQLite (default Django DB for development)
- **Other:** Django Admin for internal management

---

## 📂 Project Structure

```text
django_internship_project/
│
├── manage.py
├── db.sqlite3
├── internship_project/        # Django project settings, URLs, WSGI
│   └── urls.py                # Root URL configuration
│
├── main/                      # Main application
│   ├── models.py              # MotivationalQuote, Link, Click models
│   ├── views.py               # Task dashboard, URL shortener, analytics views
│   ├── urls.py                # App URLs (/, /task/, /r/<slug>/, /analytics/, etc.)
│   ├── admin.py               # Admin registrations for all models
│   ├── templates/
│   │   └── main/
│   │       ├── index.html         # URL shortener landing page
│   │       ├── task.html          # Internship dashboard page
│   │       ├── analytics.html     # Per-link analytics with charts
│   │       └── all-analytics.html # List of all links + their stats
│   └── static/
│       └── main/
│           ├── style.css          # Custom styling & animations
│           ├── bootstrap.min.css  # Bootstrap CSS
│           ├── hero-landing.svg   # Landing page illustration
│           ├── hero-task.svg      # Task page illustration (if used)
│           ├── Rebrandly.png      # Logo image
│           └── copy-icon.png      # Icon for features cards
