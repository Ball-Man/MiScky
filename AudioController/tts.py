import requests

api_url = 'http://api.voicerss.org'
api_key = '00a395df0b7f48efae665eac2fb49fc9'
lang = 'it-it'

def tts(text):
	params = {'key': api_key, 'hl': lang, 'src': text}
	r = requests.get(api_url, params=params)
	with open('output.mp3', 'wb') as fd:
		for chunk in r.iter_content(chunk_size=128):
			fd.write(chunk)
