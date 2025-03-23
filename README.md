# Digital Notebook System Documentation

## Version 1.0.0

---

## Table of Contents  
1. [Overview](#1-overview)  
2. [Features](#2-features)  
3. [System Architecture](#3-system-architecture)  
4. [Installation Guide](#4-installation-guide)  
5. [Database Schema](#5-database-schema)  
6. [API Documentation](#6-api-documentation)  
7. [Security & Authentication](#7-security--authentication)  
8. [Testing & Debugging](#8-testing--debugging)  
9. [Deployment Guide](#9-deployment-guide)  
10. [Troubleshooting](#10-troubleshooting)  
11. [License & Contact](#11-license--contact)  

---

## 1. Overview
The **Digital Notebook System** is a modern, cloud-based note-taking application designed for seamless organization, collaboration, and accessibility. Built with Django and React, the system allows users to create, edit, and share rich-text notes securely in real time.

**Key Goals:**
- User-friendly and intuitive note-taking experience.
- Scalable backend capable of handling large-scale data.
- Secure authentication and access control.
- Cloud storage for media and document attachments.

**Tech Stack:**
- **Backend:** Django, DRF, PostgreSQL, Redis, Celery.
- **Frontend:** React.js, Quill.js.
- **Infrastructure:** AWS S3, PythonAnywhere, Docker.

---

## 2. Features
### Core Functionalities
- **Rich Text Editing**: Markdown support, file embedding, text formatting.
- **Real-Time Collaboration**: Multi-user editing with WebSockets.
- **Advanced Search**: Full-text search with filters (tags, dates, etc.).
- **Role-Based Access**: User roles (Owner, Collaborator, Admin).
- **Cloud Storage**: Secure file and media storage via AWS S3.

### Security Features
- **JWT Authentication**: Secure user sessions.
- **Data Encryption**: AES-256 encryption for sensitive data.
- **Rate Limiting**: Prevent abuse with request throttling.

---

## 3. System Architecture
The system follows a **microservices-based architecture**, dividing core functionalities into modular services.

### High-Level Architecture
```
[ React Frontend ]  ---> [ Django API Server ] ---> [ PostgreSQL Database ]
                                      |---> [ Redis Cache ]
                                      |---> [ Celery Workers ]
                                      |---> [ AWS S3 Storage ]
```
- **Frontend**: React.js handles UI interactions and state management.
- **Backend**: Django REST Framework serves API endpoints.
- **Database**: PostgreSQL for structured data, Redis for caching.
- **Async Tasks**: Celery processes background jobs (e.g., email notifications).

---

## 4. Installation Guide
### Prerequisites
Ensure you have the following installed:
- **Python 3.8+**
- **Node.js 14+ & npm/yarn**
- **PostgreSQL 13+**
- **Redis 6+** (for caching and async tasks)

### Backend Setup
```bash
# Clone the repository
git clone https://github.com/devwithshams/digital-notebook.git
cd digital-notebook

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver
```

### Frontend Setup
```bash
cd frontend
npm install  # or yarn install
npm start    # or yarn start
```

---

## 5. Database Schema
### Notes Table (`notes_note`)
| Field       | Type         | Description                  |
|------------|------------|------------------------------|
| id         | UUID       | Primary key                  |
| user_id    | UUID (FK)  | Owner of the note            |
| title      | VARCHAR    | Note title (max 200 chars)   |
| content    | TEXT       | Formatted note text          |
| created_at | TIMESTAMPTZ| Auto-generated timestamp     |

---

## 6. API Documentation
### Authentication
#### Register User
**Endpoint:** `/api/auth/register/`
**Method:** `POST`
```json
{
  "email": "user@example.com",
  "password": "securepassword"
}
```

#### Login User
**Endpoint:** `/api/auth/login/`
**Method:** `POST`
```json
{
  "email": "user@example.com",
  "password": "securepassword"
}
```

**Response:**
```json
{
  "access_token": "eyJhbGci...",
  "refresh_token": "eyJhbGci..."
}
```

---

## 7. Security & Authentication
### Best Practices
- **Secure Password Storage:** Using Django’s PBKDF2 algorithm.
- **Token Expiry & Refresh:** JWT-based authentication with expiration policies.
- **Access Control:** Role-based permissions for note access.

---

## 8. Testing & Debugging
### Running Tests
```bash
# Run Django tests
pytest

# Run frontend tests
cd frontend
npm test
```

---

## 9. Deployment Guide
### Using PythonAnywhere
1. **Clone the repository**
```bash
git clone https://github.com/devwithshams/digital-notebook.git
```
2. **Install dependencies and configure environment variables.**
3. **Run Django migrations and start the server.**

### Docker Deployment
```bash
docker-compose up --build
```

---

## 10. Troubleshooting
| Issue                        | Solution                       |
|------------------------------|--------------------------------|
| Database connection error    | Check `.env` configuration.   |
| JWT Token Expired            | Re-authenticate and refresh.   |

---

## 11. License & Contact
- **License**: MIT
- **Author**: Shamsuddeen ([@devwithshams](https://github.com/devwithshams))
- **Repository**: [GitHub](https://github.com/devwithshams/digital-notebook)

