from flask import Flask

app = Flask(__name__)
app.secret_key = 'my_secret_key_123'

from app.views import *
from app.users.views import users
from app.products.views import products

app.register_blueprint(users)
app.register_blueprint(products)