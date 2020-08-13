import time
import requests

def st():
	r = requests.get("https://example.com")
	return r.status_code

def img_download(url):
	# http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg
	# data_folder = '/home/vishalchopra/Desktop/CA helper bot/public/'
	file_id = wget.download(url)
	print("***\n")
	print(file_id)
	return file_id