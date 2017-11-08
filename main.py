import spotipy.util as util

import export as Export

client_id = "e6376f7ecbfb45799240881e368d4d18"
client_secret = "47d3d26c9ba9492a9b0e6cc278712c99"
redirect_uri = "https://anderc.com"
username = 'c.andersen2012@gmail.com'
scopes = 'user-library-read user-follow-read'

token = util.prompt_for_user_token(username, scopes, client_id=client_id,
                                   client_secret=client_secret, redirect_uri=redirect_uri)

Export.export_playlists(token)
Export.export_follows(token)
Export.export_library_tracks(token)
