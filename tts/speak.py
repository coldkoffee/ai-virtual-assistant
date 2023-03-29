from ovos_tts_plugin_mimic3_server import Mimic3ServerTTSPlugin
from playsound import playsound
tt = Mimic3ServerTTSPlugin()

def speak(out_text):
    tt.get_tts(out_text, "test.wav", lang="en-gb")
    

if __name__ == "__main__":
    speak("I didn't work with this library; but I think r.listen(source) is a blocking function (method). A blocking method is a method that blocks code from continuing execution until it is done (returned). Your app is waiting for r.listen(source) to finish. You should put print(Recognizing...) before it. Also as I read here, r.listen(source) will return result (finish) when it detects silence (probably after a voice). So your code should continue execution after it detects silence.")