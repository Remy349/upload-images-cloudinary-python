from flaskr import db


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f"""
            Image:
                id: {self.id}
        """

