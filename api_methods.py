import pandas as pd
from datetime import datetime

def get_chanel_stats(youtube, channel_ids):
    all_data = []

    request = youtube.channels().list(
        part="snippet, contentDetails, statistics",
        id=','.join(channel_ids)
    )

    response = request.execute()

    for item in response["items"]:
        data = {
            'channel_id': item["id"],
            'channelName': item["snippet"]["title"],
            'subscribers': item["statistics"]["subscriberCount"],
            'views': item["statistics"]["viewCount"],
            'totalVideos': item["statistics"]["videoCount"],
            'playlistId': item["contentDetails"]["relatedPlaylists"]["uploads"]
        }
        all_data.append(data)

    return pd.DataFrame(all_data)

def get_video_comments(youtube, video_ids):
    comment_list = []

    for video_id in video_ids:
        # Get video details
        video_request = youtube.videos().list(
            part='snippet,contentDetails,statistics',
            id=video_id
        )
        video_response = video_request.execute()

        for video_item in video_response["items"]:
            video_details = video_item['snippet']
            video_content_details = video_item['contentDetails']
            video_statistics = video_item['statistics']

            video_Published_Date_str = video_details['publishedAt']
            video_Published_Date = datetime.strptime(video_Published_Date_str, '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d %H:%M:%S')

            # Get video comments
            nextPageToken = None  # Initialize nextPageToken

            while True:
                comments_request = youtube.commentThreads().list(
                    part='snippet,replies',
                    videoId=video_id,
                    maxResults=50,
                    pageToken=nextPageToken
                )
                comments_response = comments_request.execute()

                for item in comments_response["items"]:
                    comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                    comment_ID = item['snippet']['topLevelComment']['id']
                    reply_Count = item['snippet']['totalReplyCount']
                    like_Count = item['snippet']['topLevelComment']['snippet']['likeCount']
                    date_str = item['snippet']['topLevelComment']['snippet']['publishedAt']
                    comment_date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d %H:%M:%S')

                    videoId = item['snippet']['videoId']
                    user_ID = item['snippet']['topLevelComment']['snippet']['authorChannelId']['value']

                    video_duration_parts = video_content_details['duration'].replace('PT', '').replace('S', '').replace(
                        'M', ':').replace('H', ':').split(':')

                    hours = int(video_duration_parts[0]) if len(video_duration_parts) > 2 else 0
                    minutes = int(video_duration_parts[-2]) if len(video_duration_parts) > 1 else 0
                    seconds = int(video_duration_parts[-1]) if len(video_duration_parts) > 0 else 0

                    video_length = hours * 3600 + minutes * 60 + seconds

                    view_count = video_statistics["viewCount"]
                    like_count = video_statistics["likeCount"]
                    comment_count = video_statistics["commentCount"]

                    comment_list.append({
                        'Video_ID': videoId,
                        'Video_Title': video_details['title'],
                        'Video_Description': video_details['description'],
                        'Video_Published_Date': video_Published_Date,
                        'channel_id': video_details['channelId'],
                        'channelName': video_details['channelTitle'],
                        'Video_Length': video_length,
                        'Video_Views': view_count,
                        'Video_Likes': like_count,
                        'Video_Comments': comment_count,
                        'Comments': comment,
                        'Comment_ID': comment_ID,
                        'Comment_Reply': reply_Count,
                        'Comment_Likes': like_Count,
                        'Comment_Date': comment_date,
                        'User_ID': user_ID
                    })

                # Check if there is another page
                nextPageToken = comments_response.get('nextPageToken')
                if not nextPageToken:
                    break  # Exit the loop if there is no next page

    return comment_list