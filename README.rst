Pythonic Video summarization
----------------------------

Sick of nlp text summarization? Presenting: **video summarization**!

We take advantage of youtube's comment timestamp video references to generate
a summarized + shorter video from any youtube video.

A glance:
---------

.. code-block:: pycon

    >>> import vsummarize

    >>> data = vsummarize.summarize('http://youtube.com/watch?v=...', output='shorter.mp4')

After this command, the physical summarized ``.mp4`` is now in the output path 
you provided. We return some meta data incase you need it.

Timestamps from youtube comments are included and are important b/c our 
algorithm generates summaries via the comments and their timestamps.

.. code-block:: pycon

    >>> print data.hot_clips
    [('0:12', '0:16'), ..., ('12:31', '13:01')]

    >>> print data.timestamps 
    ['0:12', '0:12', '0:14', ..., '12:31']

    >>> print data.duration # in seconds
    65 

A demo:
-------

I tested this software on a 1 hour long Obama speech.

Original video (59 minutes): http://www.youtube.com/watch?v=hed1nP9X7pI

Summarized video (3:30 minutes): http://www.youtube.com/watch?v=aDYDN9lsSHg

A lot of the time, (even in my product www.shorten.tv), 
you just want a list of hot video clips instead of physically summarizing
a video into a new ``.mp4`` because of the resource consumption.

To do this, simply ignore the output video file parameter.

.. code-block:: pycon

    >>> data = vsummarize.summarize('http://youtube.com/watch?v=...')

    >>> print data.hot_clips
    [('0:12', '0:16'), ..., ('12:31', '13:01')]


The physical, summarized ``.mp4`` has NOT been generated. We just
retrieved a set of meta data of what would have happened if we did
summarize it.

To actually generate a summary, we use **ffmpeg + moviepy**
along with the above ``.hot_clips`` video sequences to stitch together the video.

Features
--------

- ``.mp4`` video summarization
- youtube comments timestamp extraction
- youtube video hot timestamp extraction
- youtube video hot sub-clip extraction

Get it now
----------

Because I use both OSX and Ubuntu, I have clear instructions on setting
up this project in both platforms. However, I can't guarantee
anything for the other platforms besides give installation advice.

We use ``moviepy``, the python video manipulation library, which in turn depends 
on the ``ffmpeg`` library.

Be sure you have `pip <http://www.pip-installer.org/>`_.

The installation instructions are as follows:

**OSX**:

::

    $ brew install ffmpeg


**Ubuntu**:

::

    $ curl -O http://ffmpeg.gusari.org/static/64bit/ffmpeg.static.64bit.2014-02-28.tar.gz
    $ tar -zxvf ffmpeg.static.64bit.2014-02-28.tar.gz 
    $ sudo mv ffmpeg ffprobe /usr/local/bin/.
    $ rm ffmpeg.static.64bit.2014-02-28.tar.gz 


And lastly, don't forget to install ``vSummarize`` itself!

::

    $ pip install vsummarize


**This app uses the google gdata api**. I have a file named ``settings.py`` which contains
my personal api keys. I've removed that file from this repo for obvious
reasons but i've included a file called ``rename_to_settings.py`` which has two api key
values for you to cleanly fill out. Also, please rename that file to ``settings.py`` after
you are finished!


Warning
-------

Because this is such a resource intensive task & lib (especially if you are
actually using the summarized ``.mp4`` generation feature), you may notice on a few
videos the ``.mp4`` generation fail due to an *OS memory exception*. This means
that you don't have the RAM for ``ffmpeg`` to fork processes to subchunk out your video.


License
-------

Authored and maintained by `Lucas Ou-Yang`_.
Shoutout to `Zulko`_ for helping code and giving advice to 
some parts of this project.

We use `moviepy`_ and `ffmpeg`_ for video manipulation.
We also use google's youtube api.
Please feel free to `email & contact me`_ if you run into issues or just would like
to talk about the future of this library!

.. _`Lucas Ou-Yang`: http://codelucas.com
.. _`email & contact me`: mailto:lucasyangpersonal@gmail.com
.. _`moviepy`: https://github.com/Zulko/moviepy 
.. _`ffmpeg`: http://www.ffmpeg.org/ 
.. _`Zulko`: https://github.com/Zulko
