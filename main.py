import os

import spotipy.util as util

import export as Export
import spotify_import as Import


# Functions


def backup():
    from_token = util.prompt_for_user_token(username_src, scopes, client_id=client_id_src,
                                            client_secret=client_secret_src, redirect_uri=redirect_uri)
    Export.export_playlists(from_token)
    Export.export_follows(from_token)
    Export.export_library_tracks(from_token)
    os.remove('.cache-' + username_src)


def restore():
    to_token = util.prompt_for_user_token(username_dest, scopes, client_id=client_id_dest,
                                          client_secret=client_secret_dest,
                                          redirect_uri=redirect_uri)

    Import.import_tracks_from_file(to_token)
    Import.import_tracks_from_file(to_token)
    Import.follow_artists_from_file(to_token)
    os.remove('.cache-' + username_dest)


def backup_restore():
    backup()
    restore()


# Main Stuff

scopes = 'user-library-read user-follow-read playlist-read-private playlist-modify-public playlist-modify-private'
redirect_uri = "https://google.com"

option = input('Choose an option 1 is backup, 2 is restore, 3 is both')

username_src = input('Enter a source spotify email address: ')
client_id_src = input('Enter a source client_id: ')
client_secret_src = input('Enter a source client_secret: ')
backup()
print('==================== Backup Complete for user ' + username_src + '=========================')

username_dest = input('Enter a destination spotify email address: ')
client_id_dest = input('Enter a destination client_id: ')
client_secret_dest = input('Enter a destination client_secret: ')
restore()
print('==================== Restore Complete for user ' + username_dest + '=========================')
