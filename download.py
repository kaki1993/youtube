# coding: utf-8
"""This requires google-api and pytube:
# google api
pip install --upgrade google-api-python-client
# pytube
pip install pytube
"""

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
from pytube import YouTube

# setting
outdir = "/Users/masaki/Desktop/"
DEVELOPER_KEY = "AIzaSyD7ZkNekMVqcp-U6jPa_Ig_hQAjlO6hBAw"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
YOUTUBE_URL = "https://www.youtube.com/watch?v="

# youtube search
def youtube_search(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        q=options.q,
        part="id,snippet",
        maxResults=options.max_results
    ).execute()

    videos = []
    channels = []
    playlists = []

    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append((search_result["snippet"]["title"],
                           search_result["id"]["videoId"]))
        elif search_result["id"]["kind"] == "youtube#channel":
            channels.append((search_result["snippet"]["title"],
                             search_result["id"]["channelId"]))
        elif search_result["id"]["kind"] == "youtube#playlist":
            playlists.append((search_result["snippet"]["title"],
                              search_result["id"]["playlistId"]))

#     print("Videos:\n", "\n".join(videos), "\n")
#     print("Channels:\n", "\n".join(channels), "\n")
#     print("Playlists:\n", "\n".join(playlists), "\n")

    return videos, channels, playlists


# youtube download
def youtube_download(videoId, outdir):
    YouTube(YOUTUBE_URL+videoId).streams.first().download(outdir)
