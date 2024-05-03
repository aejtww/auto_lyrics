import requests
import list_title_videotitles as A

a = int(input())
b = int(input())
print("now searching lyrics {}".format(A.lists_videotitles[a][b]))
search_word ="歌詞 + {}".format(A.lists_videotitles[a][b])

def google_search(query, api_key, cx):
    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={query}"
    response = requests.get(url)
    data = response.json()
    return data

# APIキーと検索エンジンID（cx）を設定
api_key = "AIzaSyA7BzwMKg0eKkBBnBZJ-_IxYt5a3nOhgf8"
cx = "33e6eb811f35f4a61"

# 検索クエリを入力
query = search_word

# Google検索を実行して結果を取得
search_results = google_search(query, api_key, cx)

# 結果を出力
for i, item in enumerate(search_results.get('items', [])[:5], 1):
    print(item['title'])
    print(item['link'])
    print()