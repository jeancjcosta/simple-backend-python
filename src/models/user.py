from src.server.instance import server

db = server.db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(14), unique=True, nullable=False)
    date_joined = db.Column(db.Date, nullable=False)

    def __init__(self, name, date_joined):
        self.name = name
        self.date_joined = date_joined



