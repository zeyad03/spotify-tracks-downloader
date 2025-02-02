from bs4 import BeautifulSoup
from requests_html import HTMLSession
from pathlib import Path
import yt_dlp
import pandas
import os

def DownloadVideosFromTitles(los):
	ids = []
	for index, item in enumerate(los):
		vid_id = ScrapeVidId(index, item)
		ids += [vid_id]
	print("Downloading songs")
	DownloadVideosFromIds(ids)

def DownloadVideosFromIds(lov):
	SAVE_PATH = str(os.path.join(Path.home(), "Downloads/songs"))
	try:
		os.mkdir(SAVE_PATH)
	except:
		print("download folder exists")
	ydl_opts = {
    	'format': 'bestaudio/best',
   		'postprocessors': [{
        		'key': 'FFmpegExtractAudio',
        		'preferredcodec': 'mp3',
        		'preferredquality': '192',
    		}],
		'outtmpl': SAVE_PATH + '/%(title)s.%(ext)s',
	}

	with yt_dlp.YoutubeDL(ydl_opts) as ydl:
	    ydl.download(lov)

def ScrapeVidId(idx, query):
	print (f"{idx+1}. Getting video id for: {query}")
	BASIC="http://www.youtube.com/results?search_query="
	URL = (BASIC + query)
	URL.replace(" ", "+")

	session = HTMLSession()
	response = session.get(URL)
	response.html.render(sleep=2, timeout=15, keep_page=True)
	soup = BeautifulSoup(response.html.html, "html.parser")

	results = soup.find('a', id="video-title")
	return results['href'].split('v=')[1].split("&")[0]

def __main__():

    data = pandas.read_csv('songs.csv')
    data = data['song names'].tolist()
    print("Found ", len(data), " songs!")
    DownloadVideosFromTitles(data)
	
__main__()