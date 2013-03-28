#from application import create_app
#import os
#
#
#if __name__ == '__main__':
#    port = int(os.environ.get('PORT', 5000))
#    create_app().run(debug=True, port=port)

from flask import Flask
import os


app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World!"


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    #app = create_app()
    app.run(debug=True, port=port)
