class Converter(object):
    """
    Converter logic

    Requires the processing module to do its work.

    """

    def __init__(self, module):
        self.module = module

    def single(self, input_file, output_file):
        """
        Plot a single frame

        Reads data from input_file and saves result into output_file.

        """
        self.module.process(input_file, output_file)


    def series(self, frames, input_format, output_format, polling=None):
        """
        Plot given frames

        Reads files from snap_dir and plots the frames specified, which are then
        saved in image_dir.

        image_fmt and snap_fmt can be used to specify file name formatting
        convention.

        """
        for frame in frames:
            input_file = input_format.format(frame)
            output_file = output_format.format(frame)
            if polling:
                while not os.path.isfile(input_file):
                    time.sleep(polling)
            self.single(input_file, output_file)
