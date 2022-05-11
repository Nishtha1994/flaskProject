from flask import Flask,render_template,g, request
from pathlib import Path
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/ping')
def get_response():
    myfile = Path('temp/ok')
    if myfile.is_file():
        return "OK"
    return '504 Gateway Timeout',504


@app.route('/img')
def get_image():
    print(request.endpoint)
    return render_template("index.html")

@app.after_request
def after_request(response):
    if request.endpoint== 'get_image':
        print("Response is",response.status)
        print("Response header is",response.headers)
        print("IP address is",request.remote_addr)
        print("Request path is ",request.path)
        print("Request Method is ",request.method)
        print("Request Address is:",request.remote_addr)
        print("Request URL is:",request.url)
        print(request.user_agent.string)
        print(request.user_agent.platform)
        print(request.user_agent.version)
        dict(request.args)
        print(request.view_args)
        return response
    else:
        return response

if __name__ == '__main__':
    handler = RotatingFileHandler('app.log', maxBytes=100000, backupCount=3)
    logger = logging.getLogger('tdm')
    logger.setLevel(logging.ERROR)
    logger.addHandler(handler)
    app.run(port=5000)


