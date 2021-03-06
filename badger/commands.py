"""
Conversion logic

"""

import time
import os.path


class Converter(object):
    """
    Holds reference to a module and provides processing functionality

    Requires the processing module to do its work.

    """

    def __init__(self, module):
        self.module = module

    def single(self, index, polling=None):
        """
        Process a single input file

        Reads data from input_file and saves result into output_file.

        """
        while True:
            try:
                self.module.process(index)
                return
            except:
                if polling:
                    time.sleep(polling)
                else:
                    raise

    def series(self, indices, polling=None):
        """
        Process a series of input files

        input_format and output_format are format strings used to define the
        frames.

        """
        for index in indices:
            self.single(index, polling)
