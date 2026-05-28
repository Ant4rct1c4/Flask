from flask import render_template, request
from app import app


@app.route('/')
def resume():
    theme = request.cookies.get('theme', 'light')

    return render_template(
        'resume.html',
        title='Resume',
        theme=theme
    )


@app.route('/contacts')
def contacts():
    theme = request.cookies.get('theme', 'light')

    return render_template(
        'contacts.html',
        title='Contacts',
        theme=theme
    )