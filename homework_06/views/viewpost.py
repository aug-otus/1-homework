from flask import (
    Blueprint,
    render_template,

)

from models import Posts
from models.database import db
from werkzeug.exceptions import NotFound

viewpost_page = Blueprint("viewpost_page", __name__)


@viewpost_page.get("/viewpost", endpoint="viewpost")
def get_all_viewpost_page():
    posts: list[Posts] = Posts.query.all()
    return render_template("viewpost.html", posts=posts)



@viewpost_page.get("/viewpost/<int:post_id>/", endpoint="viewposts")
def get_num_viewpost_page(post_id: int):
    post = Posts.query.get(post_id)
    if post is None:
        raise NotFound(f"Product #{post_id} not found!")
    return render_template("viewposts.html", post=post)
