import os
import tkinter as tk

import spotipy.util as util

import export as Export
import spotify_import as Import


# Functions


def backup():
    from_token = util.prompt_for_user_token(username_from, scopes, client_id=client_id_from,
                                            client_secret=client_secret_from, redirect_uri=redirect_uri)
    Export.export_playlists(from_token)
    Export.export_follows(from_token)
    Export.export_library_tracks(from_token)
    os.remove('.cache-' + username_from)


def restore():
    to_token = util.prompt_for_user_token(username_to, scopes, client_id=client_id_to, client_secret=client_secret_to,
                                          redirect_uri=redirect_uri)

    Import.import_tracks_from_file(to_token)
    Import.import_tracks_from_file(to_token)
    Import.follow_artists_from_file(to_token)
    os.remove('.cache-' + username_to)


# Main Stuff

client_id_from = "e6376f7ecbfb45799240881e368d4d18"
client_secret_from = "47d3d26c9ba9492a9b0e6cc278712c99"
username_from = 'c.andersen2012@gmail.com'

client_id_to = "e6376f7ecbfb45799240881e368d4d18"
client_secret_to = "47d3d26c9ba9492a9b0e6cc278712c99"
username_to = 'c.andersen2012@gmail.com'

scopes = 'user-library-read user-follow-read playlist-read-private playlist-modify-public playlist-modify-private'
redirect_uri = "https://google.com"

# UI

top = tk.Tk()
top.title('Spotify Backup Tool')
top.geometry("300x250")

client_id_label = tk.Label(top, text='client_id')
client_id_label.pack()

client_id_entry = tk.Entry(top)
client_id_entry.pack()

backup_button = tk.Button(top, text='Backup From Spotify', command=backup)
backup_button.pack()

top.mainloop()
