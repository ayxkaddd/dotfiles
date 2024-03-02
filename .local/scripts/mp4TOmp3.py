#!/usr/bin/python3
import sys
from moviepy.editor import VideoFileClip

def convert_video_to_audio(input_file, output_file):
    video_clip = VideoFileClip(input_file)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_file)

# Example usage:
input_file = sys.argv[1] 
output_file = sys.argv[-1]
convert_video_to_audio(input_file, output_file)

