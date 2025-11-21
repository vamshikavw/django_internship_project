# 🌐 Django URL Shortener + Analytics Dashboard  
### Internship Project – O(1) Coding Club

This is a complete **URL Shortening Web Application** built using **Django**, featuring custom short links, click-tracking analytics, device insights, country-wise charts, and a beautiful animated dashboard.

This project was developed as a part of the **O(1) Coding Club Internship Program**, and includes all tasks from Backend → Frontend → Analytics → UI Enhancements → Deployment-Ready Code.

---

## 🚀 Features

### ✅ URL Shortener
- Create custom short links (example: `/r/my-link`)
- Auto-redirect to the destination URL
- Custom slug creation (no random strings)
- Duplicate slug protection

### 📊 Analytics Dashboard
- Click count tracking
- Device type detection (Mobile / Desktop)
- Country tracking (basic)
- Chart.js bar & pie charts
- Per-link analytics page
- All-links analytics list

### 🎨 Beautiful Frontend UI
- Animated Dashboard (`/task`)
- Clean Bootstrap-based landing page
- Custom static images (SVG icons created manually)
- Responsive design
- Smooth fade-in animations

### 🗂 Admin Panel
- Manage:
  - Links  
  - Click records  
  - Motivational quotes  
- Admin UI cleaned for internship requirements

---

## 🏛 Tech Stack

- **Backend:** Django (Python 3.14)
- **Frontend:** HTML, CSS, Bootstrap 5, Chart.js, SVG Icons
- **Database:** SQLite 3
- **Tools:** Git, GitHub, VS Code

---

## 📁 Project Structure

```
django_internship_project/
│── internship_project/        # Main project folder
│── main/                      # Django app (URL Shortener + Analytics)
│   │── migrations/
│   │── static/main/           # CSS, JS, Images
│   │── templates/main/        # HTML files
│   │── models.py              # Link, Click, Quote models
│   │── views.py               # All backend logic
│   │── urls.py                # Route definitions
│   └── admin.py               # Admin customizations
│── db.sqlite3                 # Local database
│── manage.py
│── README.md                  # (This file)
└── .gitignore
```

---

## ▶️ How to Run the Project Locally

### 1️⃣ Activate Virtual Environment
```bash
venv\Scripts\activate
```

### 2️⃣ Install Dependencies (if needed)
```bash
pip install django
```

### 3️⃣ Run Server
```bash
python manage.py runserver
```

### 4️⃣ Open in Browser
- Dashboard → http://127.0.0.1:8000/task/
- URL Shortener → http://127.0.0.1:8000/
- All Analytics → http://127.0.0.1:8000/all-analytics/
- Admin Panel → http://127.0.0.1:8000/admin/

---

## 🖼 Screenshots  
*(Add screenshots here once uploaded to GitHub)*  

Example (after uploading images):
```
![Dashboard](static/screenshots/dashboard.png)
![Analytics](static/screenshots/analytics.png)
```

---

## 📌 Internship Tasks Completed

✔ Full Backend (Models, Views, Redirect Logic, Validations)  
✔ Django Admin Configuration  
✔ URL Shortening + Redirect + Tracking  
✔ All Analytics Page  
✔ Individual Analytics Page with Charts  
✔ Beautiful Frontend + Animations (Task Dashboard)  
✔ SVG Icons & Images  
✔ Static Files Setup  
✔ GitHub Repository Integration  

---

## 🤝 Contribution

This project is part of an internship, but improvements are welcome.  
Create a pull request if you'd like to add enhancements.

---

## 📄 License

This project is released for educational purposes as part of  
**O(1) Coding Club Internship Program**.

---

## 👩‍💻 Author  
**Vamshika Wagangeri**  
Django Intern – O(1) Coding Club  
GitHub: [@vamshikavw](https://github.com/vamshikavw)
