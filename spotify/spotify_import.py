import json

import requests
import spotipy
from tqdm import tqdm

SPOTIFY_BASE_URL = 'https://api.spotify.com/v1/'
SPOTIFY_FOLLOW_URL = 'me/following?type=artist&ids='


def import_tracks_from_file(token):
    print('Saving tracks to Spotify...')
    sp = spotipy.Spotify(auth=token)
    tracks_json = json.loads(open('data/tracks.json', 'r').read())
    for track in tqdm(tracks_json):
        track = [track]
        sp.current_user_saved_tracks_add(track)
    print('Finished saving tracks to spotify')


def import_playlists_from_file(token):
    print("Saving playlists to Spotify...")
    sp = spotipy.Spotify(auth=token)
    user_id = sp.me()['id']
    playlists_json = json.loads(open('data/playlist.json', 'r').read())
    for playlist in playlists_json:
        create_result = sp.user_playlist_create(user_id, playlist['name'], playlist['public'])
        playlist_id = create_result['id']
        for track in tqdm(playlist['tracks']):
            track = [track]
            sp.user_playlist_add_tracks(user_id, playlist_id, track)

    print('Finished saving playlists to Spotify.')


def follow_artists_from_file(token):
    print('Saving follows to Spotify...')
    follows_json = json.loads(open('data/follows.json', 'r').read())
    headers = {'Authorization': 'Bearer ' + token}
    for follow in tqdm(follows_json):
        result = requests.put(SPOTIFY_BASE_URL + SPOTIFY_FOLLOW_URL + follow, headers=headers)
        if result.status_code != 204:
            print('export failed............')
            break
    print('Finished')
