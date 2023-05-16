# upload-images-cloudinary-python
A simple application to demonstrate how you can upload and save your images in Cloudinary.

## Table of contents

- [Built with](#built-with)
- [How to run it?](#how-to-run-it)

## Preview image

![PREVIEW](./preview/preview.png)

## Built with

- HTML
- SCSS
- Python and Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-WTF
- SQLite

## How to run it?

1. Clone this repository on your computer:
```Shell
$ git clone https://github.com/Remy349/upload-images-cloudinary-python.git

$ cd upload-images-cloudinary-python
```

2. Once inside the repository create and activate a virtual environment:
```Shell
# For Linux
$ python3 -m venv venv
# Now activate the virtual enviroment
$ . venv/bin/activate

# For Windows(py -3 -m venv venv or...)
$ python -m venv venv
# Now activate the virtual enviroment
$ venv\Scripts\activate
```

3. Install the requirements:
```Shell
# For Windows could be just "pip"
(venv) $ pip3 install -r requirements.txt
```

4. You will have to add an ".env" file and in it you will have to add the following values for the necessary environment variables:
```Shell
# .env - Example values

SECRET_KEY=yourownsecretkey
CLOUDINARY_CLOUD_NAME=yourCloudinaryCLOUD_NAME
CLOUDINARY_API_KEY=yourCloudinaryAPI_KEY
CLOUDINARY_API_SECRET=yourCloudinaryAPI_SECRET
```

To get this data from Cloudinary, you must create your own account, it is very easy to do, I leave you the link:

- [Cloudinary](https://cloudinary.com/)

5. Now just run the following commands in the terminal to add the tables to the database and run the server:
```Shell
# Adding table models to the database
(venv) $ flask db upgrade

# Run the server
(venv) $ flask run
* Serving Flask app 'application.py'
* Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
```

### Developed by Santiago de Jesús Moraga Caldera - Remy349(GitHub)
