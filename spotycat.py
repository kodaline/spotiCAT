import requests
import base64

from cat.mad_hatter.decorators import tool, hook, plugin
from pydantic import BaseModel, Field
from .utils import get_spotify_token


class SpotifySettings(BaseModel):
    SPOTIFY_CLIENT_ID: str = Field(
        title="your spotify client id",
        description="The Spotify Client ID to connect to, check the plugin README.md for more info",
        default="",
        extra={"type": "Text"}
    )
    SPOTIFY_CLIENT_SECRET: str = Field(
        title="your spotify client secret",
        description="The Spotify Client Secret to connect to, check the plugin README.md for more info",
        default="",
        extra={"type": "Text"}
    )


@plugin
def settings_model():
    return SpotifySettings

@tool(return_direct=True)
def play_specific_song_request(tool_input, cat):
    """Use this tool to play a specific song asked by the User. Input is the song to be played."""
    scope = "user-read-playback-state,user-modify-playback-state"

    settings = cat.mad_hatter.get_plugin().load_settings()
    SPOTIFY_CLIENT_ID = settings["SPOTIFY_CLIENT_ID"]
    SPOTIFY_CLIENT_SECRET = settings["SPOTIFY_CLIENT_SECRET"]
    token = get_spotify_token(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)

    print(f'TOKEN IS \n {token}')
    return "ciao"
