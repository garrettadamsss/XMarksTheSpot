from sys import argv
from flask import Flask, request, make_response, redirect, url_for
from flask import render_template
import os
# from werkzeug import secure_filename



app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():    
    html = render_template('index.html')
    response = make_response(html)
    return response

# endpoint to upload image file to an image folder in our app
# doesn't work yet
# @app.route('/uploadimage', methods=['POST'])
# def uploadImage():
#     if request.method == 'POST':
#         f = request.files['file']   
#         # need to put as environment variable
#         f.save(os.path.join('/images', secure_filename(f.filename)))
#         return

if __name__ == '__main__':
    if len(argv) != 2:
        print('Usage: ' + argv[0] + ' port')
        exit(1)
    app.run(host='0.0.0.0', port=int(argv[1]), debug=True)

