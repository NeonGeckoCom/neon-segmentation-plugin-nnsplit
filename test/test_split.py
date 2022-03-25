import unittest

from neon_segmentation_plugin_nnsplit import NNSplitSegmenter


class TestNNSplitSegmenter(unittest.TestCase):

    def test_segment(self):
        solver = NNSplitSegmenter()
        self.assertEqual(solver.segment(
            "This is a test This is another test."),
            ["This is a test", "This is another test"])
        #self.assertEqual(solver.segment(
        #    "I am Batman I live in gotham"),
        #    ["I am Batman", "I live in gotham"])
