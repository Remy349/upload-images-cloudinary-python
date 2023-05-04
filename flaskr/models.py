import sqlalchemy as sa
from flaskr import db


class Image(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    image_title = sa.Column(sa.String(20), nullable=False)
    image_description = sa.Column(sa.String(150), default="No description")
    secure_url = sa.Column(sa.String(180), nullable=False)
    public_id = sa.Column(sa.String(80), nullable=False)

    def __repr__(self):
        return f"""
            image:
                id: {self.id},
                image_title: {self.image_title}
        """
