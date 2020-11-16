import geopy.distance
from math import sin, cos, sqrt, atan2, radians

def translate_coordinates(x):
    return

def calculate_distance(x,y):
    """
    Calculates the distance between two gps coordinates
    X should be a list of [lon1, lat1]
    y should be a list of [lon2, lat2]
    """
    # return geopy.distance.vincenty(x, y).km

    R = 6370 # rad of earth

    lat1 = radians(x[0])  #insert value
    lon1 = radians(x[1])
    lat2 = radians(y[0])
    lon2 = radians(y[1])

    difflon = lon2 - lon1
    difflat = lat2- lat1

    a = sin(difflat / 2)**2 + cos(lat1) * cos(lat2) * sin(difflon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = R * c
    return distance
