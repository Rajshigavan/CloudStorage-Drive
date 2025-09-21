# Cloud Storage Application  

A Django-based cloud storage system that allows users to upload, manage, and organize files in a structured way, similar to Google Drive.  

## 🚀 Features  
- User authentication (signup, login, logout).  
- Upload, view, update, and delete files.  
- Create, update, and delete folders.  
- Secure file storage using Django’s media handling.  
- Clean UI with HTML templates.  

## 📂 Project Structure  
```
cloudsotrage/
│── manage.py
│── db.sqlite3
│
├── drive/               # Django project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── driveapp/            # Core application
│   ├── models.py        # Database models for files/folders
│   ├── views.py         # Business logic
│   ├── urls.py          # App routes
│   ├── templates/       # HTML templates (UI)
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── signup.html
│   │   ├── folder.html
│   │   ├── delete_folder.html
│   │   └── update_folder.html
│   └── admin.py
│
├── MediaFiles/          # Uploaded user files
│   └── Files/
│
└── venv/                # Virtual environment
```

## ⚙️ Installation  

1. Clone the repository:  
   ```bash
   git clone <your-repo-url>
   cd cloudsotrage
   ```

2. Create and activate a virtual environment:  
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:  
   ```bash
   pip install django
   ```

4. Apply migrations:  
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (optional, for admin panel):  
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:  
   ```bash
   python manage.py runserver
   ```

7. Open in browser:  
   ```
   http://127.0.0.1:8000/
   ```

## 🖥️ Usage  
- Sign up for a new account or log in.  
- Upload and manage files.  
- Create and organize folders.  
- Delete or update existing files/folders.  

## 🔐 Admin Panel  
Django’s built-in admin panel is available at:  
```
http://127.0.0.1:8000/admin
```

## 📌 Future Improvements  
- Add support for sharing files via links.  
- Implement file preview for documents and images.  
- Add drag-and-drop file uploads.  
- Build a mobile-friendly UI.  
