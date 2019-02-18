import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl
import folium
from geopy.geocoders import Nominatim

def friends_finder(acct):
    """
    """
    # https://apps.twitter.com/
    # Create App and get the four strings, put them in hidden.py

    TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE


    screen_name = list()
    locations = list()
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '5'})
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    js = json.loads(data)
    for u in js['users']:
         screen_name.append((u['screen_name']))
         locations.append((u['location']))
    return (locations, screen_name)

def map_creator(tupl):
    """
    """
    map = folium.Map()
    geolocator = Nominatim(user_agent="Map")
    friends = folium.FeatureGroup(name='Location')
    for i in range(len(tupl[0])):
        location = geolocator.geocode(tupl[0][i])
        if location == None:
            continue
        else:
            friends.add_child(folium.Marker(location=[location.latitude, location.longitude],
                                            popup=tupl[1][i],
                                            icon=folium.Icon()))
    map.add_child(friends)
    map.save('templates/films.html')
