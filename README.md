# Vinyl Manager

A REST API for managing a music album catalog with user reviews. Built with FastAPI and SQLite.

## Features

- **Album CRUD**: Create, read, update, and delete albums
- **Review system**: Users can review and rate albums (1-5)
- **Authentication**: JWT-based user registration and login
- **Authorization**: Only album/review owners can edit or delete their records
- **Business rule**: Albums with associated reviews cannot be deleted (409 Conflict)
- **Pagination & filtering**: List albums with pagination and genre filter

## Quick Start

### 1. Clone

```bash
git clone https://github.com/KidmanC/techassessment_kidman.git
cd techassessment_kidman/vinyl-manager
```

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Set environment variables

```bash
# Windows
copy .env.example .env

# Linux/Mac
cp .env.example .env
```

Open `.env` and set a strong `SECRET_KEY`:

```bash
# Generate one with:
python -c "import secrets; print(secrets.token_hex(32))"
```

**Available variables:**

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `SECRET_KEY` | **Yes** | — | JWT signing key |
| `DATABASE_URL` | No | `sqlite:///./vinyl_manager.db` | Database connection string |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | No | `60` | JWT token expiration |

### 4. Run the server

```bash
python -m uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.

### 5. Populate demo data (optional)

```bash
python seed.py
```

This creates:
- **Demo user**: `demo` / `demo1234`
- **5 albums**: Abbey Road, Thriller, Kind of Blue, Nevermind, Rumours
- **3 reviews** on the first three albums

### 6. Run tests

```bash
python -m pytest -v
```

## API Endpoints

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| POST | `/users/register` | No | Register a new user |
| POST | `/users/login` | No | Login, returns JWT token |
| GET | `/albums` | No | List albums (supports `?genre=&page=&page_size=`) |
| GET | `/albums/{id}` | No | Get album details |
| POST | `/albums` | Yes | Create an album |
| PUT | `/albums/{id}` | Yes | Update album (owner only) |
| DELETE | `/albums/{id}` | Yes | Delete album (owner only, no reviews attached) |
| GET | `/albums/{id}/reviews` | No | List reviews for an album |
| POST | `/albums/{id}/reviews` | Yes | Add a review to an album |
| DELETE | `/reviews/{id}` | Yes | Delete a review (owner only) |
| GET | `/health` | No | Health check |

## Project Structure

```
vinyl-manager/
├── app/
│   ├── main.py              # FastAPI entry point
│   ├── core/
│   │   ├── config.py        # Settings via env vars (DATABASE_URL, SECRET_KEY)
│   │   ├── database.py      # SQLAlchemy engine and session
│   │   └── security.py      # JWT tokens and password hashing
│   ├── routes/              # HTTP route definitions (thin)
│   │   ├── user_routes.py
│   │   ├── album_routes.py
│   │   └── review_routes.py
│   ├── controllers/         # Orchestrate actions, format responses
│   │   ├── user_controller.py
│   │   ├── album_controller.py
│   │   └── review_controller.py
│   ├── actions/             # Business logic (one file per use case)
│   │   ├── user/
│   │   │   ├── register_user_action.py
│   │   │   └── login_user_action.py
│   │   ├── album/
│   │   │   ├── create_album_action.py
│   │   │   ├── read_album_action.py
│   │   │   ├── read_albums_action.py
│   │   │   ├── update_album_action.py
│   │   │   └── delete_album_action.py
│   │   └── review/
│   │       ├── create_review_action.py
│   │       ├── read_reviews_action.py
│   │       └── delete_review_action.py
│   ├── models/              # SQLAlchemy ORM models
│   │   ├── user_model.py
│   │   ├── album_model.py
│   │   └── review_model.py
│   └── schemas/             # Pydantic DTOs (request/response)
│       ├── user.py
│       ├── album.py
│       └── review.py
├── tests/
│   ├── conftest.py          # Fixtures (in-memory DB, auth)
│   ├── test_users.py        # 4 user tests
│   ├── test_albums.py       # 5 album tests
│   └── test_reviews.py      # 4 review tests (13 total)
├── AGENTIC.md               # AI-assisted development documentation
├── requirements.txt
└── .gitignore
```

## Architecture Flow

```
Request → routes/ → controllers/ → actions/ → models/ → DB
              ↕
         core/security (JWT auth)
```
