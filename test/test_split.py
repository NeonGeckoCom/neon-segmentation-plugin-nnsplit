import unittest

from neon_segmentation_plugin_nnsplit import NNSplitSegmenter


class TestNNSplitSegmenter(unittest.TestCase):

    def test_segment(self):
        solver = NNSplitSegmenter()
        self.assertEqual(solver.segment(
            "This is a test This is another test"),
            ["This is a test", "This is another test"])
        #self.assertEqual(solver.segment(
        #    "I am Batman I live in gotham"),
        #    ["I am Batman", "I live in gotham"])

        # test internal base class heuristic still works
        test_sent = "Mr. Smith bought cheapsite.com for 1.5 million " \
                    "dollars, i.e. he paid a lot for it. Did he mind? Adam " \
                    "Jones Jr. thinks he didn't. In any case, this isn't true..." \
                    " Well, with a probability of .9 it isn't."
        self.assertEqual(
            solver.segment(test_sent),
            [
                'Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it.',
                'Did he mind?',
                "Adam Jones Jr. thinks he didn't.",
                "In any case, this isn't true...",
                "Well, with a probability of .9 it isn't."
            ]
        )
