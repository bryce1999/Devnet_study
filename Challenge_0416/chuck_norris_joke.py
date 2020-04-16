# Native imports
import os
import sys

# Third party imports
import requests

def request_joke() -> str:
    """Return a chuck norris joke as a string

    Requests a joke from api.chucknorris.io.
    """
    response = None

    try:
        response = requests.get("https://api.chucknorris.io/jokes/random")

    except requests.exceptions.ConnectionError as e:
        raise SystemExit(e)

    response.raise_for_status()

    # Get the response json as a python Dict
    json_data = response.json()

    return json_data['value']


