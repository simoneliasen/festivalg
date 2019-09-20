class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), nullable=False)
    img = db.Column(db.String())
    uri = db.Column(db.String())
    festival = db.Column(db.String())

    def __repr__(self):
        return f"Artist('{self.name}', '{self.img}', '{self.uri}', '{self.festivalg}')"