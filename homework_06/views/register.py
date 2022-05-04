from flask import (
    Blueprint,
    render_template,
)

register_page = Blueprint("register_page", __name__)


@register_page.get("/register", endpoint="register")
def get_register_page():
    return render_template("register.html")
