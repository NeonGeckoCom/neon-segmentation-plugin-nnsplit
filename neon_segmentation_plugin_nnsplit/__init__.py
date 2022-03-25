from nnsplit import NNSplit

from ovos_plugin_manager.segmentation import Segmenter


class NNSplitSegmenter(Segmenter):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.splitter = NNSplit(self.lang.split("-")[0])

    def segment(self, text):
        chunks = []
        splitted = self.splitter.split(super().segment(text))
        for splits in splitted:
            for split in splits:
                # HACK - there is some bug in NNSplit, cant get the strings because iterating casts to list again...
                stringified = str(split).replace("[", "").replace("]", "").strip()
                stringified = [s[1:].split(", whitespace=")[0][:-1] for s in stringified.split("Token(text=")]
                stringified = " ".join(stringified).strip()\
                              .replace(" n't", "n't")\
                              .replace(" , ", ", ")\
                              .replace(" . ", ". ")\
                              .replace(" ...", "...") \
                              .replace(" !", "!") \
                              .replace(" ?", "?")
                if stringified.endswith(" ."):
                    stringified = stringified[:-2] + "."

                chunks.append(stringified)
        return chunks or [text]
