import mov_reader
from mov_reader import MOV_EXTENSION, WAV_EXTENSION
from transcriber import transcribe
import os
from waveform import Waveform
import matplotlib.pyplot as plt
import numpy as np
import json
from collections import deque


def main_script(source_file_path: str, output_dir: str, model_dir: str, channel: int):
    audio_filepath, audio_file_extension = os.path.splitext(source_file_path)
    wav_filepath = ""

    if str.lower(audio_file_extension) == MOV_EXTENSION:
        print(f"Reading MOV file at: {source_file_path}")
        wav_filepath = mov_reader.extract_audio(source_file_path)

    elif str.lower(audio_file_extension) == WAV_EXTENSION:
        print(f"Reading WAV file at: {source_file_path}")
        wav_filepath = source_file_path

    else:
        raise ValueError(f"File extension must be .wav or .mov, but was {audio_file_extension}."
                         f"\nFull path: {source_file_path}")

    waveform = Waveform(wav_filepath)
    print("Filepath: ", waveform.filepath)
    print("Number of channels: ", waveform.num_channels)
    print("Sample width: ", waveform.sample_width)
    print("Sampling frequency (Hz): ", waveform.framerate)
    print("Number of frames: ", waveform.num_frames)
    print("Time (s): ", waveform.get_audio_sample_time())
    print("Compression type: ", waveform.compression_type)

    # for signal in waveform.get_signal():
    #     time = len(signal) / waveform.framerate
    #     plt.plot(np.linspace(0, time, num=len(signal)), signal)
    # plt.show()

    channels = waveform.get_raw_signals()

    if len(channels) > 2 or len(channels) < 1:
        raise ValueError(f"Must be mono (1 channel) or stereo (2 channels) format, "
                         f"but audio signal contains {len(channels)} channels.")

    signal = channels[0]
    if len(channels) == 2 and channel == 1:
        signal = channels[1]

    result = transcribe(signal, waveform.framerate, model_dir)
    json_result = json.loads(result)
    for text in json_result.values():
        print(text)

    words_per_line = 5

    transcription_filename = f"{os.path.basename(audio_filepath)}__Transcription.txt"
    with open(os.path.join(os.path.normpath(output_dir), transcription_filename), 'w') as file:
        for text in json_result.values():
            text = deque(text.split(' '))
            while len(text) >= words_per_line:
                for i in range(words_per_line):
                    file.write(text.popleft() + ' ')
                file.writelines('\n')

            for word in text:
                file.write(word + ' ')
