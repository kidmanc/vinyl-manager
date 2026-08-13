"""Seed the database with demo data for testing."""

import os

os.environ["SECRET_KEY"] = "seed-script-secret-key"

from app.core.database import SessionLocal, engine, Base  # noqa: I001, E402
from app.core.security import hash_password  # noqa: E402
from app.models.user_model import User  # noqa: E402
from app.models.album_model import Album  # noqa: E402
from app.models.review_model import Review  # noqa: E402

Base.metadata.create_all(bind=engine)

db = SessionLocal()

if db.query(User).first():
    print("Database already has data, skipping seed.")
    db.close()
    exit(0)

demo_user = User(
    username="demo",
    email="demo@example.com",
    password_hash=hash_password("demo1234"),
)
db.add(demo_user)
db.flush()

albums = [
    Album(
        title="Abbey Road",
        artist="The Beatles",
        genre="Rock",
        release_year=1969,
        owner_id=demo_user.id,
    ),
    Album(
        title="Thriller",
        artist="Michael Jackson",
        genre="Pop",
        release_year=1982,
        owner_id=demo_user.id,
    ),
    Album(
        title="Kind of Blue",
        artist="Miles Davis",
        genre="Jazz",
        release_year=1959,
        owner_id=demo_user.id,
    ),
    Album(
        title="Nevermind",
        artist="Nirvana",
        genre="Grunge",
        release_year=1991,
        owner_id=demo_user.id,
    ),
    Album(
        title="Rumours",
        artist="Fleetwood Mac",
        genre="Rock",
        release_year=1977,
        owner_id=demo_user.id,
    ),
]
db.add_all(albums)
db.flush()

reviews = [
    Review(
        album_id=albums[0].id,
        user_id=demo_user.id,
        text="Timeless masterpiece from start to finish.",
        rating=5,
    ),
    Review(
        album_id=albums[1].id,
        user_id=demo_user.id,
        text="The best-selling album of all time for a reason.",
        rating=5,
    ),
    Review(
        album_id=albums[2].id,
        user_id=demo_user.id,
        text="Miles Davis at his peak. Essential jazz.",
        rating=5,
    ),
]
db.add_all(reviews)
db.commit()
db.close()

print("Seed complete. 1 user, 5 albums, 3 reviews created.")
print("Demo credentials: demo / demo1234")
