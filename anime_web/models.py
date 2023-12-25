from . import db
from flask_login import UserMixin
import csv


class AnimeDataset(db.Model):
    anime_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    score = db.Column(db.Float)
    genre = db.Column(db.String(50))
    english_name = db.Column(db.String(50))
    japanese_name = db.Column(db.Text)
    synopsis = db.Column(db.Text)
    type = db.Column(db.Text)
    episodes = db.Column(db.String(20))
    aired = db.Column(db.Text)
    premiered = db.Column(db.Text)
    producers = db.Column(db.String(100))
    licensors = db.Column(db.String(100))
    studios = db.Column(db.String(50))
    source = db.Column(db.Text)
    duration = db.Column(db.Text)
    rating = db.Column(db.Text)
    ranked = db.Column(db.Text)
    popularity = db.Column(db.Integer)
    members = db.Column(db.Integer)
    favorites = db.Column(db.Integer)
    watching = db.Column(db.Integer)
    completed = db.Column(db.Integer)
    on_hold = db.Column(db.Integer)
    dropped = db.Column(db.Integer)


class AnimeFiltered(db.Model):
    anime_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    english_name = db.Column(db.String(50))
    japanese_name = db.Column(db.Text)
    score = db.Column(db.Float)
    genre = db.Column(db.String(50))
    synopsis = db.Column(db.Text)
    type = db.Column(db.Text)
    episodes = db.Column(db.Integer)
    aired = db.Column(db.Text)
    premiered = db.Column(db.Text)
    producers = db.Column(db.String(100))
    licensors = db.Column(db.String(100))
    studios = db.Column(db.String(50))
    source = db.Column(db.Text)
    duration = db.Column(db.Text)
    rating = db.Column(db.Text)
    rank = db.Column(db.Integer)
    popularity = db.Column(db.Integer)
    favorites = db.Column(db.Integer)
    scored_by = db.Column(db.String(50))
    members = db.Column(db.Integer)
    image = db.Column(db.Text)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))

