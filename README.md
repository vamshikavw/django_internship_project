🌐 Django URL Shortener + Analytics Dashboard — Internship Project

A complete Django-based URL Shortener website built as part of the O(1) Coding Club Internship.
This project includes a custom dashboard, analytics tracking, device & country insights, and a fully responsive frontend with animations.

🚀 Features
✅ 1. URL Shortener

Create custom short URLs

Auto-redirect to destination

Custom slug support

Track number of visits

✅ 2. Full Analytics Dashboard

Bar chart showing country-wise clicks

Pie chart showing device distribution

Automatic detection of desktop/mobile

IP logging & basic geo-tagging

Analytics for each short link

All-links table view

✅ 3. Internship Task Dashboard

Beautiful animated dashboard including:

Personalized greeting

Current date and time

Random motivational quote

Topics covered

Quick navigation buttons

Link creation form

✅ 4. Modern Frontend

Custom-designed templates

Smooth animations (CSS + transitions)

SVG illustrations

Bootstrap UI support

Fully responsive on desktop/mobile

📁 Project Structure
internship_project/
│── internship_project/       # Main project settings
│── main/                     # Core Django app
│   │── models.py             # Database Models
│   │── admin.py              # Admin panel customization
│   │── views.py              # Application logic
│   │── urls.py               # App URL routes
│   │── templates/main/       # All HTML files
│   │── static/main/          # CSS, images, SVGs
│── manage.py                 # Django entry point
│── .gitignore                # Ignore venv, cache, DB
│── README.md                 # (This file)

🛠️ Technologies Used

Python 3.14

Django 5.2

SQLite (default)

Bootstrap

Chart.js

HTML, CSS, JavaScript

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO

2️⃣ Create Virtual Environment
python -m venv .venv

3️⃣ Activate Virtual Environment

Windows:

.venv\Scripts\activate

4️⃣ Install Dependencies
pip install django

5️⃣ Run Migrations
python manage.py migrate

6️⃣ Start Server
python manage.py runserver

🌍 Available Pages (URLs)
🔸 1. Home Page — Landing Page
http://127.0.0.1:8000/

🔸 2. Internship Dashboard (task page)
http://127.0.0.1:8000/task/

🔸 3. All Analytics (table)
http://127.0.0.1:8000/all-analytics/

🔸 4. Single Link Analytics (charts)
http://127.0.0.1:8000/analytics/<slug>/

🔸 5. Admin Panel
http://127.0.0.1:8000/admin/

📊 Screenshots (Add Your Images Here)

You can add your screenshots like this:

![Dashboard](static/main/screenshot-dashboard.png)
![Analytics Page](static/main/screenshot-analytics.png)

🏁 Conclusion

This project demonstrates:

Django backend development

URL routing + database models

Data visualization with charts

UI/UX design using HTML/CSS

Clean project structure

Perfect to show during internship interviews or as a portfolio project.
