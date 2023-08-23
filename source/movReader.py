from moviepy.editor import VideoFileClip
import os


def extract_audio(filepath):
    filename, _ = os.path.splitext(os.path.basename(filepath))
    directory = os.path.dirname(filepath)
    wav_filepath = os.path.join(directory, filename + ".wav")

    video = VideoFileClip(filepath)
    video.audio.write_audiofile(wav_filepath)
