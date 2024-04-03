import os
import csv
import google.auth
import re
import json
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def fetch_video_comments(youtube, csv_writer, **kwargs):
    results = youtube.commentThreads().list(**kwargs).execute()

    while results:
        for item in results['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            csv_writer.writerow([comment])
            print(comment)
        if 'nextPageToken' in results:
            kwargs['pageToken'] = results['nextPageToken']
            results = youtube.commentThreads().list(**kwargs).execute()
        else:
            break


    

def get_youtube_service(api_version='v3', api_service_name='youtube', scopes=['https://www.googleapis.com/auth/youtube.force-ssl']):
    # Update this line to use your API key
    api_key = 'AIzaSyAv2qQOXJLuJQ25PHhs6E-kjM1h4JSLvC0'  # Replace 'YOUR_API_KEY' with your actual API key
    youtube = build(api_service_name, api_version, developerKey=api_key)
    return youtube


def fetch_comments_for_video_ids(video_ids):
    youtube = get_youtube_service()

    with open('comments.csv', 'w', newline='', encoding='utf-8') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['Comment'])

        for video_id in video_ids:
            if not re.match(r'^[a-zA-Z0-9_-]{11}$', video_id):
                print(f"Skipping invalid video ID: {video_id}")
                continue

            print(f"Fetching comments for video ID: {video_id}")
            
            try:
                fetch_video_comments(youtube, csv_writer, part='snippet', videoId=video_id, textFormat='plainText')
                print(f"Finished fetching comments for video ID: {video_id}")
            except HttpError as e:
                error = json.loads(e.content)['error']['errors'][0]
                if error['reason'] == 'commentsDisabled':
                    print(f"Comments are disabled for video ID: {video_id}")
                else:
                    print(f"An error occurred while fetching comments for video ID {video_id}: {error}")
                    continue



if __name__ == '__main__':
    csv_path = 'video_ids.csv'
    video_ids = []
    with open(csv_path, 'r') as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            video_ids.append(row[0])

    fetch_comments_for_video_ids(video_ids)
