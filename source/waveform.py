import wave


class Waveform:
    """
    Represents the data extracted from a single .wav file.
    """
    filepath = ""
    num_channels = 1
    sample_width = 1
    framerate = 1
    num_frames = 1
    compression_type = ""
    data = bytes()

    def __init__(self, path):
        self.filepath = path
        with wave.open(self.filepath, mode='rb') as stream:
            self.num_channels = stream.getnchannels()
            self.sample_width = stream.getsampwidth()
            self.framerate = stream.getframerate()
            self.num_frames = stream.getnframes()
            self.compression_type = stream.getcompname()
            self.data = stream.readframes(self.num_frames)

    def get_audio_sample_time(self):
        """
        Gets the length of the audio sample.
        :return: Sample length, in seconds.
        """
        return self.num_frames / self.framerate