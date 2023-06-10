import streamlit as st
import subprocess
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

# 認証パート Authentication part
username = ""
my_id = ""
my_secret = ""
redirect_uri = "http://localhost:8888/callback"

# アプリの権限付与に使用する
scope = "user-library-read user-read-playback-state playlist-read-private user-read-currently-playing streaming user-read-recently-played playlist-read-collaborative playlist-modify-public playlist-modify-private"

# 認証情報の取得
auth_manager = SpotifyOAuth(
    client_id=my_id,
    client_secret=my_secret,
    redirect_uri=redirect_uri,
    scope=scope,
    username=username,
)

# 認証情報の保存
auth_manager.get_access_token(as_dict=False)
os.environ["SPOTIPY_CLIENT_ID"] = my_id
os.environ["SPOTIPY_CLIENT_SECRET"] = my_secret
os.environ["SPOTIPY_REDIRECT_URI"] = redirect_uri
os.environ["SPOTIPY_USERNAME"] = username

# プレイリストボタンの作成
make_playlist_button = st.button("make Playlist")

# ボタンが押された場合の処理
if make_playlist_button:
    # 別のPythonファイルを実行するコマンド
    command = ["python", "playlist.py"]

    # コマンドを実行して外部プロセスを起動
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # プロセスの終了を待機
    stdout, stderr = process.communicate()

# 検索ボタンの作成
start_music_button = st.button("start music")

# ボタンが押された場合の処理
if start_music_button:
    # 別のPythonファイルを実行するコマンド
    command = ["python", "start.py"]

    # コマンドを実行して外部プロセスを起動
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # プロセスの終了を待機
    stdout, stderr = process.communicate()


# 停止ボタンの作成
stop_music_button = st.button("stop music")

# ボタンが押された場合の処理
if stop_music_button:
    # 別のPythonファイルを実行するコマンド
    command = ["python", "stop.py"]

    # コマンドを実行して外部プロセスを起動
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # プロセスの終了を待機
    stdout, stderr = process.communicate()
