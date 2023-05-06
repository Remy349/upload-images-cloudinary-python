from flask_wtf import FlaskForm
from wtforms.fields import FileField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class NewImageForm(FlaskForm):
    image_title = StringField(
        "image_title",
        validators=[DataRequired(), Length(max=20)],
    )
    image_description = TextAreaField(
        "image_description",
        validators=[Length(max=150)],
    )
    image_file = FileField("image_file")
    submit = SubmitField("Save")
