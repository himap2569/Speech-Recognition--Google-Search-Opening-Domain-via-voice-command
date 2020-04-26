import speech_recognition as sr
import webbrowser
r=sr.Recognizer()

with sr.Microphone() as source:
	print("what do you want to search?")
	audio = r.listen(source)

print('opening:' + r.recognize_google(audio))

p= r.recognize_google(audio)
webbrowser.open(p)
