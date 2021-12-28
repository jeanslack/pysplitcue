# -*- coding: UTF-8 -*-

# Porpose: Contains test cases for the splitcue object.
# Rev: Dec.28.2021

import sys
import os.path
import shutil
import unittest

PATH = os.path.realpath(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(PATH)))

try:
    from pysplitcue import splitcue

except ImportError as error:
    sys.exit(error)

WORKDIR = os.path.dirname(PATH)
TMPDIR = os.path.join(WORKDIR, 'tmp')
FILECUE = os.path.join(WORKDIR, 'Three Samples.cue')
FILEFLAC = os.path.join(WORKDIR, 'Three Samples.flac')
OUTFORMAT = 'flac'

if os.path.exists(TMPDIR):
    shutil.rmtree(TMPDIR)

os.mkdir(TMPDIR, mode=0o777)


class CheckCueSheetTestCase(unittest.TestCase):
    """
    Test case for cue sheet file check out
    """
    def test_invalid_file(self):
        """
        test error with an invalid filename.

        """
        check = splitcue.cuefile_check(FILECUE)
        self.assertEqual(check, True)


class ParseCueSheetTestCase(unittest.TestCase):
    """
    Test case to get data from cue sheet file
    """
    def test_read_cue_file(self):
        """
        test to parse file cue
        """
        titletracks = splitcue.cuefile_reading(FILECUE,
                                               OUTFORMAT
                                               )
        #self.assertTrue(bool(titletracks), True)
        self.assertIs(bool(titletracks), True)


class RunSplitCommandTestCase(unittest.TestCase):
    """
    Test case to run command for splitting
    """
    def test_run_splitting(self):
        """
        test to splitting files using shntool
        """
        split = splitcue.run_process_splitting(FILECUE,
                                               FILEFLAC,
                                               OUTFORMAT,
                                               TMPDIR
                                               )
        self.assertEqual(split, None)


class RunTagCommandTestCase(unittest.TestCase):
    """
    Test case to run command for tagging
    """
    def test_run_cuetag(self):
        """
        test to tagging files using cuetag
        """
        os.chdir(TMPDIR)
        tag = splitcue.run_process_tagging(FILECUE, OUTFORMAT)
        self.assertEqual(tag, None)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
