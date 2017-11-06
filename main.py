import json

import spotipy
import spotipy.util as util

client_id = "e6376f7ecbfb45799240881e368d4d18"
client_secret = "47d3d26c9ba9492a9b0e6cc278712c99"
redirect_uri = "https://anderc.com"
username = 'c.andersen2012@gmail.com'
scope = 'user-library-read'

token = util.prompt_for_user_token(username, scope, client_id=client_id,
                                   client_secret=client_secret, redirect_uri=redirect_uri)

export_result = []

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_playlists()
    for item in results['items']:
        playlist = {}
        playlist['collaborative'] = item['collaborative']
        playlist['apiUrl'] = item['href']
        playlist['name'] = item['name']
        playlist['public'] = item['public']

        playlist_result = sp.user_playlist(item['owner']['id'], item['id'])
        tracks = []
        for track in playlist_result['tracks']['items']:
            tracks.append(track['track']['id'])

        playlist['tracks'] = tracks
        export_result.append(playlist)

    export_file = open('data/playlist.json', 'w')
    export_file.write(json.dumps(export_result))
    print(export_result)
else:
    print("Can't get token for christian")
