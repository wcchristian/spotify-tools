import os

import spotipy.util as util

from spotify import spotify_export as sp_export
from spotify import spotify_import as sp_import


# Functions


def backup(token):
    sp_export.export_playlists(token)
    sp_export.export_follows(token)
    sp_export.export_library_tracks(token)


def restore(token):
    sp_import.import_playlists_from_file(token)
    sp_import.import_tracks_from_file(token)
    sp_import.follow_artists_from_file(token)


# Main Stuff

def main():
    scopes = 'user-library-read user-follow-read playlist-read-private playlist-modify-public playlist-modify-private ' \
             'user-library-modify user-follow-modify user-follow-modify'
    redirect_uri = "https://google.com"

    run = True
    while run:
        option = input('Choose an option.\n 1:Generate Token\n 2:Backup\n 3:Restore\n 0:Exit\n\n Option: ')

        if option == '1':
            username = input('Enter a source spotify email address: ')
            client_id = input('Enter a source client_id: ')
            client_secret = input('Enter a source client_secret: ')

            token = util.prompt_for_user_token(username, scopes, client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri)
            print('\nToken: ' + token)
            os.remove('.cache-' + username)

        if option == '2':
            token = input('Token: ')
            backup(token)
            print('==================== Backup Complete for user =========================')

        if option == '3':
            token = input('Token: ')
            restore(token)
            print('==================== Restore Complete for user =========================')

        if option == '0':
            run = False


if __name__ == "__main__":
    main()
