# WendePro Blog

A Django-based blog platform with comprehensive features for content management and user interaction.

## 1. Project Requirements

### User Authentication
- Users can sign up, log in, and log out
- Protected routes for authenticated users
- Admin panel for managing blog posts and users

### Blog Management
- CRUD operations for blog posts
- Support for titles, body content, images, and categories
- Rich text editor support (Markdown/WYSIWYG)
- Category and tag system
- Commenting system

### Responsive Design
- Mobile-friendly interface
- Built with Bootstrap/TailwindCSS

### SEO Optimization
- Meta descriptions
- SEO-friendly URLs
- Social media integration

### Deployment
- Ready for deployment to Heroku or DigitalOcean
- Production-grade setup with Gunicorn

## 2. Tech Stack

### Backend
- Django (Python)
- Django ORM
- Django REST Framework (optional)

### Frontend
- HTML, CSS, JavaScript
- Bootstrap/TailwindCSS
- jQuery

### Database
- Development: SQLite
- Production: PostgreSQL

### Authentication
- Django's built-in authentication
- Custom user models (as needed)

### Additional Libraries
- django-allauth: Authentication and social login
- django-crispy-forms: Enhanced form handling
- Pillow: Image processing
- django-markdownx/django-tinymce: Rich text editing

## 3. Folder Structure 
WendeProBlog/
│
├── wendeproblog/                  # Main Django app folder
│   ├── __init__.py
│   ├── settings.py                 # Django settings
│   ├── urls.py                     # URL routing for the app
│   ├── views.py                    # Views and logic for blog
│   └── wsgi.py                     # WSGI configuration for deployment
├── wendepro_app/                  # Main Django app folder
│   ├── migrations/                 # Django migrations folder
│   ├── __init__.py
│   ├── settings.py                 # Django settings
│   ├── urls.py                     # URL routing for the app
│   ├── views.py                    # Views and logic for blog
│   ├── models.py                   # Database models for the blog posts, comments, etc.
│   ├── admin.py                    # Admin configuration for managing models
│   ├── forms.py                    # Forms for post creation, editing, etc.
│   └── templates/                  # HTML templates for the blog
│       ├── base.html                # Base template for layout
│       ├── post_list.html           # Template for listing blog posts
│       ├── post_detail.html         # Template for single blog post
│       └── ...                      # Other templates (login, sign up, etc.)
│
├── static/                         # Static assets (CSS, JS, Images)
│   ├── css/
│   ├── js/
│   └── images/
│
├── media/                          # User-uploaded files (profile pictures, post images, etc.)
│
├── templates/                      # Global templates
│   ├── registration/               # User authentication templates (login, logout, etc.)
│   └── ...                         
│
├── manage.py                       # Django manage.py to run the server and manage the app
├── requirements.txt                # Python dependencies
└── .env                            # Environment variables
