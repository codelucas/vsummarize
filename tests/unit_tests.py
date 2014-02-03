#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
All unit tests for vSummarize should be contained here.
"""
__title__ = 'vSummarize'
__author__ = 'Lucas Ou-Yang'
__license__ = 'MIT'
__copyright__ = 'Copyright 2014, Lucas Ou-Yang'

import sys
import os
import unittest
import time
import codecs

TEST_DIR = os.path.abspath(os.path.dirname(__file__))
PARENT_DIR = os.path.join(TEST_DIR, '..')

# tests is a separate module, insert parent dir manually
sys.path.insert(0, PARENT_DIR)

import vsummarize
from vsummarize import algorithm, youtube

def print_test(method):
    """
    Utility method for print verbalizing test suite, prints out
    time taken for test and functions name, and status.
    """
    def run(*args, **kw):
        ts = time.time()
        print '\ttesting function %r' % method.__name__
        method(*args, **kw)
        te = time.time()
        print '\t[OK] in %r %2.2f sec' % (method.__name__, te-ts)
    return run

class GeneralUnitTestCases(unittest.TestCase):
    def runTest(self):
        self.TIMESTAMPS = [u'1:46', u'1:51', u'00:40', u'1:43', u'1:35', u'1:44',
                u'1:47', u'2:22', u'02:48', u'1:21', u'1:32', u'1:39']
        self.DURATION = '197'
        self.client = youtube.get_client()
        self.video_id = 'p5HXQ1HFDgA'

        self.conversion_test()
        self.get_timestamps_test()
        self.sort_timestamp_test()
        self.get_hotspot_test()

    @print_test
    def conversion_test(self):
        assert algorithm.convert_to_seconds(u'1:40') == 100

    @print_test
    def get_timestamps_test(self):
        timestamps = youtube.get_timestamp_list(self.client, self.video_id)
        duration_seconds = youtube.get_duration(self.client, self.video_id)
        assert self.DURATION == duration_seconds

    @print_test
    def sort_timestamp_test(self):
        self.sorted_times = algorithm.sort_timestamps(self.TIMESTAMPS)
        SORTED_TIMES = [u'00:40', u'1:21', u'1:32', u'1:35', u'1:39',
                u'1:43', u'1:44', u'1:46', u'1:47', u'1:51', u'2:22', u'02:48']

        assert self.sorted_times == SORTED_TIMES

    @print_test
    def get_hotspot_test(self):
        self.hotspots = algorithm.get_hotspots(self.sorted_times, self.DURATION)
        print 'timestamps', self.sorted_times
        print '\r\n'
        print 'hotspots', self.hotspots

    @print_test
    def expand_hotspot_test(self):
        pass

    @print_test
    def video_summarize_test(self):
        pass

if __name__ == '__main__':
    # unittest.main() # run all units and their cases

    suite = unittest.TestSuite()
    suite.addTest(GeneralUnitTestCases())

    unittest.TextTestRunner().run(suite)
