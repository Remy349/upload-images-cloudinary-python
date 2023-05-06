from flask import Blueprint, render_template
from flaskr.main.forms import NewImageForm

bp = Blueprint("main", __name__)


@bp.route("/", methods=["GET", "POST"])
def index():
    form = NewImageForm()

    return render_template("index.html", form=form)
