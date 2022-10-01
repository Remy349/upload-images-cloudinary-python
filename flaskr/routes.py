from flask import flash, redirect, render_template, request, url_for
from cloudinary.uploader import upload
from flaskr import app, db

from flaskr.models import Image

ALLOWED_EXTENSIONS = {"png", "jpg", "gif", "jpeg"}


def allowed_file(filename):
    return "." in filename and \
        filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/add_image", methods=["POST"])
def add_image():
    file = request.files["file"]

    if file.filename == "":
        flash("No selected file!")
        return redirect(url_for("index"))

    if file and allowed_file(file.filename):
        filename = file.filename

        upload_result = upload(file,
                               resource_type="image",
                               folder="/test")

        public_id = upload_result["public_id"]
        secure_url = upload_result["secure_url"]

        new_image = Image(public_id=public_id, secure_url=secure_url,
                          filename=filename)

        db.session.add(new_image)
        db.session.commit()

        flash("Image saved successfully!")
        return redirect(url_for("index"))
    else:
        flash("File type not allowed!")
        return redirect(url_for("index"))

