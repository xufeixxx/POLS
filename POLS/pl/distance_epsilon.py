from pl.planarLaplace import addNoise, distance


def distanceOfEpsilon(epsilon):
    latitude = 0.0
    longitude = 0.0
    total_dis = 0
    for i in range(10000):
        long, lati = addNoise(epsilon, longitude, latitude)
        total_dis += distance(longitude, latitude, long, lati)

    return total_dis / 10000


d = distanceOfEpsilon(0.001)
print(d)
