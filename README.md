# Flask Cookie and Session Management

A simple Flask application that demonstrates how to manage **Cookies** and **Sessions** in Flask, including:

- Create Cookie
- Read Cookie
- Update Cookie
- Delete Cookie
- Create Session
- Read Session
- Update Session
- Clear Session
- Configure Session Lifetime

---

## Features

### Cookie Management
- Set Cookie
- Get Cookie
- Update Cookie
- Delete Cookie

### Session Management
- Set Session
- Get Session
- Update Session
- Clear Session
- Session timeout configuration (5 minutes)

---

## Project Structure

```text
flask-cookie-session-management/
│
├── app.py
└── README.md
```

---

## Requirements

- Python 3.8+
- Flask

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/flask-cookie-session-management.git
cd flask-cookie-session-management
```

### 2. Create Virtual Environment (Optional)

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/Mac:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install flask
```

Or:

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
python app.py
```

The application will run at:

```text
http://127.0.0.1:5000/
```

---

# Available Endpoints

## Cookie Endpoints

### Set Cookie

```http
GET /set_cookie
```

Creates a cookie named:

```text
AMAY = AIMAY FOUNDER
```

---

### Get Cookie

```http
GET /get_cookie
```

Displays the cookie value.

---

### Update Cookie

```http
GET /update_cookie
```

Updates the cookie value to:

```text
Updated Value
```

---

### Delete Cookie

```http
GET /delete_cookie
```

Deletes the cookie.

---

# Session Endpoints

### Set Session

```http
GET /set_session
```

Creates a session:

```text
user = AMAR
```

---

### Get Session

```http
GET /get_session
```

Displays the session value.

---

### Update Session

```http
GET /update_session
```

Updates the session value.

---

### Clear Session

```http
GET /clear_session
```

Removes all session data.

---

## Session Configuration

```python
app.permanent_session_lifetime = timedelta(minutes=5)
```

The session will expire after **5 minutes** of inactivity.

---

## Technologies Used

- Python
- Flask
- Cookies
- Sessions

---

## Learning Objectives

This project is suitable for beginners who want to learn:

- HTTP Cookies
- Session Management
- Flask Routing
- Web State Management
- Backend Development with Flask

---

## Author

**Amay (AIMAY FOUNDER)**

## ⭐ Support

If you find this project useful, please give it a ⭐ on GitHub.
