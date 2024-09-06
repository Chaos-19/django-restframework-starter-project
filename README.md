# Django REST Framework Starter Project - Snippet Highlight API

This repository contains a Django REST Framework (DRF) starter project built by following the official DRF tutorial. The project is organized into six lessons, each placed in a separate branch, allowing you to follow the development process step by step. The project demonstrates the creation of an API for managing code snippets, with key features like authentication, serialization, and highlighting.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Lessons Overview](#lessons-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project provides a basic API for creating, reading, updating, and deleting (CRUD) code snippets. It highlights Django REST Framework's core concepts, including:

- Serializers
- API Views and Viewsets
- URL routing
- Authentication and permissions
- Browsable API

The project is structured around the official Django REST Framework tutorial, providing a hands-on guide for learning API development with DRF.

## Features

- **Snippet CRUD**: Manage code snippets through the API.
- **Syntax Highlighting**: Supports language-based syntax highlighting for code snippets.
- **Authentication**: Basic authentication for managing access to the API.
- **Browsable API**: User-friendly interface for exploring the API through the browser.
- **Pagination**: Easily paginate through snippet records.

## Lessons Overview

This project is broken into six lessons, each corresponding to a tutorial section from the [official Django REST Framework tutorial](https://www.django-rest-framework.org/tutorial/1-serialization/). Each lesson is on a separate branch, so you can check out each branch as needed:

1. **[Lesson 1 - Serialization](https://www.django-rest-framework.org/tutorial/1-serialization/):** Introduction to serializers and the basics of converting models to JSON format. Branch: `tutorial-1`
2. **[Lesson 2 - Requests and Responses](https://www.django-rest-framework.org/tutorial/2-requests-and-responses/):** Handling HTTP requests and responses in DRF. Branch: `tutorial-2`
3. **[Lesson 3 - Class-Based Views](https://www.django-rest-framework.org/tutorial/3-class-based-views/):** Building reusable views using Django's class-based views. Branch: `tutorial-3`
4. **[Lesson 4 - Authentication and Permissions](https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/):** Adding user authentication and permissions to the API. Branch: `tutorial-4`
5. **[Lesson 5 - Relationships and Hyperlinked APIs](https://www.django-rest-framework.org/tutorial/5-relationships-and-hyperlinked-apis/):** Creating relationships between models and using hyperlinked APIs. Branch: `tutorial-5`
6. **[Lesson 6 - Viewsets and Routers](https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/):** Simplifying view logic using viewsets and routers for automatic URL routing. Branch: `tutorial-6`

Each branch contains the implementation specific to that lesson, helping you to understand the incremental development of the project.

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Chaos-19/django-restframework-starter-project.git
   cd drf-starter-project
   ```

2. **Checkout a specific lesson branch:**

   ```bash
   git checkout tutorial-1  # Replace with the lesson branch you want to explore
   ```

3. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser for the admin interface:**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

   The API will be available at `http://127.0.0.1:8000/`.

## Usage

### Browsing the API

You can interact with the API via the browser using Django REST Framework's browsable API at:

- **Snippets List**: `http://127.0.0.1:8000/snippets/`
- **Snippet Details**: `http://127.0.0.1:8000/snippets/<id>/`

### Authentication

The API requires basic authentication for certain endpoints. You can log in with your superuser credentials.

## Project Structure

```
drf-starter-project/
├── mysite/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── snippets/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
├── manage.py
├── db.sqlite3
└── requirements.txt
```

- **mysite/**: The main project configuration directory.
- **snippets/**: Contains the core logic for the Snippet API (models, views, serializers).
- **manage.py**: A command-line utility for interacting with the project.
- **requirements.txt**: Lists the Python dependencies for the project.

## API Endpoints

- **GET /snippets/**: Retrieve a list of all snippets.
- **POST /snippets/**: Create a new snippet.
- **GET /snippets/{id}/**: Retrieve a specific snippet by ID.
- **PUT /snippets/{id}/**: Update a snippet by ID.
- **DELETE /snippets/{id}/**: Delete a snippet by ID.

### Authentication

- **Basic Authentication** is used to secure certain endpoints.
- Users can log in with the admin credentials to access protected routes.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
