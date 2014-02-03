#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
__title__ = 'vSummarize'
__author__ = 'Lucas Ou-Yang'
__license__ = 'MIT'
__copyright__ = 'Copyright 2014, Lucas Ou-Yang'

# from moviepy.editor import *

def convert_to_seconds(timestamp):
    """
    Takes a string timestamp: [\d]{0,1}\d:\d\d and
    returns an int representing the number of seconds.
    """
    if ':' not in timestamp:
        raise Exception('Funky shit happening w/ timestamps')
    minutes = 0
    seconds = 0
    tsplit = timestamp.split(':')
    seconds = int(tsplit[1])
    minutes = int(tsplit[0])
    return (minutes * 60) + seconds

def sort_timestamps(timestamps):
    """
    Sort string timestamps by earliest-latest order
    """
    return sorted(timestamps, key=lambda num: convert_to_seconds(num))

def hotness_delta(video_duration):
    """
    Hotness delta is the number of seconds apart where
    two timestamps are considered to be referencing same event.

    For us, this is dependent on the length of the video. A
    longer video will have a longer hotness delta.
    """
    if not isinstance(video_duration, int):
        video_duration = int(video_duration)
    if video_duration < 10:
        return 1
    elif video_duration < 120:
        return 3
    elif video_duration < 300:
        return 6
    return 10

def get_hotspots(timestamps, video_duration):
    """
    We will now compute hotspot points; a hotspot point is a
    timestamp point with a higher proportion of other timestamps
    close to it.  Assert length(hotspots) < length(timestamps).

    Make sure that the range does not go before the timestamp of
    0:00 or after the timestamp of the movie length.

    Sort our hot-clips by position in video and combine into a
    video summary!
    """
    sorted_times = sort_timestamps(timestamps)
    delta = hotness_delta(video_duration)
    seen = {}

    for i, time in enumerate(sorted_times):
        for j, other_time in enumerate(sorted_times):
            if i == j:
                continue
            if i in seen or j in seen:
                continue
            i_time = convert_to_seconds(time)
            i_other_time = convert_to_seconds(other_time)

            if abs(i_time - i_other_time) <= delta:
                seen[i] = time
                seen[j] = time

    return seen.values()

def expand_hotspots(hotspots, video_duration):
    """
    Inputs a list of hot timestamps, expands each one into a
    "hot clip".

    A hotclip is a (timestampA, timestampB) tuple while a
    hotspot is just a timestamp. So we will be returning a
    list of tuples.
    """
    delta = hotness_delta(video_duration)
    expanded_spots = []
    for hotspot in hotspots:
        expanded_spots.append( (hotspot-delta, hotspot+delta) )
    return expanded_spots

def summarize(timestamps, video_duration):
    """
    Inputs a list of comment timestamps along with total
    video length.

    Combines hot-clips points together to form a summarized video.
    """
    hotspots = get_hotspots(timestamps, video_duration)
    hotclips = expand_hotspots(hotspots, video_duration)

