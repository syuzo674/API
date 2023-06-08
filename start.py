import spotipy
from spotipy.oauth2 import SpotifyOAuth

# 認証パート Authentication part
username = ""
my_id = ""
my_secret = ""
redirect_uri = "http://localhost:8888/callback"

# アプリの権限付与に使用する
scope = "user-read-playback-state user-modify-playback-state user-read-currently-playing streaming playlist-read-private"

# アクセストークンの取得
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=my_id, client_secret=my_secret, redirect_uri=redirect_uri, scope=scope
    )
)

# ユーザーのプレイリスト一覧を取得
playlists = sp.current_user_playlists()

# プレイリストのIDを取得
# プレイリスト名からIDを取得
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
devices = sp.devices()
device_id = devices["devices"][1]["id"]

# 取得したプレイリストを再生
playlist_uri = "spotify:playlist:" + playlist_id
sp.start_playback(device_id=device_id, context_uri=playlist_uri)
