# -*- coding: utf-8 -*-
"""youtube transcript summarizer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Kx8M4Gx1Ll_7v7WXJxu4YigGzqjS1MJu
"""

!pip install -q transformers

!pip install -q youtube_transcript_api

from transformers import pipeline 
from youtube_transcript_api import YouTubeTranscriptApi

youtube_video = "https://www.youtube.com/watch?v=aOL7wzEIZSc"

video_id = youtube_video.split("=")[1]

from IPython.display import YouTubeVideo
YouTubeVideo(video_id)

YouTubeTranscriptApi.get_transcript(video_id)
transcript = YouTubeTranscriptApi.get_transcript(video_id)

transcript[0:5]

YouTubeTranscriptApi.get_transcript(video_id)

result = " "
for i in transcript:
    result += ' ' + i['text']
#print(result)
print(len(result))

summarizer = pipeline('summarization')

num_iters = int(len(result)/1000)
summarized_text = [] 
for i in range(0, num_iters + 1):
  start = 0
  start = i * 1000
  end = (i + 1) * 1000
  out = summarizer(result[start:end])
  out = out[0]
  out = out['summary_text']
  summarized_text.append(out)

print(summarized_text)

len(str(summarized_text))

str(summarized_text)