from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class PostsForm(FlaskForm):
    title = StringField("Post title", name="post-title", validators=[
        DataRequired(),
        Length(min=3)])
    body = StringField("Post body", name="post-body", validators=[
        DataRequired(),
        Length(min=3)])

