import spotipy
from spotipy.oauth2 import SpotifyOAuth

# 認証パート Authentication part
username = ""
my_id = ""
my_secret = ""
redirect_uri = "http://localhost:8888/callback"

# アプリの権限付与に使用する
scope = "user-read-playback-state user-modify-playback-state"

# アクセストークンの取得
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=my_id, client_secret=my_secret, redirect_uri=redirect_uri, scope=scope
    )
)

# 曲の一時停止
sp.pause_playback()
