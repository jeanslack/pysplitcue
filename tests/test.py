# -*- coding: UTF-8 -*-

"""
Porpose: Contains test cases for the splitcue object.
Rev: Jan.05.2022
"""
import sys
import os.path
import unittest


PATH = os.path.realpath(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(PATH)))

try:
    from pysplitcue.splitcue import PySplitCue

    from pysplitcue.exceptions import InvalidFile

except ImportError as error:
    sys.exit(error)

WORKDIR = os.path.dirname(PATH)
FILECUE_ASCII = os.path.join(WORKDIR, 'Three Samples_ASCII.cue')
FILECUE_ISO = os.path.join(WORKDIR, 'Three Samples_ISO-8859-1.cue')
OUTFORMAT = 'flac'
OVERWRITE = "always"


class ParseCueSheetTestCaseISO(unittest.TestCase):
    """
    Test case to get data from cue sheet file
    """
    def setUp(self):
        """
        Method called to prepare the test fixture
        """
        self.args = {'outputdir': os.path.dirname(FILECUE_ISO),
                     'suffix': OUTFORMAT,
                     'overwrite': OVERWRITE}

    def test_invalid_file(self):
        """
        test to assert InvalidFile exception
        """
        fname = {'filename': '/invalid/file.cue'}

        with self.assertRaises(InvalidFile):
            PySplitCue(**{**self.args, **fname})


    def test_parser_with_iso_file_encoding(self):
        """
        test cuefile parsing with ISO-8859-1 encoding
        """
        fname = {'filename': FILECUE_ISO}
        split = PySplitCue(**{**self.args, **fname})
        parser = split.open_cuefile()
        split.cuefile.close()
        self.assertEqual(parser, None)

    def test_parser_with_ascii_file_encoding(self):
        """
        test cuefile parsing with ASCII encoding
        """

        fname = {'filename': FILECUE_ASCII}

        split = PySplitCue(**{**self.args, **fname})
        parser = split.open_cuefile()
        split.cuefile.close()
        self.assertEqual(parser, None)


def main():
    """
    Run
    """
    unittest.main()


if __name__ == '__main__':
    main()
