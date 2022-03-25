from nnsplit import NNSplit

from ovos_plugin_manager.segmentation import Segmenter


class NNSplitSegmenter(Segmenter):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.splitter = NNSplit(self.lang.split("-")[0])

    def segment(self, text):
        chunks = []
        for split in self.splitter.split(super().segment(text))[0]:
            # HACK - there is some bug in NNSplit, cant get the strings because iterating casts to list again...
            stringified = str(split)[1:-1].strip()
            stringified = [s.split("', whitespace=")[0] for s in stringified.split("Token(text='")]
            chunks.append(" ".join(stringified).strip())
        return chunks or [text]
