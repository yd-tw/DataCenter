import requests
import json
from datetime import datetime

API_KEY = 'YOUR_YOUTUBE_API_KEY'

CHANNEL_ID = 'UCMvvMRGp5nthxeogBo6psFg'

url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={CHANNEL_ID}&key={API_KEY}'

def save_json_response_to_file():
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data['timestamp'] = timestamp

        with open('youtube_data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
        print("API 回應檔案已儲存成功")
    else:
        print(f"HTTP 請求失敗，狀態碼: {response.status_code}")

if __name__ == '__main__':
    save_json_response_to_file()
