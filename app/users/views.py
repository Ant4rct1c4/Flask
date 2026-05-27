from flask import Blueprint, render_template, request, redirect, url_for

users = Blueprint(
    'users',
    __name__,
    template_folder='templates',
    url_prefix='/users'
)

@users.route('/hi/<name>')
def greetings(name):

    age = request.args.get('age')

    return render_template(
        'users/hi.html',
        name=name,
        age=age
    )

@users.route('/admin')
def admin():

    return redirect(
        url_for(
            'users.greetings',
            name='Administrator',
            age=45
        )
    )