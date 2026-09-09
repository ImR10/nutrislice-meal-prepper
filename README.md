# UGA NutriSlice Meal Planner

A full-stack meal planning app for UGA students with a dining hall pass. The backend pulls live menu data from the NutriSlice API, calculates calorie and macro targets from user metrics, and recommends meals based on what is actually available that day.

---

## What it does

1. User registers / logs in (JWT auth)
2. User saves fitness metrics and goals (age, height, weight, activity, goal)
3. Backend fetches today’s dining hall menu from NutriSlice and caches it in SQLite
4. Backend calculates BMR / TDEE / macro targets
5. A greedy optimizer (planned) recommends breakfast, lunch, and dinner from available items

**V1 scope:** single dining hall, three meals per day, greedy optimizer, basic auth.

---

## Tech stack

| Layer | Technology |
|-------|------------|
| Backend | Python, Flask |
| Database | SQLite via Flask-SQLAlchemy |
| Auth | Flask-JWT-Extended + bcrypt |
| Nutrition math | Mifflin–St Jeor BMR + TDEE multipliers |
| Data source | NutriSlice undocumented JSON API |
| Frontend (planned) | React (Vite) |
| Version control | Git / GitHub |

---

## Project structure

```
nutrislice-meal-prepper-v1/
├── backend/
│   ├── app.py                 # Flask entry point
│   ├── models.py              # User, UserProfile, CachedMenu
│   ├── extensions.py          # db, bcrypt, jwt
│   ├── config.py              # config placeholders
│   ├── routes/
│   │   ├── auth.py            # /register, /login
│   │   ├── profile.py         # /profile
│   │   └── meal_planner.py    # /meal-plan, /menu
│   └── services/
│       ├── nutrislice.py      # fetch + clean menu items
│       ├── nutrition.py       # BMR, TDEE, macros
│       └── optimizer.py       # greedy optimizer (in progress)
├── instance/                  # SQLite DB (created at runtime)
├── user_info.py               # early CLI nutrition prototype
├── json_menu_parse_script.py  # early NutriSlice parsing prototype
├── .env                       # secrets (not committed)
└── README.md
```

---

## Setup

### Prerequisites

- Python 3.10+
- pip
- (optional) Postman or curl for testing API routes

### 1. Clone the repo

```bash
git clone https://github.com/ImR10/nutrislice-meal-prepper.git
cd nutrislice-meal-prepper
```

### 2. Create a virtual environment

```bash
python -m venv venv

# Windows (Git Bash / bash)
source venv/Scripts/activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install flask flask-sqlalchemy flask-bcrypt flask-jwt-extended python-dotenv requests
```

> Tip: once dependencies stabilize, freeze them with `pip freeze > requirements.txt`.

### 4. Environment variables

Create a `.env` file in the project root (or `backend/`, depending on where you load dotenv from):

```env
JWT_SECRET_KEY=change-me-to-a-long-random-string
SCHOOL=uga
```

Never commit `.env` — it is listed in `.gitignore`.

### 5. Run the Flask server

```bash
cd backend
python app.py
```

The app should start at `http://127.0.0.1:5000`.  
Tables are created automatically via `db.create_all()` on startup.

---

## API overview

Base URL (local): `http://127.0.0.1:5000`

### Auth

| Method | Route | Auth | Description |
|--------|-------|------|-------------|
| `POST` | `/register` | No | Create account, return JWT |
| `POST` | `/login` | No | Verify credentials, return JWT |

**Register body example:**

```json
{
  "email": "student@uga.edu",
  "password": "secret",
  "name": "Rizwan"
}
```

**Login body example:**

```json
{
  "email": "student@uga.edu",
  "password": "secret"
}
```

Protected routes expect:

```http
Authorization: Bearer <token>
```

### Profile

| Method | Route | Auth | Description |
|--------|-------|------|-------------|
| `POST` | `/profile` | Yes | Save user metrics / goal |
| `GET` | `/profile` | Yes | Get current user profile |

**Profile body example:**

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

### Menu / meal plan

| Method | Route | Auth | Description |
|--------|-------|------|-------------|
| `GET` | `/menu` | Yes | Today’s cleaned menu (cached in SQLite) |
| `GET` | `/meal-plan` | Yes | Optimized daily meal plan (in progress) |

---

## Architecture (high level)

```
NutriSlice API
      │
      ▼
Flask services (fetch + clean + cache)
      │
      ▼
SQLite (users, profiles, cached_menus)
      │
      ▼
Nutrition + Optimizer
      │
      ▼
Flask routes  ──JSON──►  React frontend (planned)
```

This project follows an MVC-style split:

- **Model:** SQLAlchemy models + services
- **View:** React frontend (planned)
- **Controller:** Flask routes

---

## Database schema

| Table | Key fields |
|-------|------------|
| `users` | `id`, `email`, `password_hash`, `name` |
| `user_profiles` | `user_id`, `age`, `gender`, `height`, `weight`, `activity_level`, `goal` |
| `cached_menus` | `date`, `meal_type`, `menu_json` |

Menus are cached once per `(date, meal_type)` so NutriSlice is not hit repeatedly during development.

---

## V2 backlog

- Swap greedy optimizer for PuLP linear programming
- Multiple dining halls
- Dietary restriction filters
- Meal history / weekly macro summary
- Mobile-responsive UI
- Body weight tracking over time

---

## Notes for contributors / future

- Test backend routes in Postman **before** wiring React.
- NutriSlice’s API is undocumented and can change — caching helps catch parse breaks early.
- Filter out items with missing nutrition data before sending them to the optimizer.
- Keep secrets in `.env`; only commit placeholders like `.env.example` if you add one later.

---

## License

Personal / educational project for UGA coursework and learning. Not affiliated with NutriSlice or the University of Georgia dining services.
