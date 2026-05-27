from flask import Blueprint, render_template

products = Blueprint(
    'products',
    __name__,
    url_prefix='/products'
)

@products.route('/')
def show_products():

    items = [
        'Laptop',
        'Phone',
        'Keyboard'
    ]

    return render_template(
        'products/products.html',
        items=items
    )