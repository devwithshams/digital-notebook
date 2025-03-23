# Digital Notebook System Documentation

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Installation Guide](#installation-guide)
4. [Database Schema](#database-schema)
5. [API Documentation](#api-documentation)
6. [Authentication & Security](#authentication--security)
7. [Deployment Guide](#deployment-guide)
8. [Testing Strategy](#testing-strategy)
9. [Contributing Guide](#contributing-guide)
10. [Support & Troubleshooting](#support--troubleshooting)

---

## Overview
The **Digital Notebook System** is a cloud-based application for creating, organizing, and collaborating on notes. Built with Django and React, it provides a seamless note-taking experience with features like **rich text editing, real-time collaboration, and cloud storage**.

### **Tech Stack**
- **Backend**: Django, Django REST Framework (DRF), PostgreSQL, Redis.
- **Frontend**: React.js, Quill.js.
- **Infrastructure**: AWS S3, PythonAnywhere, Celery.
- **Authentication**: JWT-based authentication.

---

## Features
| Feature               | Description                                    |
|-----------------------|------------------------------------------------|
| **Rich Text Editing** | WYSIWYG editor, markdown support.             |
| **Real-Time Sync**    | Live updates, comments, and mentions.         |
| **Advanced Search**   | Full-text search with filters.                |
| **Cloud Storage**     | Secure AWS S3 integration for media.          |
| **User Roles**        | Admin, Owner, Editor, Viewer.                 |

---

## Installation Guide
### Prerequisites
- Python 3.9+
- Node.js 16+
- PostgreSQL
- Redis
- Virtual Environment (venv)

### **Backend Setup**
```bash
# Clone repository
git clone https://github.com/devwithshams/digital-notebook.git
cd digital-notebook/backend

# Create virtual environment and activate it
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start the server
python manage.py runserver
```

### **Frontend Setup**
```bash
cd ../frontend

# Install dependencies
npm install

# Start the development server
npm start
```

---

## Database Schema
### **Relational Model (PostgreSQL)**
#### **Table: `notes_note`**
| Field         | Type       | Description                     |
|--------------|------------|---------------------------------|
| `id`         | UUID       | Primary key.                    |
| `user_id`    | UUID (FK)  | Owner of the note.              |
| `title`      | VARCHAR    | Note title (max 200 chars).     |
| `content`    | TEXT       | Formatted text/content.         |
| `created_at` | TIMESTAMPTZ| Auto-generated timestamp.       |

#### **Table: `collaborators`**
| Field             | Type       | Description                     |
|------------------|------------|---------------------------------|
| `note_id`        | UUID (FK)  | Note being shared.              |
| `user_id`        | UUID (FK)  | Collaborator’s user ID.         |
| `permission_level`| ENUM       | `view` or `edit`.               |

---

## API Documentation
### **Endpoints**
| Endpoint                 | Method | Auth Required | Description                 |
|--------------------------|--------|--------------|-----------------------------|
| `/api/auth/register/`    | POST   | No           | Register a new user.        |
| `/api/auth/login/`       | POST   | No           | User login.                 |
| `/api/notes/`            | GET    | Yes          | List all user notes.        |
| `/api/notes/{note_id}/`  | PUT    | Yes          | Update a specific note.     |

**Example Request:**
```bash
curl -X POST http://api.notebook.com/auth/login/ \  
  -H "Content-Type: application/json" \  
  -d '{"email": "user@example.com", "password": "pass123"}'
```

---

## Authentication & Security
- **JWT Authentication**: Secure login and session management.
- **Data Encryption**: AES-256 for data at rest, HTTPS/TLS 1.3 for transit.
- **Rate Limiting**: 100 requests per minute per user.
- **SQL Injection Prevention**: Django ORM handles queries securely.

---

## Deployment Guide
### **PythonAnywhere Setup**
1. Clone the repository.
2. Set up a virtual environment.
3. Configure `settings.py` for production.
4. Apply database migrations.
5. Start the WSGI application.

### **Frontend Deployment (Vercel)**
1. Push code to GitHub.
2. Connect repository on Vercel.
3. Deploy automatically from `main` branch.

---

## Testing Strategy
### **Test Types**
| Type              | Tools            | Coverage Target |
|------------------|-----------------|-----------------|
| Unit Tests       | Pytest           | 90%             |
| Integration Tests| DRF APITestCase  | Critical flows  |
| Performance Tests| Locust           | 1k+ users       |

**Example Test:**
```python
# tests/test_notes.py
def test_note_creation():
    note = Note.objects.create(title="Test", content="...")
    assert note.title == "Test"
```

---

## Contributing Guide
1. **Fork the repository** on GitHub.
2. **Create a feature branch**: `git checkout -b feature-new-feature`.
3. **Commit changes**: `git commit -m "Added new feature"`.
4. **Push to GitHub**: `git push origin feature-new-feature`.
5. **Create a Pull Request** on GitHub.

---

## Support & Troubleshooting
### **Common Issues**
| Issue                  | Solution                              |
|------------------------|--------------------------------------|
| Static files missing  | Run `python manage.py collectstatic`. |
| Database connection   | Check `.env` credentials.            |

### **Contact**
- **Email**: support@notebook.com
- **Community Forum**: [forum.notebook.com](https://forum.notebook.com)

---

**License**: MIT  
**Repository**: [GitHub](https://github.com/devwithshams/digital-notebook)

