import os
import requests
import json
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('YOUTUBE_API_KEY')

output_dir = 'youtube'
os.makedirs(output_dir, exist_ok=True)

CHANNELS = {
    'playeryd': 'UCMvvMRGp5nthxeogBo6psFg',
    'codecat-tw': 'UCZg6zXjhK1RT5NDejLcapSA',
    'YT-bright_moon_fall_night': 'UCovAQCyXar8ra_WC2bLGqIA',
    '曹哥議題': 'UC5ZtFyy8wjO7TCMWovFd21Q',
}

def fetch_youtube_data(name, id):
    url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={id}&key={API_KEY}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data['timestamp'] = timestamp

        with open(os.path.join(output_dir, f'{name}.json'), 'w') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
        print(f"頻道 {name} 的 API 回應檔案已儲存成功: {name}")
    else:
        print(f"頻道 {name} 的 HTTP 請求失敗，狀態碼: {response.status_code}")

def main():
    for name, id in CHANNELS.items():
        fetch_youtube_data(name, id)

if __name__ == '__main__':
    main()
