from app_ecommerce.models import Category

def get_categories_allowed():
    categories = Category.query.all()
    output = []
    for cat in categories:
        if len(cat.subCategories) == 0:
            output.append((cat.id,cat.name))
    return output