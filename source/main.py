import movReader
from movReader import MOV_EXTENSION
from test import transcribe
import os
from waveform import Waveform
import matplotlib.pyplot as plt
import numpy as np


def main():
    print("Enter *.mov filename, without the extension: ")
    mov_filename = input() + MOV_EXTENSION
    wav_filepath = movReader.extract_audio(os.path.join(os.path.curdir, mov_filename))
    waveform = Waveform(wav_filepath)
    print("Filepath: ", waveform.filepath)
    print("Number of channels: ", waveform.num_channels)
    print("Sample width: ", waveform.sample_width)
    print("Sampling frequency (Hz): ", waveform.framerate)
    print("Number of frames: ", waveform.num_frames)
    print("Time (s): ", waveform.get_audio_sample_time())
    print("Compression type: ", waveform.compression_type)

    for signal in waveform.get_signal():
        time = len(signal) / waveform.framerate
        plt.plot(np.linspace(0, time, num=len(signal)), signal)

    plt.show()

    # TODO: average the 2 channels
    #text = transcribe(waveform._raw_signal, waveform.framerate)
    left, right = waveform.get_raw_signals()
    text = transcribe(right, waveform.framerate)
    print(text)


if __name__ == '__main__':
    main()
