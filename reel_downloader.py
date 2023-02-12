import re

reel_id = input('Enter reel link :')
reel_id = list(reel_id.split('/'))

if len(reel_id[4]) == 11:
    reel_id = reel_id[4]
elif len(reel_id[5]) == 11:
    reel_id = reel_id[5]
else:
    reel_id = 'CoT1MflIGJg' # default value if error.

link = f'https://www.instagram.com/reel/{reel_id}/'
dev_link = link + '?__a=1&__d=dis'
print('\nClick below link ...')
print(dev_link)

dev_json = input('''

1. Click above link
2. Copy site content
3. Paste below.

''')

def reel_audio():
    a = re.search(r'\b(progressive_download_url)\b', dev_json)
    start_index = a.start()
    start_index = start_index + 3 + len('progressive_download_url')
    dev_json[start_index:]

    b = re.search(r'\b(",")\b', dev_json[start_index + 1:])
    end_index = b.start() + 1
    end_index += start_index

    audio_link = dev_json[start_index : end_index]
    print('Audio Link : ', audio_link)
    
def reel_video():
    a = re.search(r'\b(o1/v/t16/f1/m82)\b', dev_json)
    check_index = a.start()
    start_index = check_index - 40

    b = re.search(r'\b(o1/v/t16/f1/m82)\b', dev_json[check_index+1:])
    end_index = b.start()
    end_index = end_index - 70
    end_index += start_index

    video_link = dev_json[start_index : end_index]
    print('Video Link : ', video_link)

reel_audio()
print()
reel_video()