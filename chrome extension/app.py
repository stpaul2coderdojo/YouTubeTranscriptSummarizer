from flask import Flask
from datetime
import requests
import rx
import json
from rx import operators as ops

from transformers import pipeline

# define a variable to hold you app
app = Flask(__name__)

# define your resource endpoints
app.route('/')
def index_page():
    return "Hello world"

app.route('/time', methods=['GET'])
def get_time():
    return str(datetime.datetime.now())

# server the app when this file is run
if __name__ == '__main__':
    app.run()

def getTranscript(VideoId vId):
  transcript_list = YouTubeTranscriptApi.list_transcripts(vId)
  for transcript in transcript_list:
  y = (transcript.fetch())

source = rx.from_(y)
case1 = source.pipe(
   ops.map(lambda c: c["text"]),
   ops.reduce(lambda accumulator,x: accumulator+x))

return case1


def summarizer(string s):
  summarization = pipeline("summarization")
  summary_text = summarization(s)[0]['summary_text']
  return summary_text

