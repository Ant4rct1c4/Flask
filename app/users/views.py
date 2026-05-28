from flask import Blueprint, render_template, request, redirect, url_for, session, flash

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


@users.route('/login', methods=['GET', 'POST'])
def login():
    theme = request.cookies.get('theme', 'light')

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'user1' and password == '12345':
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('users.profile'))

        flash('Wrong data! Try again!', 'danger')

    return render_template(
        'users/login.html',
        title='Login',
        theme=theme
    )


@users.route('/profile')
def profile():
    if 'username' not in session:
        flash('Please login first!', 'danger')
        return redirect(url_for('users.login'))

    theme = request.cookies.get('theme', 'light')

    return render_template(
        'users/profile.html',
        title='Profile',
        username=session['username'],
        cookies=request.cookies,
        theme=theme
    )


@users.route('/logout')
def logout():
    session.pop('username', None)
    flash('You logged out!', 'info')
    return redirect(url_for('users.login'))


@users.route('/add-cookie', methods=['POST'])
def add_cookie():
    if 'username' not in session:
        return redirect(url_for('users.login'))

    key = request.form.get('key')
    value = request.form.get('value')
    max_age = request.form.get('max_age')

    response = redirect(url_for('users.profile'))

    if key and value:
        response.set_cookie(
            key,
            value,
            max_age=int(max_age or 3600)
        )
        flash('Cookie added successfully!', 'success')

    return response


@users.route('/delete-cookie', methods=['POST'])
def delete_cookie():
    if 'username' not in session:
        return redirect(url_for('users.login'))

    key = request.form.get('key')
    response = redirect(url_for('users.profile'))

    if key:
        response.delete_cookie(key)
        flash('Cookie deleted!', 'warning')

    return response


@users.route('/delete-all-cookies')
def delete_all_cookies():
    if 'username' not in session:
        return redirect(url_for('users.login'))

    response = redirect(url_for('users.profile'))

    for key in request.cookies:
        response.delete_cookie(key)

    flash('All cookies deleted!', 'warning')
    return response


@users.route('/set-theme/<theme>')
def set_theme(theme):
    if 'username' not in session:
        return redirect(url_for('users.login'))

    response = redirect(url_for('users.profile'))

    if theme in ['light', 'dark']:
        response.set_cookie(
            'theme',
            theme,
            max_age=60 * 60 * 24 * 30
        )
        flash('Theme changed!', 'success')

    return response