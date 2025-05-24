# Task Manager API

A comprehensive task management REST API built with Django and Django REST Framework, featuring JWT authentication, user management, and full CRUD operations for todos.

## 🚀 Features

- **User Management**
  - User registration and authentication
  - Custom user model with email-based login
  - JWT token-based authentication
  - User profile management

- **Task Management**
  - Create, read, update, and delete todos
  - User-specific task isolation
  - Task completion status tracking
  - Timestamp tracking for task creation

- **Security**
  - JWT access and refresh tokens
  - Protected API endpoints
  - CORS support for frontend integration
  - BCrypt password hashing

## 🛠️ Tech Stack

- **Backend:** Django 5.2.1, Django REST Framework
- **Database:** PostgreSQL
- **Authentication:** JWT (Simple JWT)
- **Password Hashing:** BCrypt
- **API Documentation:** REST Framework browsable API
- **Development:** Python 3.12

## 📋 Prerequisites

- Python 3.12 or higher
- PostgreSQL
- pip (Python package manager)

## 🏗️ Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd task_manager
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   
   # On Windows
   .venv\Scripts\activate
   
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django djangorestframework djangorestframework-simplejwt
   pip install psycopg2-binary django-cors-headers
   ```

4. **Database Setup**
   - Create a PostgreSQL database named `postgres`
   - Update the database credentials in `task_manager/settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'postgres',
           'USER': 'your_username',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/`

## 📚 API Documentation

### Authentication Endpoints

#### Register User
- **POST** `/register/`
- **Description:** Create a new user account
- **Request Body:**
  ```json
  {
    "username": "johndoe",
    "email": "john@example.com",
    "password": "securepassword123",
    "first_name": "John"
  }
  ```
- **Response:**
  ```json
  {
    "message": "User created successfully"
  }
  ```

#### Login
- **POST** `/login/`
- **Description:** Authenticate user and receive JWT tokens
- **Request Body:**
  ```json
  {
    "email": "john@example.com",
    "password": "securepassword123"
  }
  ```
- **Response:**
  ```json
  {
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
  }
  ```

#### User Profile
- **GET** `/profile/`
- **Description:** Get current user's profile information
- **Headers:** `Authorization: Bearer <access_token>`
- **Response:**
  ```json
  {
    "name": "",
    "email": "john@example.com",
    "username": "johndoe"
  }
  ```

### Todo Endpoints

All todo endpoints require authentication. Include the JWT token in the Authorization header:
`Authorization: Bearer <your_access_token>`

#### List Todos
- **GET** `/todos/`
- **Description:** Get all todos for the authenticated user
- **Response:**
  ```json
  [
    {
      "id": 1,
      "title": "Complete project",
      "description": "Finish the task manager API",
      "completed": false,
      "created_at": "2025-05-17T16:35:00Z"
    }
  ]
  ```

#### Create Todo
- **POST** `/todos/`
- **Description:** Create a new todo
- **Request Body:**
  ```json
  {
    "title": "New Task",
    "description": "Task description",
    "completed": false
  }
  ```

#### Get Todo Detail
- **GET** `/todos/{id}/`
- **Description:** Get a specific todo by ID

#### Update Todo
- **PUT** `/todos/{id}/`
- **Description:** Update a specific todo
- **Request Body:**
  ```json
  {
    "title": "Updated Task",
    "description": "Updated description",
    "completed": true
  }
  ```

#### Partial Update Todo
- **PATCH** `/todos/{id}/`
- **Description:** Partially update a specific todo
- **Request Body:**
  ```json
  {
    "completed": true
  }
  ```

#### Delete Todo
- **DELETE** `/todos/{id}/`
- **Description:** Delete a specific todo

## 📁 Project Structure

```
task_manager/
├── task_manager/           # Main project directory
│   ├── __init__.py
│   ├── settings.py         # Django settings
│   ├── urls.py            # Main URL configuration
│   ├── wsgi.py            # WSGI configuration
│   └── asgi.py            # ASGI configuration
├── users/                  # User management app
│   ├── models.py          # CustomUser model
│   ├── serializers.py     # User serializers
│   ├── views.py           # Authentication views
│   └── migrations/        # Database migrations
├── todos/                  # Todo management app
│   ├── models.py          # Todo model
│   ├── serializers.py     # Todo serializers
│   ├── views.py           # Todo ViewSet
│   └── migrations/        # Database migrations
├── manage.py              # Django management script
└── README.md             # Project documentation
```

## 🔧 Configuration

### JWT Settings
The project uses JWT tokens with the following configuration:
- **Access Token Lifetime:** 1 hour
- **Refresh Token Lifetime:** 1 day

### CORS Settings
CORS is enabled for all origins in development. For production, update `CORS_ALLOW_ALL_ORIGINS` in settings.py.

## 🧪 Testing

Run the built-in Django tests:
```bash
python manage.py test
```

## 🚀 Usage Examples

### Using cURL

1. **Register a new user:**
   ```bash
   curl -X POST http://127.0.0.1:8000/register/ \
     -H "Content-Type: application/json" \
     -d '{"username": "testuser", "email": "test@example.com", "password": "testpass123", "first_name": "Test"}'
   ```

2. **Login:**
   ```bash
   curl -X POST http://127.0.0.1:8000/login/ \
     -H "Content-Type: application/json" \
     -d '{"email": "test@example.com", "password": "testpass123"}'
   ```

3. **Create a todo:**
   ```bash
   curl -X POST http://127.0.0.1:8000/todos/ \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer <your_access_token>" \
     -d '{"title": "My First Todo", "description": "This is a test todo", "completed": false}'
   ```

## 🔒 Security Notes

- Change the `SECRET_KEY` in production
- Set `DEBUG = False` in production
- Configure proper database credentials
- Use environment variables for sensitive settings
- Implement proper CORS settings for production

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🐛 Known Issues

- CORS headers middleware is referenced but not fully configured in INSTALLED_APPS
- Duplicate router registration in main URLs
- Consider adding pagination for todo lists
- Add input validation and error handling improvements

## 🔮 Future Enhancements

- [ ] Add task categories and tags
- [ ] Implement due dates for todos
- [ ] Add task priority levels
- [ ] Email notifications for reminders
- [ ] Frontend web interface
- [ ] API rate limiting
- [ ] Advanced filtering and search
- [ ] Task sharing between users

---

For any questions or issues, please open an issue on GitHub or contact the development team.
