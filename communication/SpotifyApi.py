from requests import request


class SpotifyApi:
    def __init__(self):
        # Set up Spotify connection.
        print('Foo')
        self.res = request('get', 'https://google.com')
