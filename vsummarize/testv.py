#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import sys
import os
from moviepy.editor import *

clip = VideoFileClip("cascada.mp4").subclip(0, 10)
clip2 = VideoFileClip("cascada.mp4").subclip(20, 30)
final_clip = concatenate([clip, clip2])

txt_clip = TextClip("blah", fontsize=20, color='white')
txt_clip = txt_clip.set_pos('bottom').set_duration(20)

final_clip = CompositeVideoClip([clip, txt_clip])
final_clip.to_videofile("solution.mp4", fps=25, codec='mpeg4')
final_clip.to_videofile("solution.avi", fps=25, codec='mpeg4')
final_clip.to_videofile("solution.mp4", remove_temp=False)


final_clip.to_videofile('test.mp4', audio_codec='mp3', codec'mpeg4')
to_videofile("solution.ogv", fps=25, codec='libtheora')
