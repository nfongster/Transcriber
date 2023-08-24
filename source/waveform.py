import wave
import numpy as np


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
    _raw_signal = bytes()

    def __init__(self, path):
        self.filepath = path
        with wave.open(self.filepath, mode='rb') as stream:
            self.num_channels = stream.getnchannels()
            self.sample_width = stream.getsampwidth()
            self.framerate = stream.getframerate()
            self.num_frames = stream.getnframes()
            self.compression_type = stream.getcompname()
            self._raw_signal = stream.readframes(self.num_frames)

    def get_audio_sample_time(self):
        """
        Gets the length of the audio sample.
        :return: Sample length, in seconds.
        """
        return self.num_frames / self.framerate

    def get_signal(self):
        """
        Gets the audio signal as an array.  For example, if the original .wav file is in stereo format,
        the returned array will consist of 2 numpy arrays (representing the left and right channels, respectively).
        :return: Array of numpy arrays, each consisting of the entire signal from one channel.
        """
        signal = np.frombuffer(self._raw_signal, dtype="int16")
        return list(signal[ch::self.num_channels] for ch in range(self.num_channels))
