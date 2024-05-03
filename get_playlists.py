from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import pickle

# YouTube Data API v3を使用するための認証情報ファイルのパス
credentials_path = 'client_secret_454390944112-8q5tj4i997auipt0fqbrr6ihka6vjv6v.apps.googleusercontent.com.json'
play_lists = []
lists_videos = []


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

# 再生リストを取得する関数
def get_playlists():
    youtube = create_youtube_client()
    request = youtube.playlists().list(part='snippet,contentDetails', mine=True)
    response = request.execute()
    playlists = response.get('items', [])
    return playlists  

# メイン関数
def main():
    playlists = get_playlists()
    if playlists:
        play_lists = []
        play_lists_id = []
        for playlist in playlists:
            play_lists.append(playlist['snippet']['title'])
            play_lists_id.append(playlist['id'])
            #for video_title in video_titles:
                #print(f"{video_title}")

    else:
        print("再生リストが見つかりませんでした。")
    
    return play_lists,play_lists_id

result = main()
print(result[0])
print(result[1])