from http import HTTPStatus
from flask import (
    Blueprint,
    render_template, request, url_for,
)

from forms import PostsForm
from models import Posts
from models.database import db

from psycopg2 import IntegrityError, DatabaseError
from werkzeug.exceptions import BadRequest, InternalServerError
from werkzeug.utils import redirect

addpost_page = Blueprint("addpost_page", __name__)


@addpost_page.route("/addpost/", methods=["GET", "POST"], endpoint="addpost")
def add_post():
    form = PostsForm()
    if request.method == "GET":
        return render_template("addpost.html", form=form)

    if not form.validate_on_submit():
        return render_template("addpost.html", form=form), HTTPStatus.BAD_REQUEST

    post_title = form.data["title"]
    post_body = form.data["body"]
    post = Posts(title=post_title, body=post_body)
    db.session.add(post)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise BadRequest(f"could not save post, probably title {post_title!r} is not unique")
    except DatabaseError:
        db.session.rollback()
        raise InternalServerError(f"could not save post, unexpected error")

    post_url = url_for("viewpost_page.viewpost")
    return redirect(post_url)