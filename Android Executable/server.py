
import requests, zipfile, os
URL = 'https://github.com/imvickykumar999/Download-Reels/raw/main/android.zip'

r = requests.get(URL, allow_redirects=True)
open('android.zip', 'wb').write(r.content)

with zipfile.ZipFile('android.zip', 'r') as zip_ref:
    zip_ref.extractall('.')

print('''

Public Server started at
http://192.168.0.103:5000

Access this link from any Device nearby.

''')
os.system('python app.py')