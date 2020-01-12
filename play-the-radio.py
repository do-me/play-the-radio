import speech_recognition as sr
from selenium import webdriver

r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    audio = r.listen(source)
phrase = r.recognize_google(audio)

if phrase == "play the radio":
    print(phrase)
    browser = webdriver.Chrome(executable_path="C:/.../chromedriver.exe") 
    browser.get("https://srv.deutschlandradio.de/themes/dradio/script/aod/index.html?audioMode=2&audioID=4&state=")
    browser.find_element_by_xpath('//*[@class="mkdraod-audio-play"]').click()
