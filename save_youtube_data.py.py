import requests
import json

# 替換為你的 API 密鑰
API_KEY = 'YOUR_YOUTUBE_API_KEY'

# 替換為你要查詢的 YouTube 頻道 ID
CHANNEL_ID = 'YOUR_CHANNEL_ID'

# YouTube Data API 的 URL
url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={CHANNEL_ID}&key={API_KEY}'

def save_json_response_to_file():
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        # 將 JSON 資料存成檔案，使用複寫模式。如果檔案不存在，會自動創建。
        with open('youtube_channel_data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
        print("API 回應已儲存至 'youtube_channel_data.json'")
    else:
        print(f"HTTP 請求失敗，狀態碼: {response.status_code}")

if __name__ == '__main__':
    save_json_response_to_file()
