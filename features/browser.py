import webbrowser
import pywhatkit
import pyautogui
from pywikihow import search_wikihow
import wikipedia

def play_on_youtube(query):
    pywhatkit.playonyt(query)
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter') 
    return True  

def sites(data):
    webbrowser.open(f'www.{data}.com')
    return True

def google_search(query):
    pywhatkit.search(query)
    wikipedia.summary(query,2)
    return True

def how_to(query):
    max_results=1
    how_to_func=search_wikihow(query=query,max_results=max_results)
    assert len(how_to_func) == 1
    how_to_func[0]
    result=how_to_func[0].summary
    return result
