from swaglyrics.cli import lyrics
import os

os.environ['SPOTIPY_CLIENT_ID'] = 'YOUR CLIENT ID'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'YOUR CLIENT SECRET'
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://localhost:8888/callback'

class Spotify:

    def __init__(self, curr_song, curr_pb_state):
        self.curr_song = curr_song
        self.curr_pb_state = curr_pb_state


    def getArtists(self):
        artist_info = []
        try:
            for artist in self.curr_song["item"]["artists"]:
                artist_info.append({"name": artist["name"], "id": artist["id"], "url": artist["external_urls"]["spotify"]})
        except:
            artist_info.append({"name": None, "id": None, "url": "#"})
        return artist_info

    def getSongName(self):
        try:
            return self.curr_song["item"]["name"]
        except:
            return None

    def getSongImage(self):
        try:
            for image in self.curr_song["item"]["album"]["images"]:
                if image["height"] == 640:
                    image_url = image["url"]
                    break
            return image_url
        except:
            return ""


    def getSongReleaseDate(self):
        try:
            return self.curr_song["item"]["album"]["release_date"]
        except:
            return None

    def getSongLink(self):
        try:
            return self.curr_song["item"]["album"]["external_urls"]["spotify"]
        except:
            return "#"

    def getShuffleState(self):
        try:
            return self.curr_pb_state["shuffle_state"]
        except:
            return None

    def getLyrics(self, song_name, artist):
        song_lyrics = lyrics(song_name, artist)
        return song_lyrics.split("\n")
