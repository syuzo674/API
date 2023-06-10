import spotipy
import spotipy.util as util
import os

# 認証パート Authentication part
username = os.getenv("SPOTIPY_USERNAME")
my_id = os.getenv("SPOTIPY_CLIENT_ID")
my_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")
scope = os.getenv("SPOTIPY_SCOPE")

# 認証トークンを取得
token = util.prompt_for_user_token(username, scope, my_id, my_secret, redirect_uri)
spotify = spotipy.Spotify(auth=token)

# プレイリストの命名
creat_playlist = "test_list_00"

# 取得した情報からプレイリストを作成
spotify.user_playlist_create(user=username, name=creat_playlist)
