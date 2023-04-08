# import requests;print(requests.get('https://www.instagram.com/p/CqTC9d3vYlX/?__a=1&__d=1').json()['graphql']['shortcode_media']['edge_sidecar_to_children']['edges'][0]['node']['video_url'])

from flask import Flask, request, redirect
import requests

app = Flask(__name__)
@app.route('/') 
def home():
    try:
        return redirect(requests.get(f'https://www.instagram.com/p/{request.args.get("id")}/?__a=1&__d=1').json()['graphql']['shortcode_media']['video_url'], code=200)
    except:
        return 'Replace id parameter with your REEL_ID : <a href="http://127.0.0.1:5000/?id=ClwrpW1BB-R">id = ClwrpW1BB-R</a>'

if __name__ =='__main__':  
    app.run(debug = True)
