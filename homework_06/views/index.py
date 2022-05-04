from flask import (
    Blueprint,
    render_template,
)

index_page = Blueprint("index_page", __name__)


@index_page.get("/", endpoint="index")
def get_index_page():
    return render_template("index.html")
