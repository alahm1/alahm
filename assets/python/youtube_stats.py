import os
import pandas as pd
from dotenv import load_dotenv
from googleapiclient.discovery import build
import logging
import time

load_dotenv() 

API_KEY = os.getenv("YOUTUBE_API_KEY")
API_VERSION = 'v3'

youtube = build('youtube', API_VERSION, developerKey=API_KEY)

def get_channel_stats(youtube, channel_id):
    try:
        request = youtube.channels().list(
            part='snippet, statistics',
            id=channel_id
        )
        response = request.execute()

        if response['items']:
            data = {
                'channel_name': response['items'][0]['snippet']['title'],
                'total_subscribers': response['items'][0]['statistics']['subscriberCount'],
                'total_views': response['items'][0]['statistics']['viewCount'],
                'total_videos': response['items'][0]['statistics']['videoCount'],
            }
            return data
        else:
            logging.warning(f"No data found for channel ID: {channel_id}")
            return None
    except Exception as e:
        logging.error(f"Error fetching data for channel ID {channel_id}: {e}")
        return None 

# Read CSV into DataFrame
df = pd.read_csv("us_youtubers_2024.csv")

# Extract channel IDs and remove potential duplicates
channel_ids = df['NAME'].str.split('@').str[-1].unique()

# Initialize a list to keep track of channel stats
channel_stats = []

# Loop over the channel IDs and get stats for each
for channel_id in channel_ids:
    stats = get_channel_stats(youtube, channel_id)
    if stats is not None:
        channel_stats.append(stats)
    time.sleep(1)  # To manage API rate limits

# Convert the list of stats to a DataFrame
stats_df = pd.DataFrame(channel_stats)

df.reset_index(drop=True, inplace=True)
stats_df.reset_index(drop=True, inplace=True)

# Concatenate the dataframes horizontally
combined_df = pd.concat([df, stats_df], axis=1)

# Save the merged DataFrame back into a CSV file
combined_df.to_csv('youtube_data_from_python.csv', index=False)

# Display the first 10 rows
print(combined_df.head(10))
