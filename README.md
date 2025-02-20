# Best Cars Dealership - Django Application

## Overview

This project is a Django-based web application for the Best Cars Dealership. It provides a simple online presence with a homepage, an "About Us" page, and a "Contact Us" page.

## Prerequisites

Before you begin, ensure you have the following installed:

*   **Python:** Python 3.x is required.
*   **pip:** Python package installer (usually comes with Python).
*   **virtualenv:** (Optional but recommended) For creating isolated Python environments.

## Setup Instructions

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/JayJay247in/-Full-Stack-Application_part1.git
    cd Full-Stack-Application_part1
    ```

    Replace `https://github.com/JayJay247in/-Full-Stack-Application_part1.git` with the URL of your forked repository.
    Replace `Full-Stack-Application_part1` with the name of the project directory.

2.  **Create a Virtual Environment (Recommended):**

    ```bash
    python3 -m venv djangoenv
    source djangoenv/bin/activate  # On Linux/macOS
    # djangoenv\Scripts\activate  # On Windows
    ```

3.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Static Files:**

    *   Ensure that `STATICFILES_DIRS` and `DIRS` (under `TEMPLATES`) in `djangoproj/settings.py` are configured to point to the `frontend/static` directory.
        ```python
        TEMPLATES = [
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [
                    os.path.join(BASE_DIR, 'frontend/static')
                ],
                'APP_DIRS': True,
                'OPTIONS': {
                    'context_processors': [
                        'django.template.context_processors.debug',
                        'django.template.context_processors.request',
                        'django.contrib.auth.context_processors.auth',
                        'django.contrib.messages.context_processors.messages',
                    ],
                },
            },
        ]

        STATICFILES_DIRS = [
            os.path.join(BASE_DIR, 'frontend/static')
        ]
        ```

5.  **Database Migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6.  **Set `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS`:**

    *   In `djangoproj/settings.py`, set `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` to your application's URL.
        ```python
        ALLOWED_HOSTS = ['localhost', '<your_application_url>']
        CSRF_TRUSTED_ORIGINS = ['<your_application_url>']
        ```

## Running the Application

1.  **Start the Development Server:**

    ```bash
    python manage.py runserver
    ```

2.  **Access the Application:**

    Open your web browser and navigate to the address provided by the `runserver` command (usually `http://127.0.0.1:8000/`).

## Application Structure

The project has the following directory structure:
Use code with caution.
Markdown
Full-Stack-Application_part1/
├── server/
│ ├── djangoapp/ # Django Application
│ ├── djangoproj/ # Project Configuration
│ └── frontend/ # HTML, CSS, and JavaScript Front End
│ └── static/ # Static files (HTML, CSS, images)
├── manage.py # Django management script
├── README.md # This file
└── requirements.txt # Project dependencies

## Key Components

*   **djangoapp:** Contains the core Django application logic.
*   **djangoproj:** Contains the Django project settings and URL configurations.
*   **frontend:**  Contains the static HTML, CSS, and image files for the front end.
*   **`About.html`:** The "About Us" page.
*   **`Contact.html`:** The "Contact Us" page.
*   **`style.css`:** CSS stylesheet for styling the application.
*   **`requirements.txt`:** Lists the Python packages required for the project.

## Contributing

If you wish to contribute to this project, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Commit your changes with descriptive commit messages.
4.  Push your changes to your forked repository.
5.  Submit a pull request to the main repository.