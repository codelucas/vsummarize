Pythonic Video summarization
----------------------------

Enough of nlp text summarization algorithms.. Time for some video summarization!
We take advantage of youtube's commenting timestamp system to generate
a new + shorter video from a youtube video's referenced timestamps.


.. code-block:: pycon

    >>> import vsummarize

    >>> meta_data = vsummarize.summarize('/path/to/video.mp4', '/new/path/finished.mp4')

    >>> print meta_data.timestamps
    ['0:12', '0:12', '0:14', ..., '12:31']

    >>> print meta_data.video_hotspots
    [('0:12', '0:16'), ..., ('12:31', '13:01')]


Features
--------


License
-------


