# Perspectum Django Project

This is a Django project located in the `/src` directory. Below are the detailed instructions to set up and run the project.

## Prerequisites

- Python 3.x
- pip (Python package installer)
- virtualenv (optional but recommended)

## Setup Instructions

1. **Create and activate a virtual environment (optional but recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install the required packages:**

   ```bash
   python -m ensurepip --upgrade
   pip install -r requirements.txt
   ```

3. **Apply the migrations:**

   ```bash
   python manage.py migrate
   ```

4. **Load the data:**

   ```bash
   python manage.py load_data
   ```

5. **Create a superuser (optional but recommended for accessing the admin interface):**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

7. **Access the application:**

   Open your web browser and go to `http://127.0.0.1:8000/leaderboard`.

## Project Structure

- `manage.py`: Command-line utility for administrative tasks.
- `perspectum/`: Main project directory.
- `app_name/`: Replace with your actual app name(s).
  - `migrations/`: Database migrations.
  - `static/`: Static files (CSS, JavaScript, images).
  - `templates/`: HTML templates.
  - `views.py`: View functions.
  - `models.py`: Database models.
  - `urls.py`: URL declarations.
  - `admin.py`: Admin interface configuration.
  - `apps.py`: Application configuration.

## Additional Commands

- **Run tests:**

  ```bash
  python manage.py test
  ```
