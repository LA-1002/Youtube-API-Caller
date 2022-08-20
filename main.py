import requests
import os

type = 'playlists';
key = os.environ['YTAPI']
playlist = '' #PUT PLAYLIST ID HErE
part = 'contentDetails'



def getPlaylistNumber():
    url = ('https://youtube.googleapis.com/youtube/v3/playlistItems?key=%s&playlistId=%s&part=%s'%(key,playlist,part))
    req = requests.get(url);
    results = req.json()['pageInfo']['totalResults']
    print(results);

def playListIDs():
    url = ('https://youtube.googleapis.com/youtube/v3/playlistItems?key=%s&playlistId=%s&part=%s&maxResults=50'%(key,playlist,part));
    req = requests.get(url);
    items = req.json()['items']
    file = open('Video_URLs.txt','a')
    for i in items:
        id = (i['contentDetails']['videoId'])
        file.write(('https://www.youtube.com/watch?v=%s \n\n'%id));
    file.close();


playListIDs()




