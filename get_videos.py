import lists as A
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import pickle

# 変数nはプレイリストのindex、listsからはプレイリストの名前とそのidを取得
n = 1
playlist_title = A.playlist_titles[n]
playlist_id = A.playlist_ids[n]

# YouTube Data API v3を使用するための認証情報ファイルのパス
credentials_path = 'client_secret_454390944112-8q5tj4i997auipt0fqbrr6ihka6vjv6v.apps.googleusercontent.com.json'


# 認証情報をロードする関数
def load_credentials():
    creds = None
    # 以前に保存された認証情報のロードを試みる
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # 保存された認証情報がない場合、ユーザーによる認証を行う
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_path, ['https://www.googleapis.com/auth/youtube.readonly'])
            creds = flow.run_local_server(port=0)
        # 認証情報を保存
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds

# YouTube Data API v3のクライアントを作成
def create_youtube_client():
    credentials = load_credentials()
    youtube = build('youtube', 'v3', credentials=credentials)
    return youtube

# 再生リスト内の動画の情報を取得する関数
def get_playlist_videos(playlist_id):
    youtube = create_youtube_client()
    videos = []
    next_page_token = None
    
    # ページングを使用してすべての動画を取得
    while True:
        # playlistItems.listメソッドを使用して再生リスト内の動画を取得
        playlist_request = youtube.playlistItems().list(
            part='snippet',
            playlistId=playlist_id,
            maxResults=50,  # 1ページあたりの最大結果数
            pageToken=next_page_token
        )
        playlist_response = playlist_request.execute()
        
        # 動画の情報をリストに追加
        videos.extend(playlist_response['items'])
        
        # 次のページがあるか確認
        next_page_token = playlist_response.get('nextPageToken')
        if not next_page_token:
            break
    
    return videos

# 再生リスト内の動画のタイトルを取得する関数
def get_video_titles(playlist_id):
    videos = get_playlist_videos(playlist_id)
    titles = [video['snippet']['title'] for video in videos]
    return titles


# メイン関数
def main():
    video_titles= []
    video_titles = get_video_titles(playlist_id)
            
    return playlist_title,video_titles

result = main()
print(result[0])
print(result[1])