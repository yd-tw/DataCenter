import instaloader
import json
import os

output_dir = 'instagram'
os.makedirs(output_dir, exist_ok=True)

usernames = ["guangdiy", "playeryd", "codecat.tw", "frc_8569"]

def get_instagram_data():
  L = instaloader.Instaloader()
  followers_data = {}

  for username in usernames:
      try:
          profile = instaloader.Profile.from_username(L.context, username)
          followers_data[username] = profile.followers
      except Exception as e:
          print(f"Error retrieving data for {username}: {e}")
      print(f"Get info of {username}")

  print(followers_data)

  try:
      with open(os.path.join(output_dir, 'followers_data.json'), 'w') as json_file:
          json.dump(followers_data, json_file)
      print("Followers data saved")
  except Exception as e:
      print(f"Error saving JSON file: {e}")
