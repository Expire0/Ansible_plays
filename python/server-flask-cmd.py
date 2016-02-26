#sample code to run a server using Flask and display the data via a webpage
# Make the WSGI interface available at the top level so wfastcgi can get it.
from flask import Flask
import subprocess
import os
app = Flask(__name__)
wsgi_app = app.wsgi_app

@app.route('/')
def hello():
    cmd = ["df", "-h"]
    proc = subprocess.Popen(cmd,stdout =subprocess.PIPE,
            stderr=subprocess.PIPE,stdin=subprocess.PIPE) #using stdout to capture the output 
    output, status = proc.communicate()
    return "<pre> %s </pre>"  % output  #keeping the ouput the same 

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
##run with ./filename 
