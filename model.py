from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    shows = db.relationship('Show', backref='Venue')
    seeking_talent= db.Column(db.Boolean) 
    seeking_description= db.Column(db.String())
    
    def create(self):
        db.session.add(self)
        db.session.commit()
       
    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean)
    seeking_description = db.Column(db.String(500))
    website= db.Column(db.String(500))
    shows = db.relationship('Show', backref='Artist')
    
    def create(self):
        db.session.add(self)
        db.session.commit()
       
    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Show(db.Model):
  __tablename__ = "Show"

  id = db.Column(db.Integer, primary_key=True, nullable=False)
  start_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

  artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'), nullable=False)
  venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'), nullable=False)

  def create(self):
        db.session.add(self)
        db.session.commit()
       
  def delete(self):
    db.session.delete(self)
    db.session.commit()


  
  
