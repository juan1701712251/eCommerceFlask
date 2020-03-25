from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FloatField, FileField, SelectField
from wtforms.validators import DataRequired,Length
from flask_wtf.file import FileAllowed

class ProductsForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(),Length(min=2,max=20)])
    description = TextAreaField('Description', validators=[DataRequired(),Length(min=2,max=120)])
    weight = StringField('Weight',validators=[DataRequired()])
    price = FloatField('Price(USD)', validators=[DataRequired()])
    image_file1 = FileField('Insert Image 1',validators=[FileAllowed(['jpg','png'])])
    image_file2 = FileField('Insert Image 2', validators=[FileAllowed(['jpg', 'png'])])
    image_file3 = FileField('Insert Image 3', validators=[FileAllowed(['jpg', 'png'])])
    category = SelectField('Category',choices=[])

    submit = SubmitField('Create Product')