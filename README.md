# UGA NutriSlice Meal Planner

Personalized meal plans for UGA students with a dining hall pass — built from live NutriSlice menu data and each user’s fitness goals.

**Rizwan Hoque** · University of Georgia

---

## Overview

This project is a Flask REST API that helps students turn dining hall menus into meals that match their calorie and macro targets.

Users create an account, enter height/weight/activity/goal, and the backend:

1. Calculates BMR and TDEE (Mifflin–St Jeor)
2. Fetches the day’s menu from the NutriSlice API
3. Caches cleaned menu items in SQLite
4. Returns meal recommendations based on available food that day

**V1 focus:** one dining hall · breakfast / lunch / dinner · JWT auth · greedy meal selection

---

## Features

- **Auth** — register and login with bcrypt password hashing and JWT tokens
- **User profiles** — store metrics and fitness goals behind protected routes
- **Live menu ingestion** — pull JSON from NutriSlice and normalize it for the app
- **Daily caching** — store menus by date and meal type so the external API isn’t hit on every request
- **Nutrition engine** — derive calorie and macro targets from profile data
- **Meal planning API** — expose cleaned menus and optimized daily plans as JSON

---

## Tech stack

| Layer | Technology |
|-------|------------|
| Backend | Python, Flask |
| Database | SQLite, Flask-SQLAlchemy |
| Auth | Flask-JWT-Extended, bcrypt |
| HTTP client | Requests |
| Config | python-dotenv |
| Frontend (next) | React |

---

## Architecture

```
Client (Postman / future React app)
              │
              ▼
        Flask routes
     (auth · profile · menu)
              │
     ┌────────┼────────┐
     ▼        ▼        ▼
 Nutrition  Optimizer  Nutrislice service
     │                   │
     ▼                   ▼
  SQLite ◄──────── NutriSlice API
 (users, profiles, cached menus)
```

**MVC-style split**

| Layer | In this project |
|-------|-----------------|
| Model | SQLAlchemy models + service classes |
| Controller | Flask blueprints / routes |
| View | JSON responses (React UI coming next) |

---

## Project structure

```
├── backend/
│   ├── app.py                  # Flask entry point
│   ├── models.py               # User, UserProfile, CachedMenu
│   ├── extensions.py           # db, bcrypt, jwt
│   ├── routes/
│   │   ├── auth.py             # POST /register, POST /login
│   │   ├── profile.py          # GET/POST /profile
│   │   └── meal_planner.py     # GET /menu, GET /meal-plan
│   └── services/
│       ├── nutrislice.py       # Fetch + clean menu data
│       ├── nutrition.py        # BMR, TDEE, macros
│       └── optimizer.py        # Meal selection logic
├── instance/                   # Local SQLite database
├── .env                        # Secrets (not committed)
└── README.md
```

---

## Getting started

### Prerequisites

- Python 3.10+
- pip

### 1. Clone

```bash
git clone https://github.com/ImR10/nutrislice-meal-prepper.git
cd nutrislice-meal-prepper
```

### 2. Virtual environment

```bash
python -m venv venv

# Windows (Git Bash)
source venv/Scripts/activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install flask flask-sqlalchemy flask-bcrypt flask-jwt-extended python-dotenv requests
```

### 4. Environment variables

Create a `.env` file:

```env
JWT_SECRET_KEY=your-long-random-secret
SCHOOL=uga
```

### 5. Run the API

```bash
cd backend
python app.py
```

Server: `http://127.0.0.1:5000`  
Database tables are created automatically on startup.

---

## API reference

Base URL: `http://127.0.0.1:5000`

Protected routes require:

```http
Authorization: Bearer <token>
```

### Authentication

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| `POST` | `/register` | No | Create account and return JWT |
| `POST` | `/login` | No | Verify credentials and return JWT |

**Register**

```json
{
  "email": "student@uga.edu",
  "password": "secret",
  "name": "Rizwan"
}
```

**Login**

```json
{
  "email": "student@uga.edu",
  "password": "secret"
}
```

### Profile

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| `POST` | `/profile` | Yes | Save metrics and goal |
| `GET` | `/profile` | Yes | Fetch saved profile |

```json
{
  "age": 20,
  "gender": "male",
  "height": 175.0,
  "weight": 70.0,
  "activity_level": 3,
  "goal": 1
}
```

### Menu & meal plan

| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| `GET` | `/menu` | Yes | Today’s cleaned menu (breakfast, lunch, dinner) |
| `GET` | `/meal-plan` | Yes | Optimized daily meal plan for the current user |

---

## Database

| Table | Purpose |
|-------|---------|
| `users` | Account credentials and display name |
| `user_profiles` | Fitness metrics and goals |
| `cached_menus` | Menu JSON keyed by date + meal type |

---

## Roadmap

- React frontend for login, profile, and meal plan display
- Stronger meal optimizer (PuLP linear programming)
- Multiple dining halls and dietary filters
- Meal history and weekly macro summaries

---

## License

Educational / personal project. Not affiliated with NutriSlice or UGA Dining Services.
