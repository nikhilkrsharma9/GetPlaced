# GetPlaced

## Introduction
GetPlaced is a Django-based job portal designed to connect students, colleges, and companies. It allows students to apply for jobs, colleges to manage student data, and companies to post job openings.

## Features
- User authentication (students, colleges, companies)
- Job posting and application system
- College and company profile management
- Student profile with image upload
- Admin verification for colleges
- Media support for logos and images

## Prerequisites
- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

## Install Modules
- Django
  cmd : "pip install django"

- Pillow
  cmd : "pip install Pillow"

## Installation
1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd GetPlaced
   ```
2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```
3. **Install dependencies (Django and Pillow):**
   ```sh
   pip install django pillow
   ```

## Running the Project
1. **Navigate to the project directory:**
   ```sh
   cd job_portal
   ```
2. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```
3. **Create a superuser (admin):**
   ```sh
   python manage.py createsuperuser
   ```
4. **Run the development server:**
   ```sh
   python manage.py runserver
   ```
5. **Access the portal:**
   Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Project Structure
- `job_portal/` - Django project root
  - `manage.py` - Django management script
  - `job_portal/` - Project settings and URLs
  - `portal/` - Main app (models, views, templates, static files)
  - `media/` - Uploaded images and logos
  - `static/` - Static files (CSS, JS, images)

## How It Works
- Users register as students, colleges, or companies.
- Colleges and companies are verified by the admin.
- Companies post jobs; students apply for jobs.
- Colleges manage student data and verify student profiles.
- Admin oversees the platform and manages verifications.

## Notes
- Make sure to configure your database and media/static paths as needed in `settings.py`.
- For production, set `DEBUG = False` and configure allowed hosts and static/media file serving.

## License
This project is for educational purposes.

#Project group
