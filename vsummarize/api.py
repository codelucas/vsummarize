#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
High level summarization commands to be directly imported
by __init__.py
"""
import sys
import os
import subprocess
import urlparse

try:
    from . import youtube
    from . import algorithm
    from . import video
except Exception, e:
    print 'This fails when not run as a module', str(e)
    import youtube
    import algorithm
    import video

parent_dir = os.path.dirname(os.path.abspath(__file__))

def rechunk_video(filename, new_filename, clips):
    video.summarize(filename, new_filename, clips)

def download_video(url):
    """
    Downloads a video on youtube, saves the video id
    and then saves the video as the video id. We also
    return the video id.
    """
    parsed_url = urlparse.urlparse(url)
    youtube_id = urlparse.parse_qs(parsed_url.query)['v'][0]
    subprocess.call(["youtube-dl", "--id", url]) # save video id as filename
    return youtube_id

def get_subclips(youtube_id, meta_data):
    """
    Retrieves the timestamps from the youtube comments
    section and applies a series of algorithms to generate
    a few subsections of the video where it is popular.
    """
    client = youtube.get_client()
    timestamps = youtube.get_timestamp_list(client=client, video_id=youtube_id)
    duration_seconds = youtube.get_duration(client, video_id=youtube_id)
    clips = algorithm.get_clips(timestamps, duration_seconds)

    meta_data.timestamps = timestamps
    meta_data.hot_clips = clips
    meta_data.duration = duration_seconds

    return clips

def summarize(youtube_url, output=None):
    """
    If the output is None, we don't generate a summary
    and simply return metadata.
    """
    # default downloads to "youtubeID.mp4"
    youtube_id = download_video(youtube_url)

    meta_data = VideoMetadata()
    clips = get_subclips(youtube_id, meta_data)

    if output is not None:
        rechunk_video(youtube_id+".mp4", output, clips)
        return meta_data
    else:
        return meta_data

class VideoMetadata(object):

    def __init__(self):
        self.hot_clips = []
        self.timestamps = []
        self.duration = None


if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='download and summarize youtube videos')
    # parser.add_argument('-f', '--filename', type=str, default='', help='Enter a filename')
    # parser.add_argument('-u', '--url', type=str, default='', help='Enter a youtube url')
    # args = parser.parse_args()
    # filename = args.filename
    # url = args.url
    summarize('http://www.youtube.com/watch?v=YkADj0TPrJA', 'finished_from_api.mp4')
