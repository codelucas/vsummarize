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
    seconds = int(timestamp.split(':')[1])
    minutes = int(timestamp.split(':')[0])

    return (minutes * 60) + seconds

def sort_timestamps(timestamps):
    """
    Sort string timestamps by earliest-latest order
    """
    return sorted(timestamps, key=lambda num: convert_to_seconds(num))

def get_hotspots(timestamps):
    """
    Input list of sorted timestamps.
    We will now compute hotspot points; a hotspot point is a
    timestamp point with a higher proportion of other timestamps
    close to it.  Assert length(hotspots) < length(timestamps).

    Make sure that the range does not go before the timestamp of
    0:00 or after the timestamp of the movie length.

    Sort our hot-clips by position in video and combine into a
    video summary!
    """
    pass

def summarize(timestamps, videolen):
    """
    Inputs a list of comment timestamps along with total
    video length.

    Combines hot-clips points together to form a summarized video.
    """
    pass

if __name__ == '__main__':
    timestamps = [u'1:46', u'1:51', u'00:40', u'1:43', u'1:35', u'1:44',
                u'1:47', u'2:22', u'02:48', u'1:21', u'1:32', u'1:39']
