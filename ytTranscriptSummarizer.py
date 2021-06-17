import requests
import rx
import json
from rx import operators as ops

from transformers import pipeline

from youtube_transcript_api import YouTubeTranscriptApi

import PySimpleGUI as sg

################# GUI #################

#layout = [[sg.Multiline(size=(30, 10), #reroute_stdout=True, echo_stdout_stderr=True)],
         # [sg.MLine(size=(30, 5), key='-MLINE IN-', enter_submits=True, do_not_clear=False),
          # sg.Button('SEND', bind_return_key=True), sg.Button('EXIT')]]

#window = sg.Window('Chat Window', layout,
            #default_element_size=(10, 2))

# ---===--- Loop taking in user input and using it to query HowDoI web oracle --- #
#while True:
    #event, values = window.read()
    #if event != 'SEND':
        #break
    #string = values['-MLINE IN-'].rstrip()
    #print('  ' + string)
    # send the user input to chatbot to get a response
    
vID = input('Enter Video Id:')    
    

# retrieve the available transcripts
transcript_list = YouTubeTranscriptApi.list_transcripts(vID)

# iterate over all available transcripts
for transcript in transcript_list:
  y = (transcript.fetch())

source = rx.from_(y)
case1 = source.pipe(
   ops.map(lambda c: c["text"]),
   ops.reduce(lambda accumulator,x: accumulator+x+" "))

summarization = pipeline("summarization")
print("Transcript Follows:")   
case1.subscribe(
   on_next = lambda i: print("{0}".format(i)),  
   on_error = lambda e: print("Error : {0}".format(e)),
   on_completed = lambda: print("Job Done!"),
) 

case2 = case1.pipe(
  #ops.map(lambda s:[s[i:i+512] for i in range(0, len(s), int(len(s)/512))] ),
  ops.map(lambda q: summarization(q, max_length = 512))
)

case2.subscribe(
   on_next = lambda i: print("{0}".format(i)),  
   on_error = lambda e: print("Error : {0}".format(e)),
   on_completed = lambda: print("Job Done!"),
) 





