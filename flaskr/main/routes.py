from cloudinary.uploader import upload, destroy
from flaskr import db
from flask import Blueprint, flash, redirect, render_template, url_for
from flaskr.main.forms import NewImageForm

from flaskr.models import Image

bp = Blueprint("main", __name__)

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@bp.route("/", methods=["GET", "POST"])
def index():
    form = NewImageForm()

    images = db.session.execute(db.select(Image)).scalars().all()

    if form.validate_on_submit():
        image_title = form.image_title.data
        image_file = form.image_file.data
        image_description = form.image_description.data

        image = Image(image_title=image_title, image_description=image_description)

        if image_file.filename == "":
            flash("No selected file!", "error")
            return redirect(url_for("main.index"))

        if image_file and allowed_file(image_file.filename):
            upload_result = upload(
                image_file,
                resource_type="image",
                folder="/test",
            )

            secure_url = upload_result["secure_url"]
            public_id = upload_result["public_id"]

            image.secure_url = secure_url
            image.public_id = public_id
        else:
            flash("File type not allowed!", "error")
            return redirect(url_for("main.index"))

        db.session.add(image)
        db.session.commit()

        flash("Image save successfully!", "success")

        return redirect(url_for("main.index"))

    return render_template("index.html", form=form, images=images)


@bp.route("/delete/<int:image_id>", methods=["GET"])
def delete_image(image_id):
    image = db.get_or_404(Image, image_id)

    destroy(image.public_id, resource_type="image")

    db.session.delete(image)
    db.session.commit()

    flash("Image successfully deleted!", "success")

    return redirect(url_for("main.index"))
