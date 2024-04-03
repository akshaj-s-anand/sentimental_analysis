import csv
import googleapiclient.discovery

youtube = googleapiclient.discovery.build("youtube", "v3", developerKey="AIzaSyCI-6t8ePD4eCvZPM-nmh4Q339NRAZQCC4")

def search_videos(youtube, **kwargs):
    video_ids = []
    results = youtube.search().list(part='id', **kwargs).execute()

    while results:
        for item in results["items"]:
            if item["id"]["kind"] == "youtube#video":
                video_id = item["id"]["videoId"]
                video_ids.append(video_id)
                print(video_id)
        if "nextPageToken" in results:
            kwargs["pageToken"] = results["nextPageToken"]
            results = youtube.search().list(part='id', **kwargs).execute()
        else:
            break

    return video_ids

"""query = "COVID-19"
year = 2020
video_ids = search_videos(youtube, q=query, type="video", publishedAfter=f"{year}-01-01T00:00:00Z", publishedBefore=f"{year}-12-31T23:59:59Z", regionCode="US", maxResults=10000000)"""

query = "COVID-19"
year = 2019
month = 10
video_ids = search_videos(youtube, q=query, type="video", publishedAfter=f"{year}-{month:02d}-01T00:00:00Z", publishedBefore=f"{year}-{month:02d}-31T23:59:59Z", regionCode="IN", maxResults=10000000)
# change the date of "published before when you change the month"
#https://www.iso.org/iso-3166-country-codes.html (visit this website for country code)
with open("video_ids.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["video_id"])
    for video_id in video_ids:
        writer.writerow([video_id])
""" errors
 1. dupicate values                         (fixed - added code)
 2. = comes before some video ids           (fixed - must be solved in excel)
 3. error while changing year and month     (fixed - )
"""
# cleaning the videos
# Read the CSV file and remove duplicates
video_ids = set()
with open('video_ids.csv', 'r', newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        if row:
            video_ids.add(row[0])

# Remove blank rows
video_ids.discard('')

# Overwrite the CSV file
with open('video_ids.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    for video_id in video_ids:
        csv_writer.writerow([video_id])