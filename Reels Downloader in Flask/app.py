"""Flask Login Example and instagram fallowing find"""

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def getfollowedby(url):
    """View Instagram user follower count"""
    link = f'https://www.instagram.com/{url}/?__a=1&__d=1'
    user = requests.get(link)

    a = user.json()
    # print(a)
    b = a['graphql']['user']['edge_followed_by']['count']
    
    c = a['graphql']['user']['edge_felix_video_timeline']['edges']
    d = a['graphql']['user']['edge_owner_to_timeline_media']['edges']
    return b, c+d

def getname(url):
    """Split the URL from the username"""
    url = list(url.split('/'))
    
    if 'https:' in url:
        url = url[3]
    else:
        url = url[0]
    return url

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = getname(request.form['username'])
        data = getfollowedby(username)

        return render_template('index.html', 
            username=username, data=data[0], 
            full_data=data[1], 
            )
    return render_template('index.html')

if __name__ == '__main__':
    app.secret_key = "123"
    app.run(debug=True)

# https://www.instagram.com/p/Cp1dAGxrmAl/?&__a=1&__d=1
