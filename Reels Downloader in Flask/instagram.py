"""View Instagram user follower count from Instagram public api"""
import requests

def getfollowedby(url):
    """View Instagram user follower count"""
    link = f'https://www.instagram.com/{url}/?__a=1&__d=1'
    user = requests.get(link)

    a = user.json()
    b = a['graphql']['user']['edge_followed_by']['count']
    
    c = a['graphql']['user']['edge_felix_video_timeline']['edges']
    d = a['graphql']['user']['edge_owner_to_timeline_media']['edges']
    return b, c+d

def getname(url):
    """Split the URL from the username"""
    sp = url.split("instagram.com/")
    rep = sp[0].replace("/", "")
    return rep

'''
	<table border="10">
		<thead>
			<tr>
			<th>Key</th>
			<th>Value</th>
			</tr>
		</thead>
		
		<tbody>
			{% for i in edge_felix_video_timeline %}
				{% for key, value in i.items() %}
					<tr>
						<td> {{ key }} </td>
						{% for x, y in value.items() %}
							<tr>
								<td> {{ x }} </td>
								<td> {{ y }} </td>
							</tr>
						{% endfor %}

					</tr>
				{% endfor %}
			{% endfor %}
		</tbody>
	</table>
'''