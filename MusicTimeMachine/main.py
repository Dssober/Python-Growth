import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

date_input = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")


CLIENT = "4b4fdaa705d44c72aa238d43047b60ce"
SECERET = "4170c253fb3e42d484b2c7611d085424"
URL = f"https://www.billboard.com/charts/hot-100/{date_input}/"


# Make soup of billboard top 100
response = requests.get(URL)
top_100 = response.text

soup = BeautifulSoup(top_100, "html.parser")

song_names_list = soup.select(selector="li h3", class_="c-title")
song_names = [song.getText().strip() for song in song_names_list]

# print(song_names)

# Spotify access
SPOTIPY_CLIENT_ID = CLIENT
SPOTIPY_CLIENT_SECRET = SECERET
SPOTIPY_REDIRECT_URI = "http://localhost:8888/callback"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="user-library-read playlist-modify-private",
redirect_uri=SPOTIPY_REDIRECT_URI,
client_id=SPOTIPY_CLIENT_ID,
client_secret=SPOTIPY_CLIENT_SECRET,
show_dialog=False,
cache_path="token.txt"))

results = sp.current_user()

formatted_results = json.dumps(results, indent=4)
with open("results.json", mode="w") as file:
    file.write(formatted_results)

user_id = results["id"]

# print(user_id)

# Build Playlist

year = date_input.split("-")[0]

playlist_uris = []
for song in song_names:
    results = sp.search(q=f"track:{song} year:{year}", type="track")

    try:
        uri = results["tracks"]["items"][0]["uri"]
        playlist_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify, Skipped!")
#print(playlist_uris)

# Build Playlist

    playlist = sp.user_playlist_create(user=user_id, name=f"{date_input} Billboard 100", public=False)
    print(playlist)

    sp.playlist_add_items(playlist_id=playlist["id"], items=playlist_uris)

print(f"\nThe playlist has been created. A total of {len(playlist_uris)}/100 of the top 100 songs were found!")


















