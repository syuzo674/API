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

# ユーザーのプレイリスト一覧を取得
playlists = spotify.current_user_playlists()

# プレイリストIDをプレイリスト名から取得
target_playlist_name = "test_list_00"

playlist_id = None
for playlist in playlists["items"]:
    if playlist["name"] == target_playlist_name:
        playlist_id = playlist["id"]
        break

if playlist_id:
    print("プレイリスト名:", target_playlist_name)
    print("プレイリストID:", playlist_id)
else:
    print("指定したプレイリストが存在しません。")

# デバイスの取得
devices = spotify.devices()
device_id = devices["devices"][1]["id"]

# 取得したプレイリストを再生
playlist_uri = "spotify:playlist:" + playlist_id
spotify.start_playback(device_id=device_id, context_uri=playlist_uri)
