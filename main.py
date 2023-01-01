import math


# calculate radian measure
def toRadians(degrees):
    return degrees * math.pi / 180


# calculate distance
def gpsDistance(lat1, lon1, lat2, lon2):
    R = 6371
    dLat = toRadians(lat2 - lat1)
    dLon = toRadians(lon2 - lon1)
    lat1 = toRadians(lat1)
    lat2 = toRadians(lat2)
    a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.sin(dLon / 2) * math.sin(dLon / 2) * math.cos(lat1) * math.cos(
        lat2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = R * c
    return d


# main ------------------------------------------------

# Koeln Dom
kdLat = 50.94157
kdLon = 6.95821

# Düsseldorf Airport
ftLat = 51.21795
ftLon = 6.76165

print('The Disctance between Koeln Dom and Düsseldorf Airport is: ' + str(gpsDistance(kdLat, kdLon, ftLat, ftLon)) + 'km')
