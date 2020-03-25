from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from app_ecommerce import db, login_manager
from flask import app
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60),nullable=False)


    def get_reset_token(self,expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'],expires_sec)
        return s.dumps({'user_id':self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}','{self.email}')"

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20),unique=True,nullable=False)
    image_file = db.Column(db.String(20),nullable=False,default='defaultCategory.jpg')
    parent_category = db.Column(db.Integer, db.ForeignKey('category.id'),nullable=False,default='root')

    products = db.relationship('Product', backref='cate', lazy=True)
    subCategories = db.relationship('Category',backref=db.backref('parent_cat',remote_side='Category.id'),lazy=True)

    def __repr__(self):
        return f"Category('{self.name}','{self.parent_category}','{self.image_file}')"

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20),unique=True, nullable=False)
    description = db.Column(db.String(120),nullable=False)
    weight = db.Column(db.String(10), nullable=False,default='1Kg')
    price = db.Column(db.Float(10), nullable=False,default=3.1)
    image_file1 = db.Column(db.String(20),nullable=False,default='defaultProduct.jpg')
    image_file2 = db.Column(db.String(20), nullable=False, default='defaultProduct.jpg')
    image_file3 = db.Column(db.String(20), nullable=False, default='defaultProduct.jpg')
    category = db.Column(db.Integer, db.ForeignKey('category.id'),nullable=False)

    def __repr__(self):
        return f"Product('{self.name}','{self.category}','{self.price}')"