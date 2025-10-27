import os

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from PicsNBlogs.auth import login_required
from PicsNBlogs.db import get_db

bp = Blueprint('pics', __name__, url_prefix='/pics')

@bp.route('/')
def index():
    
    
    return render_template('pics/index.html')