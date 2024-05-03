# auto_lyrics
動画の歌詞を検索し表示する
現在、就活の為、パブリックにしているが、テスト中である。
基本的に自身以外の環境で動くかは調べていない。
事前準備として環境の構築、youtubeAPIの導入が必要。
また、youtubeAPIの利用を無料で行うために、あまり、多くの動画を取得することには対応していない。
(その為、一度にできることを複数に分けていたり、得られた情報を手動で格納していたりする。)

## pip install
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

## get_playlists.py
YouTubeにログインし、プレイリストがあれば取得
### lists.py
get_playlists.pyで得られたプレイリストの名前とidを手動で格納

## get_videos.py
プレイリストから動画のタイトルを取得する
### list_titles_videotitles.py
get_viddeos.pydで得られたプレイリストの名前とリスト内の動画のタイトルを手動で格納

## get_lyrics.py
歌ネットから歌詞を取得し、htmlに出力

## 
電子書籍風に出力
