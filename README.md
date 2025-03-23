# Digital Notebook System Documentation

## Version: 1.0.0  
## Author: [DevWithShams](https://github.com/devwithshams/digital-notebook)

---

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [System Architecture](#system-architecture)
4. [Database Schema](#database-schema)
5. [Installation Guide](#installation-guide)
6. [API Specifications](#api-specifications)
7. [Authentication & Security](#authentication--security)
8. [Deployment](#deployment)
9. [Testing Strategy](#testing-strategy)
10. [Troubleshooting](#troubleshooting)
11. [Contributing](#contributing)
12. [License](#license)

---

## Overview

The **Digital Notebook System** is a cloud-based note-taking and collaboration platform designed to replace traditional notebooks. It allows users to create, edit, and share rich-text notes in real-time with seamless synchronization across devices.

### Tech Stack:
- **Backend**: Django, DRF, PostgreSQL, Redis
- **Frontend**: React.js, Quill.js
- **Infrastructure**: AWS S3, PythonAnywhere
- **Authentication**: JWT, OAuth (Google, GitHub)

---

## Features

| Feature               | Description |
|----------------------|-------------|
| **Rich Text Editing** | Advanced note-taking with markdown and image embedding |
| **Real-Time Collaboration** | Multi-user live editing with WebSockets |
| **Advanced Search** | Full-text search with filters (tags, date, content) |
| **Cloud Storage** | Secure AWS S3 storage for images and files |
| **User Roles** | Owner, Editor, Viewer with permission-based access |

---

## System Architecture

### Backend Components:
1. **Django REST Framework** - Handles API endpoints
2. **PostgreSQL** - Relational database for storing notes
3. **Redis + Celery** - Manages background tasks (notifications, indexing)

### Frontend Components:
1. **React.js** - Interactive user interface
2. **Quill.js** - Rich text editor for formatting notes

### Data Flow:
1. **User Requests** - Frontend interacts with Django REST API
2. **Processing** - API fetches data, applies business logic, stores in PostgreSQL
3. **Storage** - Files and images are stored securely in AWS S3
4. **Notifications** - WebSockets notify users of real-time changes

---

## Database Schema

### Table: `notes`
| Column Name | Type | Description |
|------------|------|-------------|
| `id` | UUID | Unique identifier |
| `title` | VARCHAR(200) | Note title |
| `content` | TEXT | Rich text content |
| `created_at` | TIMESTAMP | Timestamp when note was created |
| `updated_at` | TIMESTAMP | Timestamp of last update |
| `user_id` | UUID (FK) | Foreign key referencing `users` table |

### Table: `collaborators`
| Column Name | Type | Description |
|------------|------|-------------|
| `note_id` | UUID (FK) | Associated note ID |
| `user_id` | UUID (FK) | Collaborator's user ID |
| `permission` | ENUM | `view` or `edit` access |

---

## Installation Guide

### Prerequisites
- Python 3.8+
- Node.js 16+
- PostgreSQL
- Redis (for async tasks)

### Backend Setup
```bash
# Clone repository
git clone https://github.com/devwithshams/digital-notebook.git
cd digital-notebook/backend

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

### Frontend Setup
```bash
cd ../frontend

# Install dependencies
npm install

# Start development server
npm start
```

---

## API Specifications

### Authentication
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/auth/register/` | POST | User registration |
| `/api/auth/login/` | POST | User login & JWT generation |
| `/api/auth/logout/` | POST | Logout & invalidate token |

### Notes Management
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/notes/` | GET | Retrieve all notes |
| `/api/notes/{id}/` | GET | Retrieve a single note |
| `/api/notes/create/` | POST | Create a new note |
| `/api/notes/{id}/update/` | PUT | Update a note |
| `/api/notes/{id}/delete/` | DELETE | Delete a note |

---

## Authentication & Security
- **JWT-Based Authentication**: Secure login system using Django SimpleJWT
- **OAuth Support**: Login via Google/GitHub (optional)
- **Role-Based Access Control (RBAC)**:
  - **Owner**: Full control over notes
  - **Editor**: Edit permissions
  - **Viewer**: Read-only access

**Security Measures:**
- AES-256 encryption for stored data
- HTTPS/TLS 1.3 for secure communication
- Rate-limiting (100 requests/min) to prevent abuse

---

## Deployment

### Docker Deployment
```bash
# Build and run containers
docker-compose up --build
```

### PythonAnywhere Deployment
1. Clone repository
2. Install dependencies
3. Configure `.env` file
4. Run migrations & collect static files

---

## Testing Strategy

| Test Type | Tool | Coverage |
|-----------|------|----------|
| Unit Tests | Pytest | 90% |
| API Tests | DRF TestCase | Critical API endpoints |
| Performance | Locust | Handles 1k+ users |

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Cannot connect to database | Check PostgreSQL credentials in `.env` |
| Notes not saving | Verify Redis is running for Celery tasks |
| Authentication fails | Ensure JWT secret key is correct |

---

## Contributing

1. Fork the repository
2. Create a new branch (`feature/new-feature`)
3. Commit changes (`git commit -m 'Added new feature'`)
4. Push to branch and create a PR

---

## License

This project is licensed under the **MIT License**.

**Repository**: [GitHub - DevWithShams](https://github.com/devwithshams/digital-notebook)
