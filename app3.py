import speech_recognition as sr
import webbrowser

sr.Microphone(device_index=1)
r=sr.Recognizer()

with sr.Microphone() as source:
	print("What do you want to search for?")
	audio=r.listen(source)
	try:
		text=r.recognize_google(audio)
		print("Searching for:".format(text))
		url='https://www.google.com/search?source=hp&ei=gBJ9XfWFFKfaz7sPwsaj8AE&q='
		search_url=url+text
		webbrowser.open(search_url)
		
	except:
		print("Sorry!What did you say?")