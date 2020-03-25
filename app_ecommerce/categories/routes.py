from flask import (render_template, url_for, flash,
                   redirect, Blueprint)
from flask_login import login_required
from app_ecommerce.categories.forms import CategoryForm
from app_ecommerce.products.utils import save_picture
from app_ecommerce.models import Product, Category
from app_ecommerce import db

categories = Blueprint('categories',__name__)

@categories.route('/category/new',methods=['GET','POST'])
@login_required
def new_category():
    form = CategoryForm()
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