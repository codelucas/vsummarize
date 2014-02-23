Pythonic Video summarization
----------------------------

Enough of nlp text summarization algorithms.. Presenting: **video summarization**!
We take advantage of youtube's comment timestamp video references to generate
a summarized + shorter video from any youtube video.

A glance:
---------

.. code-block:: pycon

    >>> import vsummarize

    >>> meta_data = vsummarize.summarize('http://youtube.com/watch?v=...', 'summarized.mp4')

After this command, the physical summarized mp4 is now in whatever
path you saved it into. We return some meta_data incase you need it.

Timestamps from youtube comments, important b/c our algorithm generates 
summaries via the comments

.. code-block:: pycon

    >>> print meta_data.summary_clips
    [('0:12', '0:16'), ..., ('12:31', '13:01')]

    >>> print meta_data.comment_timestamps 
    ['0:12', '0:12', '0:14', ..., '12:31']

    >>> print meta_data.video_duration # in seconds
    65 

Sometimes, actually a lot of the time, (even in my product www.shorten.tv), 
you just want a list of hot video clips instead of physically summarizing
a video into a new `.mp4` because of the resource consumption.

To do this, simply ignore the output video file parameter.

The physical, summarized .mp4 has NOT been generated. We just
retrieve a set of meta data of what would have happened if we did
summaraize it.

.. code-block:: pycon

    >>> meta_data = vsummarize.summarize('http://youtube.com/watch?v=...')

    >>> print meta_data.hot_clips
    [('0:12', '0:16'), ..., ('12:31', '13:01')]

To actually generate a summary, we use ffmpeg + moviepy
along with the above hot_clip timestamps to stitch together the video.

Documentation
-------------

Comming soon!

Features
--------

- ``.mp4`` video summarization
- youtube comments timestamp extraction
- youtube video hot timestamp extraction
- youtube video hot sub-clip extraction

Get it now
----------

Because of the various video manipulation libraries we use, installing
vsummarize is a multi-step process. First, be sure you have 
`pip <http://www.pip-installer.org/>`_.

::

    $ pip install vsummarize

    Now we need our video manipulation binaries.

    $ sudo apt-get install python-pygame
    $ sudo apt-get install libsdl1.2-dev
    $ sudo apt-get install libsmpeg-dev
    $ sudo apt-get install imagemagick
    
    $ cd packages/pygame
    $ python2.7 setup.py build
    $ sudo python2.7 setup.py install
    
    $ wget http://ffmpeg.gusari.org/static/64bit/ffmpeg.static.64bit.2014-01-25.tar.gz


License
-------

Authored and maintained by `Lucas Ou-Yang`_.

vsummarize uses `moviepy` and `ffmpeg` for video manipulation.
We also use google's youtube api.

Please feel free to `email & contact me`_ if you run into issues or just would like
to talk about the future of this library!

.. _`Lucas Ou-Yang`: http://codelucas.com
.. _`email & contact me`: mailto:lucasyangpersonal@gmail.com
.. _`moviepy`: https://github.com/Zulko/moviepy 
.. _`ffmpeg`: http://www.ffmpeg.org/ 
