from flaskr import db


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(100), nullable=False)
    secure_url = db.Column(db.String(140), nullable=False)
    filename= db.Column(db.String(60))

    def __repr__(self):
        return f"""
            Image:
                id: {self.id},
                public_id: {self.public_id},
                secure_url: {self.secure_url},
                filename: {self.filename}
        """
