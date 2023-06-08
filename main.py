import streamlit as st
import subprocess

# ボタンの作成
increment = st.button("make Playlist")

# ボタンが押された場合の処理
if increment:
    # 別のPythonファイルを実行するコマンド
    command = ["python", "playlist.py"]

    # コマンドを実行して外部プロセスを起動
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # プロセスの終了を待機
    stdout, stderr = process.communicate()


# ボタンの作成
increment = st.button("start music")

if increment:
    # 別のPythonファイルを実行するコマンド
    command = ["python", "start.py"]

    # コマンドを実行して外部プロセスを起動
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # プロセスの終了を待機
    stdout, stderr = process.communicate()


# ボタンの作成
increment = st.button("stop music")

if increment:
    # 別のPythonファイルを実行するコマンド
    command = ["python", "stop.py"]

    # コマンドを実行して外部プロセスを起動
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # プロセスの終了を待機
    stdout, stderr = process.communicate()
