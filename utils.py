import requests
import base64


def get_spotify_token(SPOTIFY_CLIENT_ID: str, SPOTIFY_CLIENT_SECRET: str):
    auth_str = f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}"
    base64_auth_str = base64.b64encode(auth_str.encode()).decode()

    auth_options = {
        "url": "https://accounts.spotify.com/api/token",
        "headers": {
            "Authorization": f"Basic {base64_auth_str}"
        },
        "data": {
            "grant_type": "client_credentials"
        }
    }

    response = requests.post(**auth_options)
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        return "ERROR DURING TOKEN REQUEST" # TODO better errors


def search_spotify_song(search: str, token: str):
    auth_options = {
        "url": "https://api.spotify.com/v1/me/shows?offset=0&limit=1",
        "headers": {
            "Authorization": token
        },
        "data": {
            "grant_type": "client_credentials"
        }
    }