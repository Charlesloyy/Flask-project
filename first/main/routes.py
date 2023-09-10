from flask import render_template, request, Blueprint
from first.model import Post



main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template ("index.html")

@main.route('/community')
def community():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template ("community.html", posts=posts)

@main.route('/hosting')
def host():
    return render_template ("hosting.html")

@main.route('/domain')
def domain():
    return render_template ("domain.html")

@main.route('/contact')
def contact():
    return render_template ("contact.html")

@main.route('/about')
def about():
    return render_template ("about.html")
