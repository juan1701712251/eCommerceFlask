from flask import (render_template, url_for, flash,
                   redirect, Blueprint)
from flask_login import login_required
from app_ecommerce.categories.utils import get_categories
from app_ecommerce.categories.forms import CategoryForm
from app_ecommerce.products.utils import save_picture
from app_ecommerce.models import Category, Product
from app_ecommerce import db

categories = Blueprint('categories',__name__)

@categories.route('/category/new',methods=['GET','POST'])
@login_required
def new_category():
    form = CategoryForm()
    form.parent_category.choices = get_categories()
    if form.validate_on_submit():
        img = None
        if form.image.data:
            img = save_picture(form.image.data, 'category_pics')
        par_cat = None
        if form.parent_category.data:
            par_cat = Category.query.get(form.parent_category.data)
        c = Category(name=form.name.data,
                     image_file=img,
                     parent_cat=par_cat)
        db.session.add(c)
        db.session.commit()
        flash(f'Your category has been created', 'success')
        return redirect(url_for('main.home'))

    return render_template('create_category.html', title='New Category', form=form, legend='New Category')

@categories.route('/category/<int:category_id>')
def subcategories_for_category(category_id):
    categories = Category.query.get(category_id).subCategories
    return render_template('home.html', categories=categories)

@categories.route('/category/<int:category_id>/products')
def products_for_category(category_id):
    c = Category.query.get(category_id)
    products = c.products
    categories = [c]
    return render_template('home.html',categories=categories, products=products)