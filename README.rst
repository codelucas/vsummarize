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
on the ``ffmpeg`` and ``pygame`` libraries.

Be sure you have `pip <http://www.pip-installer.org/>`_.

The installation instructions are as follow:

**OSX**:

::

    $ brew install mercurial
    $ brew install sdl sdl_image sdl_mixer sdl_ttf smpeg portmidi 
    $ sudo pip install hg+http://bitbucket.org/pygame/pygame

    $ brew install ffmpeg

    $ pip install vsummarize


**Ubuntu**:

::

    $ sudo apt-get install python-pygame
    $ sudo apt-get install libsdl1.2-dev
    $ sudo apt-get install libsmpeg-dev

    $ wget http://ffmpeg.gusari.org/static/64bit/ffmpeg.static.64bit.2014-01-25.tar.gz

    $ cd packages/pygame
    $ python2.7 setup.py build
    $ sudo python2.7 setup.py install

    $ pip install vsummarize


Warning
-------

Because this is such a resource intensive task & lib (especially if you are
actually using the summarized ``.mp4`` generation feature), you may notice on a few
videos the ``.mp4`` generation fail due to an *OS memory exception*. This means
that you don't have the RAM for ``ffmpeg`` to fork processes to subchunk out your video.

I don't know any solution to this besides hoping for impovements in the moviepy or 
ffmpeg libraries (or just get more RAM).

Also, ``moviepy`` functions manipulate your terminal console environment.. it's a bit funky.
You will know what i'm talking about when you see it. One way around this is to
pipe your entire command into some file so moveipy's weird console never appears (it's
getting piped into your file).

License
-------

Authored and maintained by `Lucas Ou-Yang`_.

We use `moviepy`_ and `ffmpeg`_ for video manipulation.
We also use google's youtube api.

Please feel free to `email & contact me`_ if you run into issues or just would like
to talk about the future of this library!

.. _`Lucas Ou-Yang`: http://codelucas.com
.. _`email & contact me`: mailto:lucasyangpersonal@gmail.com
.. _`moviepy`: https://github.com/Zulko/moviepy 
.. _`ffmpeg`: http://www.ffmpeg.org/ 
