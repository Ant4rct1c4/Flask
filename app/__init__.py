from flask import Flask

app = Flask(__name__)

from app.views import *
from app.users.views import users

app.register_blueprint(users)
from app.products.views import products

app.register_blueprint(products)