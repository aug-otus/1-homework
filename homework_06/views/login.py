from flask import (
    Blueprint,
    render_template,
)

login_page = Blueprint("login_page", __name__)


@login_page.get("/login", endpoint="login")
def get_login_page():
    return render_template("login.html")


