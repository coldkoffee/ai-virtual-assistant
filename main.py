import sys
sys.path.append("..")
sys.path.append("tts/")
sys.path.append("intent_classification/")
sys.path.append("features/")
sys.path.append("stt/")


from stt import whisper_stt
from tts import speak
from intent_classification import model,alan,nltk_utils
from features import system,api,greet,browser
from playsound import playsound

query=whisper_stt.transcribe()
Query=whisper_stt.transcribed_text(query)
Query=str(Query).lower()
keyword=alan.keyword_extract(Query)
if keyword=='news':
    returned=api.news(Query)
    print(returned)
elif keyword=='create_file':
    system.create_files(Query)
elif keyword=='camera':
    system.take_picture()
elif keyword=='delete_file':
    system.delete_files(Query)
elif keyword=='create_directory':
    system.create_directories(Query)
elif keyword=='delete_directory':
    system.delete_directories(Query)
elif keyword=='note':
    system.take_note(Query)
elif keyword=='read_note':
    system.read_note()
elif keyword=='restart':
    system.restart()
elif keyword=='shutdown':
    system.shutdown()
elif keyword=='close':
    system.close_application(Query)
else:
    speak.speak(keyword)
    playsound('test.wav')
