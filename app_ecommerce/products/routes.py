from flask import (render_template, url_for, flash,
                   redirect, Blueprint)
from flask_login import login_required
from app_ecommerce.categories.utils import get_categories_allowed
from app_ecommerce.products.utils import save_picture
from app_ecommerce.products.forms import ProductsForm
from app_ecommerce.models import Product, Category
from app_ecommerce import db,quote

products = Blueprint('products',__name__)

@products.route('/products/new',methods=['GET','POST'])
@login_required
def new_product():
    form = ProductsForm()
    form.category.choices = get_categories_allowed()
    if form.validate_on_submit():
        #print(form.image1.data)
        #print(form.image2.data)
        #print(form.image3.data)
        img1 = None
        img2 = None
        img3 = None
        if form.image1.data:
            img1 = save_picture(form.image1.data,'product_pics')
        if form.image2.data:
            img2 = save_picture(form.image2.data,'product_pics')
        if form.image3.data:
            img3 = save_picture(form.image3.data,'product_pics')
        cate = Category.query.get(form.category.data)
        product = Product(name=form.name.data,
                          description=form.description.data,
                          weight=form.weight.data,
                          price=form.price.data,
                          cate=cate,
                          image_file1=img1,
                          image_file2=img2,
                          image_file3=img3)
        db.session.add(product)
        db.session.commit()
        flash(f'Your product has been created','success')
        return redirect(url_for('main.home'))

    return render_template('create_product.html', title='New Product', form=form, legend='New Product')

@products.route('/product/<int:product_id>')
def view_product(product_id):
    product = Product.query.get(product_id)
    return render_template('product.html', title='Product',quote=quote,product=product)
