from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from PicsNBlogs.auth import login_required
from PicsNBlogs.db import get_db

bp = Blueprint('blog', __name__, url_prefix='/blog')

############################
# Blogs index page handler.#
############################

@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    
    # return render_template('blog/index.html', posts=posts)

    # DELETE THIS
    return '<h1>Blog Index</h1>'


############################


###############################
# Blog Create Page handler.   #
###############################

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)'
                ' VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('blog.index'))

    # return render_template('blog/create.html')

    # DELETE THIS
    return '<h1>Create Blog</h1>'

##################################