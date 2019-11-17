import requests
import json
import webbrowser


def coordinates(nomad_id: int) -> tuple:
    print(f'NOMAD id: {nomad_id}')
    # Gets the JSON, 25544 - the ISS(МКС) coordinates
    request = requests.get(f'https://api.wheretheiss.at/v1/satellites/{nomad_id}')

    # Converting request to the default python dict
    request = json.loads(request.text)

    # Get geopositioning for ISS coordinates
    # Latitude and Longitude here
    latitude, longitude = request['latitude'], request['longitude']

    print(latitude, longitude)
    return latitude, longitude


def open_browser_map(latitude: float, longitude: float) -> None:
    url = f'https://www.google.com/maps/@{latitude},{longitude},4.75z'
    webbrowser.open(url)


if __name__ == '__main__':
    latitude, longitude = coordinates()
    open_browser_map(latitude, longitude)
