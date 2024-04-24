from . import db
from flask_login import UserMixin


class AnimeData(db.Model):
    anime_id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50))
    score = db.Column(db.Text)
    genres = db.Column(db.Text)
    synopsis = db.Column(db.Text)
    type = db.Column(db.Text)
    episodes = db.Column(db.Integer)
    aired = db.Column(db.Text)
    studios = db.Column(db.String(50))
    duration = db.Column(db.Text)
    rating = db.Column(db.Text)
    rank = db.Column(db.Integer)
    image_url = db.Column(db.Text)
    favorites = db.Column(db.Integer)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))


class AnimeDataset(db.Model):
    anime_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Strings(70))
    score = db.Column(db.Float)
    type = db.Column(db.Strings(20))
    # The columns where the anime is not finished show up as 'UNKNOWN'; might have to change to something else
    episodes = db.Column(db.Integer)
    aired = db.Column(db.Strings(30))
    premiered = db.Column(db.Strings(20))
    status = db.Column(db.Strings(20))
    producers = db.Column(db.Strings(100))
    licensors = db.Column(db.Strings(100))
    studios = db.Column(db.Strings(100))
    source = db.Column(db.Strings(20))
    duration = db.Column(db.Strings(30))
    rating = db.Column(db.Strings(40))
    rank = db.Column(db.Integer)
    popularity = db.Column(db.Integer)
    favorites = db.Column(db.Integer)
    scored_by = db.Column(db.Integer)
    members = db.Column(db.Integer)
    images_url = db.Column(db.Text)


class AnimeImages(db.Model):
    anime_id = db.Column(db.Integer, db.ForeignKey('anime_id'), nullable=False)
    images = db.Column(db.Text)


class AnimeGenres(db.Model):
    anime_id = db.Column(db.Integer, db.ForeignKey('anime_id'), nullable=False)
    name = db.Column(db.String(35))

    # This needs to go to the AnimeDataset Model when it is made
    genre = db.relationship('AnimeDataset', backref='anime')


class UserDetails(db.model):
    # id for the users from the anime dataset (not the anime dataset mmodel)
    mal_id = db.Column(db.Integer, primary_key=True)
    username = db.Columns(db.Strings(100))
    gender = db.Columns(db.Strings(20))
    birthday = db.Columns(db.Date)
    location = db.Columns(db.Text)
    joined = db.Column(db.Text)
    days_watched = db.Columns(db.Integer)
    mean_score = db.Columns(db.Float)
    watching = db.Columnd(db.Integer)
    completed = db.Columns(db.Integer)
    on_hold = db.Columns(db.Integer)
    dropped = db.Columns(db.Integer)
    plan_to_watch = db.Columns(db.Integer)
    total_entries = db.Columns(db.Integer)
    rewatched = db.Columns(db.Integer)
    episodes_watched = db.Columns(db.Integer)
    age = db.Columns(db.Integer)



# class AnimeFiltered(db.Model):
#     anime_id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50))
#     score = db.Column(db.Text)
#     genres = db.Column(db.Text)
#     synopsis = db.Column(db.Text)
#     type = db.Column(db.Text)
#     episodes = db.Column(db.Integer)
#     aired = db.Column(db.Text)
#     studios = db.Column(db.String(50))
#     duration = db.Column(db.Text)
#     rating = db.Column(db.Text)
#     rank = db.Column(db.Integer)
#     image_url = db.Column(db.Text)
#     favorites = db.Column(db.Integer)


# class AnimeDataset(db.Model):
#     anime_id = db.Column(db.Integer, primary_key=True, unique=True)
#     name = db.Column(db.String(50))
#     score = db.Column(db.Float)
#     genre = db.Column(db.String(50))
#     english_name = db.Column(db.String(50))
#     japanese_name = db.Column(db.Text)
#     synopsis = db.Column(db.Text)
#     type = db.Column(db.Text)
#     episodes = db.Column(db.String(20))
#     aired = db.Column(db.Text)
#     premiered = db.Column(db.Text)
#     producers = db.Column(db.String(100))
#     licensors = db.Column(db.String(100))
#     studios = db.Column(db.String(50))
#     source = db.Column(db.Text)
#     duration = db.Column(db.Text)
#     rating = db.Column(db.Text)
#     ranked = db.Column(db.Text)
#     popularity = db.Column(db.Integer)
#     members = db.Column(db.Integer)
#     favorites = db.Column(db.Integer)
#     watching = db.Column(db.Integer)
#     completed = db.Column(db.Integer)
#     on_hold = db.Column(db.Integer)
#     dropped = db.Column(db.Integer)
