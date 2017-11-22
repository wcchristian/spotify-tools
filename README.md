# Spotify Backup/Restore
A Tool to Backup and Restore playlists and libraries to Spotify. This tool is primarily meant to do a full backup and restore your spotify data to a new account. Very helpful in the case where you created a spotify account with facebook and want to create a new account directly with spotify.

# Backup Items
* Artist Follows
* Playlists
* Saved Songs (Library)
* TODO: User follows

# Usage
To use the spotify backup tool, simply follow the guides below in order.

_Note: I highly recommend that you 'clean' up your account before export. Make sure you have all of the playlists you want so you import everything in nice and clean into your new account._

## Spotify Token
You can get an access token by one of two ways.

### Web Console

You can log in to the spotify web console and retrieve a token, make sure to give adequate permissions (scope) check main.py for more information.

### Within the App

To use this program, you must first get a spotify access token. You can do this by
navigating [here](https://developer.spotify.com/my-applications/#!/applications/create) and following the steps below.

1. Enter the application name "Spotify Backup Tool"
2. Set the reply url to https://google.com
3. Enter a short description that will help you remember whay this registration is for.
4. Collect the Client ID and the Client Secret
5. Click Save.

You will provide this information to the tool so that the tool can correctly authenticate to your account.

_You can use the same client id and secret for multiple accounts with this tool._

## Setting up python

This program was built to run on python 3.6

To run this app you must install the required libraries into the python installation, feel free to create a virtual 
environment as to not add the required libraries directly onto your python installation.

The requirements are in the requirements.txt file.



## Getting a token
After the requirements are installed, simply run:

```sh
python main.py
```

Once the program is running, select the Generate Token Option.
After selecting, the program will ask you for the email address of the client, as well as the client id and client 
secret you got when setting up the app in spotify.

The app will then open a browser and spotify will ask you to approve the app (you may also have to log in to your 
spotify account here).

Once you authorize the app, it will redirect you to google.com. Copy the url from the address bar and paste it in the
 console for the tool.

 Once you do this, the tool will return your token, save this as you will need it for running backup and restore. You
  will need to generate a new token for a destination account when running the restore. 

  If you are having touble try deleting cookies and clearing cache in the browser when getting a token for a second 
  spotify account.

 ## Running a Restore
If you already have a token, just run the restore option at the main menu.

 # Submitting a feature.
 Feel free to submit bugs and new feature proposals including new things to be backed up. Just navigate to the issues
  section of this repo.

Please be as descriptive as possible when writing the issues.


 # Libraries Used
 [requests](https://github.com/requests/requests)

 [spotipy](https://github.com/plamere/spotipy)

 [tqdm](https://github.com/noamraph/tqdm)