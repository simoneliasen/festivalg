from app import db

class Artist(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    img = db.Column(db.String())
    uri = db.Column(db.String())
    festival = db.Column(db.String())

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
