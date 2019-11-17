import requests
import json
import webbrowser
from src.Classes import Pass

API_KEY = 'QRGLJV-JCPRUX-7ZLNAR-48LW'


def coordinates(norad_id: int) -> tuple:
    '''
    :param norad_id: norad id of Station
    :return: latitude, longitude: tuple of station coordinates
    '''

    print(f'NOMAD id: {norad_id}')

    # Gets the JSON, 25544 - the ISS(МКС) coordinates
    request = requests.get(f'https://api.wheretheiss.at/v1/satellites/{norad_id}')

    # Converting request to the default python dict
    request = json.loads(request.text)

    # Get geopositioning for ISS coordinates
    # Latitude and Longitude here
    latitude, longitude = request['latitude'], request['longitude']

    return latitude, longitude


def open_browser_map(latitude: float, longitude: float) -> None:
    '''
    Opens google maps in the browser by coordinates
    :param latitude: latitude
    :param longitude: longitude
    :return: None
    '''

    url = f'https://www.google.com/maps/@{latitude},{longitude},4.75z'
    webbrowser.open(url)


def visual_passes(api_key: str, norad_id: int, obs_lat: float, obs_lng: float, obs_alt: float, days: int,
                  min_visibility: int) -> list:
    '''
    Get predicted visual passes for any satellite relative to a location on Earth

    :param api_key: API_KEY to get  access to the data
    :param norad_id: NORAD id of current object(space station)
    :param obs_lat: Observer's latitide (decimal degrees format)
    :param obs_lng: Observer's longitude (decimal degrees format)
    :param obs_alt: Observer's altitude above sea level in meters
    :param days: Number of days of prediction (max 10)
    :param min_visibility: Minimum number of seconds the satellite should be considered optically visible during the pass to be returned as result

    Request: /visualpasses/{id}/{observer_lat}/{observer_lng}/{observer_alt}/{days}/{min_visibility}
    example of request: http://www.n2yo.com/rest/v1/satellite/visualpasses/25544/41.702/-76.014/0/2/300/&apiKey=589P8Q-SDRYX8-L842ZD-5Z9

    :return: list of Pass objects
    '''

    url = f'http://www.n2yo.com/rest/v1/satellite/visualpasses/{norad_id}/{obs_lat}/{obs_lng}/{obs_alt}/{days}/{min_visibility}/&apiKey={api_key}'

    # Get the JSON by request
    request = requests.get(url)
    request = json.loads(request.text)

    # Assign pass count to passes
    passes = request['info']['passescount']
    # List of returns objects
    passes_list = list()

    # Checking passes more than 0
    if passes > 0:
        # If there is more than 0 passes

        passes = request['passes']
        for i in passes:
            # print(i)
            passing = Pass(i['startAz'], i['startAzCompass'], i['startUTC'], i['maxAz'], i['maxAzCompass'],
                           i['maxUTC'], i['endAz'], i['endAzCompass'], i['endUTC'], i['mag'], i['duration'])
            passes_list.append(passing)
    else:
        passes_list.append(None)

    return passes_list


if __name__ == '__main__':
    object = visual_passes(API_KEY, 25544, 37.953757, 58.336792, 129, 10, 300)
    print(object[0])
