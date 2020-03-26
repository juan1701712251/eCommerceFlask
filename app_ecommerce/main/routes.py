from flask import render_template, Blueprint
from app_ecommerce.models import Category
main = Blueprint('main',__name__)


@main.route('/')
@main.route('/home')
def home():
    categories = Category.query.filter_by(parent_category ='root').all()
    return render_template('home.html',categories=categories)
