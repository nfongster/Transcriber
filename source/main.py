import movReader
from movReader import MOV_EXTENSION
import os
from waveform import Waveform


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


if __name__ == '__main__':
    main()
