from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

# show = db.Table('show',
#   db.Column('venue_id', db.Integer, db.ForeignKey('venue.id'), primary_key=True),
#   db.Column('artist_id', db.Integer, db.ForeignKey('artist.id'), primary_key=True),
#   db.Column('start_time', db.DateTime, nullable=False)  
# )

class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    image_link = db.Column(db.String(500), nullable=False)
    facebook_link = db.Column(db.String(120), nullable=True)
    website = db.Column(db.String(120),nullable=True)
    seeking_talent = db.Column(db.Boolean, nullable=False, default=False)
    seeking_description = db.Column(db.String(1000), nullable=True)
    genres = db.Column(db.String(120), nullable=False)

    # artists = db.relationship('Artist', secondary=show,
    #     backref=db.backref('venues'), lazy=True)
    shows = db.relationship('Show', backref='venue', lazy='dynamic')
   
    def __repr__(self):
        return f'<id: {self.id}, name: {self.name}, city: {self.city}, state: {self.state}, address: {self.address}, phone: {self.phone}, image_link: {self.image_link},facebook_link: {self.facebook_link}, website: {self.website}, seeking_talent: {self.seeking_talent}, seeking_description: {self.seeking_description}, genres: {self.genres}>'
    # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    genres = db.Column(db.String(120), nullable=False)
    image_link = db.Column(db.String(500), nullable=False)
    facebook_link = db.Column(db.String(120), nullable=True)
    website = db.Column(db.String(120), nullable=True)
    seeking_venue = db.Column(db.Boolean, nullable=False, default=False)
    seeking_description = db.Column(db.String(1000), nullable=True)
   
    shows = db.relationship('Show', backref='artist', lazy='dynamic')

    def __repr__(self):
        return f'<artist ID: {self.id}, name: {self.name}, city: {self.city}, state: {self.state}, genres: {self.genres}>'
    
    # TODO: implement any missing fields, as a database migration using Flask-Migrate

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
class Show(db.Model):
  __tablename__ = 'show'

  artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), primary_key=True)
  venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), primary_key=True)
  start_time = db.Column('start_time', db.DateTime, nullable=False)  
  def __repr__(self):
        return f'<artist: {self.artist}, venue: {self.venue}, start_time: {self.start_time}>'
