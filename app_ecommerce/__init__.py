from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from app_ecommerce.config import Config

app = Flask(__name__)
app.config.from_object(Config)
#Manejo de Base de Datos
db = SQLAlchemy(app)
#Encriptación
bcrypt = Bcrypt(app)
# A que lugar se redirige si no está logueado
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail(app)

from app_ecommerce.main.routes import main
from app_ecommerce.users.routes import users
from app_ecommerce.products.routes import products
from app_ecommerce.categories.routes import categories
app.register_blueprint(main)
app.register_blueprint(users)
app.register_blueprint(products)
app.register_blueprint(categories)

