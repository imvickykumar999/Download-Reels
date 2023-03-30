"""Flask Login Example and instagram fallowing find"""

from flask import Flask, render_template, request
import requests

app = Flask(__name__)
app.jinja_env.globals.update(zip=zip)


def getreelsinfo(url = 'ClwrpW1BB-R'):
    """View Instagram user follower count"""
    link = f'https://www.instagram.com/p/{url}/?&__a=1&__d=1'

    user = requests.get(link)
    a = user.json()
    x = a['graphql']['shortcode_media']

    if x['is_video']:
        b = [x['video_url']]
        c = [x['display_url']]
    else:
        try:
            d,e = [],[]
            for i in x['edge_sidecar_to_children']['edges']:
                y = i['node']

                try:
                    b = y['video_url']
                    c = y['display_resources'][-1]['src']
                except:
                    b = "Click Below Link to Download Photo" 
                    c = y['display_url']

                d.append(b)
                e.append(c)
            b,c = d,e

        except:
            b = ["Click Below Link to Download Photo"] 
            c = [x['display_url']]
    return c,b


def getfollowedby(url = 'vix.bot'):
    """View Instagram user follower count"""
    link = f'https://www.instagram.com/{url}/?__a=1&__d=dis'
    user = requests.get(link)

    a = user.json()
    b = a['graphql']['user']['edge_followed_by']['count']
    
    c = a['graphql']['user']['edge_felix_video_timeline']['edges']
    d = a['graphql']['user']['edge_owner_to_timeline_media']['edges']
    return b, c+d


def getname(url):
    """Split the URL from the username"""
    url = list(url.split('/'))

    if len(url) == 1:
        url = url[0]
        itis = 'user'

        if len(url) == 11 and url[0] == 'C':
            itis = 'reels'
    else:
        if url[3] == 'reels' or url[3] == 'reel' or url[3] == 'p':
            url = url[4]
            itis = 'reels'
        else:
            url = url[3]
            itis = 'user'

    return url, itis


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = getname(request.form['username'])

        if username[1] == 'user':
            data = getfollowedby(username[0])
        elif len(username[0]) == 11:
            data = getreelsinfo(username[0])
        else:
            data = (["Private Reels are not Supported, Try above link"], 
                    ["https://indown.io/private-reels-download"])
        
        return render_template('index.html', 
            username=username[0], data=data[0], 
            itis=username[1], full_data=data[1],
            )
    return render_template('index.html', data='')


if __name__ == '__main__':
    app.secret_key = "123"
    app.run(debug=True)
