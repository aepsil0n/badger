"""
Conversion logic

"""


class Converter(object):
    """
    Holds reference to a module and provides processing functionality

    Requires the processing module to do its work.

    """

    def __init__(self, module):
        self.module = module

    def single(self, input_file, output_file):
        """
        Process a single input file

        Reads data from input_file and saves result into output_file.

        """
        self.module.process(input_file, output_file)

    def series(self, frames, input_format, output_format, polling=None):
        """
        Process a series of input files

        input_format and output_format are format strings used to define the
        frames.

        """
        for frame in frames:
            input_file = input_format.format(frame)
            output_file = output_format.format(frame)
            if polling:
                while not os.path.isfile(input_file):
                    time.sleep(polling)
            self.single(input_file, output_file)
