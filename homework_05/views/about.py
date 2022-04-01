from flask import (
    Blueprint,
    render_template,
)

about_page = Blueprint("about_page", __name__)


@about_page.get("/about/", endpoint="about")
def get_about_page():
    return render_template("about.html")
