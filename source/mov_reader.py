from moviepy.editor import VideoFileClip
import os

MOV_EXTENSION = ".mov"
WAV_EXTENSION = ".wav"


def extract_audio(filepath):
    filename, _ = os.path.splitext(os.path.basename(filepath))
    directory = os.path.dirname(filepath)
    wav_filepath = os.path.join(directory, filename + WAV_EXTENSION)

    video = VideoFileClip(filepath)
    video.audio.write_audiofile(wav_filepath)
    return wav_filepath
