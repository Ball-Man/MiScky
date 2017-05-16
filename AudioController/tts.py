import requests

api_url = 'http://api.voicerss.org'
api_key = '00a395df0b7f48efae665eac2fb49fc9'
lang = 'it-it'
codec = 'WAV'
format = '16khz_16bit_mono'
path = 'output'

def tts(text, getpath):
	params = {'key': api_key, 'hl': lang, 'src': text, 'c':codec, 'f':format}
	r = requests.get(api_url, params=params)
	if(getpath):
		with open(path+'.'+codec, 'wb') as fd:
			for chunk in r.iter_content(chunk_size=128):
				fd.write(chunk)
		return path+'.'+codec
	return r.content
	
