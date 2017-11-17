import json
import os

import spotipy
from tqdm import tqdm


def export_playlists(token):
    if token:
        print('Exporting playlists to data/playlists.json...')
        sp = spotipy.Spotify(auth=token)
        limit = 50
        offset = 0
        current_size = -1

        export_result = []
        while current_size == -1 or current_size == limit:
            results = sp.current_user_playlists(limit=limit, offset=offset)
            offset += limit
            current_size = len(results['items'])
            for item in tqdm(results['items']):
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

        if not os.path.exists('data'):
            os.makedirs('data')

        export_file = open('data/playlist.json', 'w')
        export_file.write(json.dumps(export_result))
        print('Finished exporting playlists.')
    else:
        print("Token must be passed to be able to export playlists.")


def export_follows(token):
    if token:
        print('Exporting follows to data/follows.json...')
        sp = spotipy.Spotify(auth=token)
        limit = 50
        after = None
        current_size = -1
        export_result = []

        while current_size == -1 or current_size == limit:
            followed_artists = sp.current_user_followed_artists(limit, after)
            current_size = len(followed_artists['artists']['items'])
            after = followed_artists['artists']['items'][current_size - 1]['id']

            for item in tqdm(followed_artists['artists']['items']):
                export_result.append(item['id'])

        if not os.path.exists('data'):
            os.makedirs('data')

        export_file = open('data/follows.json', 'w')
        export_file.write(json.dumps(export_result))
        print('Finished exporting follows.')
    else:
        print("Token must be passed to be able to export user follows.")


def export_library_tracks(token):
    if token:
        print('Exporting tracks to data/tracks.json...')
        sp = spotipy.Spotify(auth=token)
        limit = 50
        offset = 0
        current_size = -1
        export_result = []

        while current_size == -1 or current_size == limit:
            saved_tracks = sp.current_user_saved_tracks(limit, offset)
            current_size = len(saved_tracks['items'])
            offset += limit

            for item in tqdm(saved_tracks['items']):
                export_result.append(item['track']['id'])

        if not os.path.exists('data'):
            os.makedirs('data')

        export_file = open('data/tracks.json', 'w')
        export_file.write(json.dumps(export_result))
        print("Finished exporting tracks.")
    else:
        print("Token must be passed to be able to export user tracks.")
