#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
"""
import sys
import os
import argparse
import subprocess
import urlparse

import youtube
import video
import algorithm

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

def get_subclips(youtube_id):
    """
    Retrieves the timestamps from the youtube comments
    section and applies a series of algorithms to generate
    a few subsections of the video where it is popular.
    """
    client = youtube.get_client()
    timestamps = youtube.get_timestamp_list(client=client, video_id=youtube_id)
    duration_seconds = youtube.get_duration(client, video_id=youtube_id)
    clips = algorithm.get_clips(timestamps, duration_seconds)
    print 'CLIPS:', clips
    return clips

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='download and summarize youtube videos')
    parser.add_argument('-f', '--filename', type=str, default='', help='Enter a filename')
    parser.add_argument('-u', '--url', type=str, default='', help='Enter a youtube url')
    args = parser.parse_args()

    filename = args.filename
    url = args.url

    youtube_id = download_video(url)
    clips = get_subclips(youtube_id)
    rechunk_video(youtube_id+".mp4", "summarized-"+youtube_id+".mp4", clips)
