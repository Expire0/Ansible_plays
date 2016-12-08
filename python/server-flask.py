#sample code to run a server using Flask
# Make the WSGI interface available at the top level so wfastcgi can get it.
from flask import Flask
app = Flask(__name__)
wsgi_app = app.wsgi_app

@app.route('/')
def hello():
    return "hey"

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
