from flask import Flask
# from flask_cors import CORS
import requests

app = Flask(__name__)
# CORS(app, resources={"/": {"origins": "http://127.0.0.1:5000/"}})

@app.route("/")
def helloWorld(url = 'CxKin2BSv3Q'):
    link = f'https://www.instagram.com/p/{url}/?&__a=1&__d=1'
    user = requests.get(link)
    a = user.json()
    return a

if __name__ == '__main__':
   app.run()