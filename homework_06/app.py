from os import getenv
from models.database import db

from flask import Flask
from flask_migrate import Migrate

from views.about import about_page
from views.index import index_page
from views.addpost import addpost_page
from views.register import register_page
from views.login import login_page
from views.viewpost import viewpost_page


app = Flask(__name__)
CONFIG_OBJECT_PATH = "config.{}".format(getenv("CONFIG_NAME", "DevelopmentConfig"))
app.config.from_object(CONFIG_OBJECT_PATH)
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(index_page)
app.register_blueprint(register_page)
app.register_blueprint(login_page)
app.register_blueprint(addpost_page)
app.register_blueprint(viewpost_page)
app.register_blueprint(about_page)


if __name__ == '__main__':
    app.run(debug=True)

