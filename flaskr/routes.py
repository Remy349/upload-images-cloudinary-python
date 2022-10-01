from flask import flash, redirect, render_template, request, url_for
from cloudinary.uploader import upload
from flaskr import app

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
        upload_result = upload(file)
        print(upload_result)
    else:
        flash("File type not allowed!")
        return redirect(url_for("index"))

    return redirect(url_for("index"))

