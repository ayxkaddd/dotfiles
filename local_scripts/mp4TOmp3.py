#!/usr/bin/python3

from moviepy.editor import VideoFileClip

def convert_video_to_audio(input_file, output_file):
    video_clip = VideoFileClip(input_file)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_file)

# Example usage:
input_file = "chatgpt-draingang.mkv"
output_file = "dgbestsong.mp3"
convert_video_to_audio(input_file, output_file)

