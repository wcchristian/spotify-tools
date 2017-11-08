import spotipy


def follow_artists(token):
    sp = spotipy.Spotify(auth=token)
