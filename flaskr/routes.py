import cloudinary.api
from flask import flash, redirect, render_template, request, url_for
from cloudinary.uploader import upload, destroy
from flaskr import app, db

from flaskr.models import Image

ALLOWED_EXTENSIONS = {"png", "jpg", "gif", "jpeg"}


def allowed_file(filename):
    return "." in filename and \
        filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET"])
def index():
    page = request.args.get("page", 1, type=int)
    images = Image.query.paginate(
        page, app.config["IMAGES_PER_PAGE"], False)

    next_url = url_for("index", page=images.next_num) \
        if images.has_next else None
    prev_url = url_for("index", page=images.prev_num) \
        if images.has_prev else None

    return render_template("index.html", images=images.items,
                           next_url=next_url, prev_url=prev_url)


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


@app.route("/delete_image/<int:image_id>", methods=["GET"])
def delete_image(image_id):
    delete_image = Image.query.get_or_404(image_id)
    public_id = delete_image.public_id

    destroy(public_id, resource_type="image")

    db.session.delete(delete_image)
    db.session.commit()

    flash("Image successfully deleted!")
    return redirect(url_for("index"))

