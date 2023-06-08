import spotipy
import spotipy.util as util

# 入力パート Input part
creat_playlist = "test_list_00"

# 認証パート Authentication part
username = ""
my_id = ""  # client ID
my_secret = ""  # client secret
redirect_uri = "http://localhost:8888/callback"

# アプリの権限付与に使用する
scope = "user-library-read user-read-playback-state playlist-read-private user-read-recently-played playlist-read-collaborative playlist-modify-public playlist-modify-private"

token = util.prompt_for_user_token(username, scope, my_id, my_secret, redirect_uri)
spotify = spotipy.Spotify(auth=token)

spotify.user_playlist_create(user=username, name=creat_playlist)
