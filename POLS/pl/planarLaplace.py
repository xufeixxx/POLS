import numpy as np

earth_radius = 6378137


def rad_of_deg(ang):
    return ang * np.pi / 180


def deg_of_rad(ang):
    return ang * 180 / np.pi


def getCartesian(longitude, latitude):
    x = earth_radius * rad_of_deg(longitude)
    y = earth_radius * np.log(np.tan(np.pi / 4 + rad_of_deg(latitude) / 2))

    return x, y


def lambertW(x):
    min_diff = 1e-10
    if x == -1 / np.e:
        return -1
    elif 0 > x > -1 / np.e:
        q = np.log(-x)
        p = 1
        while np.abs(p - q) > min_diff:
            p = (q * q + x / np.exp(q)) / (q + 1)
            q = (p * p + x / np.exp(p)) / (p + 1)

        return np.round(1000000 * q) / 1000000
    elif x == 0:
        return 0
    else:
        return 0


def inverseCumulativeGamma(epsilon, z):
    x = (z - 1) / np.e
    return -(lambertW(x) + 1) / epsilon


def addVectorToPos(longitude, latitude, distance, angle):
    ang_distance = distance / earth_radius
    lat1 = rad_of_deg(latitude)
    lon1 = rad_of_deg(longitude)

    lat2 = np.arcsin(np.sin(lat1) * np.cos(ang_distance) + np.cos(lat1) * np.sin(ang_distance) * np.cos(angle))
    lon2 = lon1 + np.arctan2(np.sin(angle) * np.sin(ang_distance) * np.cos(lat1),
                             np.cos(ang_distance) - np.sin(lat1) * np.sin(lat2))

    lon2 = (lon2 + 3 * np.pi) % (2 * np.pi) - np.pi
    long = deg_of_rad(lon2)
    lati = deg_of_rad(lat2)

    return long, lati


def addPolarNoise(epsilon, longitude, latitude):
    theta = np.random.uniform(0, np.pi * 2)
    z = np.random.random()
    r = inverseCumulativeGamma(epsilon, z)
    return addVectorToPos(longitude, latitude, r, theta)


def addNoise(epsilon, longitude, latitude):
    return addPolarNoise(epsilon, longitude, latitude)


def distance(lon1, lat1, lon2, lat2):
    delta_lon = rad_of_deg(lon2 - lon1)
    delta_lat = rad_of_deg(lat2 - lat1)

    a = np.sin(delta_lat / 2) * np.sin(delta_lat / 2) + np.cos(rad_of_deg(lat1)) * np.cos(rad_of_deg(lat2)) * np.sin(
        delta_lon / 2) * np.sin(delta_lon / 2)
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

    return earth_radius * c


print(distance(-1.243890963751346e+02, 32.541304760745156, -114.294416039413, 32.5413047607452))
print(distance(-1.243890963751346e+02, 32.541304760745156,-124.389096375135,42.0153233511193))