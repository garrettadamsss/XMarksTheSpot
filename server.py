from sys import argv
from flask import Flask, request, make_response, redirect, url_for
from flask import render_template
import requests
import os
from entry import Entry
from database import Database
# from werkzeug import secure_filename



app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():    
    html = render_template('index.html')
    response = make_response(html)
    return response


@app.route('/location')
def location():
    html = render_template('location.html')
    resp = make_response(html)
    return resp

# endpoint to upload image file to an image folder in our app
# doesn't work yet
# @app.route('/uploadimage', methods=['POST'])
# def uploadImage():
#     if request.method == 'POST':
#         f = request.files['file']   
#         # need to put as environment variable
#         f.save(os.path.join('/images', secure_filename(f.filename)))
#         return


# adds user entry into database
@app.route('/addEntry', methods=['POST'])
def addEntry():


    placename = request.args.get('placeName')
    description = request.args.get('description')
    location = request.args.get('location')

    # still need to write something that can process and handle images

    entry = Entry(placename=placename, description=description, location=location)

    database = Database()

    database.insertEntry(entry)

    html = render_template('index.html')
    response = make_response(html)
    return response







if __name__ == '__main__':
    # if len(argv) != 2:
    #     print('Usage: ' + argv[0] + ' port')
    #     exit(1)
    app.run()

