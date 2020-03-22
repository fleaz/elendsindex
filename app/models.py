from app import db


class Thing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200))
    original_value = db.Column(db.Float(), unique=True)
    value = db.Column(db.Integer(), default=0)
    count = db.Column(db.Integer(), default=0)

    def __repr__(self):
        return "<Thing {}>".format(self.original_value)

    def upvote(self):
        self.value += 1

    def choosen(self):
        self.count += 1
