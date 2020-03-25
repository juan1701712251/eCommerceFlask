from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from app_ecommerce.categories.utils import get_categories_allowed
from app_ecommerce.products.forms import ProductsForm

products = Blueprint('products',__name__)

@products.route('/products/new',methods=['GET','POST'])
@login_required
def new_product():
    form = ProductsForm()
    form.category.choices = get_categories_allowed()
    return render_template('create_product.html', title='New Product', form=form, legend='New Product')