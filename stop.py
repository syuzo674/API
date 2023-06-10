import spotipy
import os

# 認証パート Authentication part
username = os.getenv("SPOTIPY_USERNAME")
my_id = os.getenv("SPOTIPY_CLIENT_ID")
my_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")
scope = os.getenv("SPOTIPY_SCOPE")

# 認証マネージャーの作成
auth_manager = spotipy.oauth2.SpotifyOAuth(
    client_id=my_id,
    client_secret=my_secret,
    redirect_uri=redirect_uri,
    scope=scope,
    username=username,
)

# Spotifyオブジェクトの作成
spotify = spotipy.Spotify(auth_manager=auth_manager)

# 曲の一時停止
spotify.pause_playback()
