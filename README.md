# Blog

A full-featured blog web application built with **Django**. Visitors can browse and search posts, filter by category, register, log in and comment. Logged-in users get a custom dashboard to manage categories, blog posts and users.

**Live demo:** https://darshankg.pythonanywhere.com/

## Features

**Public site**
- Home page with featured posts, latest posts and an About section
- Single post page with a featured image and slug-based URLs
- Browse posts by category
- Keyword search across title, short description and body (published posts only)
- User registration, login and logout
- Comments on posts (login required to comment)
- Custom 404 page
- Social links in the site footer, managed from the admin panel

**Dashboard** (`/dashboard/`, login required)
- Overview with total category and post counts
- Category management: add, edit, delete
- Blog post management: add, edit, delete, with image upload
- Draft / Published status and a "featured" flag on every post
- User management: add, edit, delete, with staff and superuser permissions

**Admin panel** (`/admin/`)
- Manage the About section and social links through Django admin

## Tech Stack

| Area | Technology |
|------|------------|
| Language | Python |
| Framework | Django 5.2 |
| Database | SQLite |
| Forms | django-crispy-forms with crispy-bootstrap4 |
| Images | Pillow |
| Frontend | Django templates, Bootstrap 4, custom CSS |

## Project Structure

```
Blog/
├── blog_main/        # Project settings, root URLs, home/auth views, static files
├── blogs/            # Models (Category, Blog, Comment), post/category/search views
├── dashboards/       # Dashboard views, forms and URLs (categories, posts, users)
├── assignments/      # About and SocialLink models
├── templates/        # HTML templates (public pages and dashboard/)
├── media/uploads/    # Uploaded featured images
├── manage.py
├── requirements.txt
└── db.sqlite3
```

## Getting Started

### Prerequisites
- Python 3.10 or newer
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Darshankg18/Blog.git
cd Blog

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
source venv/bin/activate       # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply database migrations
python manage.py migrate

# 5. Create an admin account
python manage.py createsuperuser

# 6. Start the development server
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Usage

1. Log in at `/admin/` with your superuser account.
2. Under **About** and **Social links**, add the content for the home page and footer.
3. Go to `/login/` and sign in to reach the dashboard at `/dashboard/`.
4. Create a **category**, then add a **post**. Set its status to *Published* to make it visible, and tick *Is featured* to show it in the featured section on the home page.

## URL Overview

| URL | Description |
|-----|-------------|
| `/` | Home page |
| `/blogs/<slug>/` | Single post and comments |
| `/blogs/search/?keyword=...` | Search results |
| `/category/<id>/` | Posts in a category |
| `/register/`, `/login/`, `/logout/` | Authentication |
| `/dashboard/` | Dashboard home |
| `/dashboard/categories/` | Manage categories |
| `/dashboard/posts/` | Manage posts |
| `/dashboard/users/` | Manage users |
| `/admin/` | Django admin |

## Data Models

- **Category**: name, created and updated timestamps
- **Blog**: title, slug, category, author, featured image, short description, body, status (Draft or Published), featured flag
- **Comment**: user, blog, comment text
- **About**: heading and description for the home page
- **SocialLink**: platform name and URL

## Notes for Production

This project is set up for local development. Before deploying:
- Move `SECRET_KEY` out of `settings.py` into an environment variable
- Set `DEBUG = False` and configure `ALLOWED_HOSTS`
- Use a production database and serve media files through your web server

## Author

[Darshankg18](https://github.com/Darshankg18)
