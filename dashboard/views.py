from django.shortcuts import render
from django.http import HttpResponse
from .spotify import Spotify
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

scope = "user-read-currently-playing user-modify-playback-state user-read-playback-state"

username = os.getlogin()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, username=username))

def index(request):


    curr_song = sp.current_user_playing_track()
    curr_pb_state = sp.current_playback()
    spotify = Spotify(curr_song, curr_pb_state)
    song_name = spotify.getSongName()
    song_url = spotify.getSongLink()
    artists = spotify.getArtists()
    shuffle_state = spotify.getShuffleState()
    song_img = spotify.getSongImage()
    lyrics = spotify.getLyrics(song_name, artists[0]["name"])

    info = {}
    info["title"] = song_name
    info["song"] = {}
    info["song"]["name"] = song_name
    info["song"]["url"] = song_url
    info["song"]["artists"] = artists
    info["shuffle_state"] = shuffle_state
    info["song"]["image"] = song_img
    info["song"]["lyrics"] = lyrics


    # return HttpResponse("<h1>%s</h1><p>%s</p>" % (title, cal))
    return render(request, 'dashboard/home.html', info)

def pause(request):
    curr_pb_state = sp.current_playback()
    if curr_pb_state["is_playing"]:
        sp.pause_playback()
    else:
        sp.start_playback()

    return HttpResponse("")