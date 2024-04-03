import csv
import googleapiclient.discovery

youtube = googleapiclient.discovery.build("youtube", "v3", developerKey="AIzaSyAv2qQOXJLuJQ25PHhs6E-kjM1h4JSLvC0")

def search_videos(youtube, **kwargs):
    video_ids = []
    results = youtube.search().list(part='id', **kwargs).execute()

    while results:
        for item in results["items"]:
            if item["id"]["kind"] == "youtube#video":
                video_id = item["id"]["videoId"]
                video_ids.append(video_id)

        if "nextPageToken" in results:
            kwargs["pageToken"] = results["nextPageToken"]
            results = youtube.search().list(part='id', **kwargs).execute()
        else:
            break

    return video_ids

query = "COVID-19"
year = 2020
video_ids = search_videos(youtube, q=query, type="video", publishedAfter=f"{year}-01-01T00:00:00Z", publishedBefore=f"{year}-12-31T23:59:59Z", regionCode="US", maxResults=10000000)

with open("video_ids.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["video_id"])
    for video_id in video_ids:
        writer.writerow([video_id])
