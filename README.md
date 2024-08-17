# Project Management Backend

## Overview

The Project Management Backend is a web application backend developed using Django and Django Rest Framework (DRF). It provides a comprehensive API for managing project workflows, including task assignments, project timelines, and team collaboration. This backend serves as the core component for handling project-related data and operations.

## Repository Link

[GitHub Repository](https://github.com/Lokeshsejuwal99/Project_Management)

## Purpose and Goals

1. **Task Management**: Allow users to create, assign, update, and track tasks within projects through a RESTful API.
2. **Project Tracking**: Manage project details, deadlines, and progress with CRUD operations.
3. **Team Collaboration**: Facilitate collaboration among team members with API endpoints for team management.
4. **Reporting**: Provide endpoints for generating reports on project progress and task completion.

## Key Features

- **User Authentication**: Secure authentication and authorization using Django's built-in user model and DRF's token-based authentication.
- **Task Management**: Full CRUD functionality for tasks including creation, retrieval, updating, and deletion.
- **Project Management**: Endpoints to manage project details, timelines, and status updates.
- **Team Collaboration**: Manage team members and their roles within projects.
- **Reporting**: Generate project and task reports through API endpoints.

## Technology Stack

- **Backend**: Django
- **API Framework**: Django Rest Framework (DRF)
- **Database**: PostgreSQL/MySQL (or the database used)
- **Authentication**: Token-based authentication with DRF

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/lokeshsejuwal99/Project_Management.git


2. **Navigate to the Project Directory**:
   ```bash
   cd Project_Management


3. **Create a Virtual Environment (Optional but recommended)**:
   ```bash
   python -m venv venv

4. **Activate the Virtual Environment**:
* on windows:
     ```bash
  venv\Scripts\activate

* On macOS/Linux:
    ```bash
  source venv/bin/activate

5. **Install Dependencies**:
   ``` bash
   pip install -r requirements.txt


6. **Apply Migrations**:
   ``` bash
   python manage.py makemigrations
   python manage.py migrate
   
6. **Create a Superuser (For accessing the Django admin)**:
   ``` bash
   python manage.py createsuperuser

7. **Run the Development Server**:
   ``` bash
   python manage.py runserver

8. **Access the Application**:
   Open your browser and go to http://127.0.0.1:8000 to access the API.
