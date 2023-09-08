import movReader
from movReader import MOV_EXTENSION, WAV_EXTENSION
from transcriber import transcribe
import os
from waveform import Waveform
import matplotlib.pyplot as plt
import numpy as np
import wave
import json
from collections import deque


def main():
    print("Enter *.mov filename, without the extension: ")
    mov_filename = input() + MOV_EXTENSION
    wav_filepath = movReader.extract_audio(os.path.join(os.path.curdir, mov_filename))

    # print("Enter *.wav filename, without the extension: ")
    # wav_filename = input() + WAV_EXTENSION
    # wav_filepath = os.path.join(os.path.curdir, wav_filename)

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

    left, right = waveform.get_raw_signals()
    result = transcribe(right, waveform.framerate)  # TODO: average the 2 channels
    json_result = json.loads(result)
    for text in json_result.values():
        print(text)

    words_per_line = 5

    with open("result.txt", 'w') as file:
        for text in json_result.values():
            text = deque(text.split(' '))
            while len(text) >= words_per_line:
                for i in range(words_per_line):
                    file.write(text.popleft() + ' ')
                file.writelines('\n')

            for word in text:
                file.write(word + ' ')

    # with wave.open('combined_single_channel.wav', 'wb') as wav_file:
    #     wav_file.setnchannels(1)
    #     wav_file.setsampwidth(waveform.sample_width)
    #     wav_file.setframerate(waveform.framerate)
    #     wav_file.setnframes(waveform.num_frames)
    #     wav_file.writeframes(left)


if __name__ == '__main__':
    main()
