from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField, SubmitField,SelectField
from wtforms.validators import DataRequired,Length
from app_ecommerce.categories.utils import get_categories

class NonValidatingSelectField(SelectField):
    def pre_validate(self, form):
        pass

class CategoryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    image = FileField('Insert Image', validators=[FileAllowed(['jpg', 'png'])])
    parent_category = NonValidatingSelectField('Parent Category', choices=get_categories())

    submit = SubmitField('Create Category')