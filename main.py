import os
from datetime import datetime
# from dotenv import load_dotenv
from youtube import fetch_all_channels
from instagram import get_instagram_data

# load_dotenv() # 只需在本地執行，伺服器端取消這行

API_KEY = os.getenv('YOUTUBE_API_KEY')

if __name__ == '__main__':
    fetch_all_channels(API_KEY)
    get_instagram_data()

    with open('timestamp.txt', 'a+') as timestamp_file:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        timestamp_file.write(f'Update in: {timestamp}\n')
