import logging

from flask import render_template, request, redirect, url_for, flash
from app import app
from app.forms import ContactForm


logging.basicConfig(
    filename='contact.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)


@app.route('/')
def resume():
    theme = request.cookies.get('theme', 'light')

    return render_template(
        'resume.html',
        title='Resume',
        theme=theme
    )


@app.route('/contacts', methods=['GET', 'POST'])
@app.route('/contact', methods=['GET', 'POST'])
def contacts():
    theme = request.cookies.get('theme', 'light')
    form = ContactForm()

    if form.validate_on_submit():
        logging.info(
            f"Name: {form.name.data}, Email: {form.email.data}, "
            f"Phone: {form.phone.data}, Subject: {form.subject.data}, "
            f"Message: {form.message.data}"
        )

        flash(
            f"Message from {form.name.data} with email {form.email.data} was sent successfully!",
            'success'
        )

        return redirect(url_for('contacts'))

    if request.method == 'POST':
        flash('Form has errors. Please check your data.', 'danger')

    return render_template(
        'contacts.html',
        title='Contacts',
        form=form,
        theme=theme
    )