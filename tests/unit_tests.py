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
from vsummarize import algorithm

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

class AlgorithmTestCase(unittest.TestCase):
    def runTest(self):
        self.sort_timestamp_test()

    @print_test
    def sort_timestamp_test(self):
        timestamps = [u'1:46', u'1:51', u'00:40', u'1:43', u'1:35', u'1:44',
                u'1:47', u'2:22', u'02:48', u'1:21', u'1:32', u'1:39']
        sorted_times = algorithm.sort_timestamps(timestamps)

        print 'sorted times', sorted_times, 'old times', timestamps

if __name__ == '__main__':
    # unittest.main() # run all units and their cases

    suite = unittest.TestSuite()
    suite.addTest(AlgorithmTestCase())

    unittest.TextTestRunner().run(suite)
