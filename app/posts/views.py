from flask import (
    render_template,
    redirect,
    url_for,
    flash,
    request,
    session
)

from app import db
from app.posts import post_bp
from app.posts.models import Post
from app.posts.forms import PostForm


@post_bp.route('/')
def all_posts():
    stmt = (
        db.select(Post)
        .where(Post.is_active == True)
        .order_by(Post.posted.desc())
    )

    posts = db.session.scalars(stmt).all()

    theme = request.cookies.get('theme', 'light')

    return render_template(
        'posts/all_posts.html',
        title='All Posts',
        posts=posts,
        theme=theme
    )


@post_bp.route('/create', methods=['GET', 'POST'])
def create_post():
    form = PostForm()
    theme = request.cookies.get('theme', 'light')

    if form.validate_on_submit():
        author = session.get('username', 'Anonymous')

        post = Post(
            title=form.title.data,
            content=form.content.data,
            is_active=form.is_active.data,
            posted=form.publish_date.data,
            category=form.category.data,
            author=author
        )

        db.session.add(post)
        db.session.commit()

        flash('Post added successfully!', 'success')

        return redirect(url_for('posts.all_posts'))

    if request.method == 'POST':
        flash('Post form has errors. Please check your data.', 'danger')

    return render_template(
        'posts/add_post.html',
        title='Create Post',
        form=form,
        page_title='Create New Post',
        theme=theme
    )


@post_bp.route('/<int:id>')
def detail_post(id):
    post = db.get_or_404(Post, id)
    theme = request.cookies.get('theme', 'light')

    return render_template(
        'posts/detail_post.html',
        title=post.title,
        post=post,
        theme=theme
    )


@post_bp.route('/<int:id>/update', methods=['GET', 'POST'])
def update_post(id):
    post = db.get_or_404(Post, id)
    form = PostForm(obj=post)
    theme = request.cookies.get('theme', 'light')

    if request.method == 'GET':
        form.publish_date.data = post.posted

    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.is_active = form.is_active.data
        post.posted = form.publish_date.data
        post.category = form.category.data

        db.session.commit()

        flash('Post updated successfully!', 'success')

        return redirect(
            url_for(
                'posts.detail_post',
                id=post.id
            )
        )

    if request.method == 'POST':
        flash('Post update form has errors.', 'danger')

    return render_template(
        'posts/add_post.html',
        title='Update Post',
        form=form,
        page_title='Update Post',
        theme=theme
    )


@post_bp.route('/<int:id>/delete', methods=['GET', 'POST'])
def delete_post(id):
    post = db.get_or_404(Post, id)
    theme = request.cookies.get('theme', 'light')

    if request.method == 'POST':
        db.session.delete(post)
        db.session.commit()

        flash('Post deleted successfully!', 'warning')

        return redirect(url_for('posts.all_posts'))

    return render_template(
        'posts/delete_confirm.html',
        title='Delete Post',
        post=post,
        theme=theme
    )