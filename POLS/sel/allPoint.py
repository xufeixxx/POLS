import numpy as np
from pl.planarLaplace import distance
from pl.getLatLon_distance import square_LatLon


def all_point_distance(poi_id, dist, poi):
    # add_id = int(dist / 2)
    add_id = 3000
    p_matrix = np.array([], dtype=np.int32)
    u_lon = poi[poi_id, 0]
    u_lat = poi[poi_id, 1]
    [lon1, lon2], [lat1, lat2] = square_LatLon(u_lon, u_lat, dist)
    for i in range(1, add_id + 1):
        if poi_id - i >= 0:
            if lon1 <= poi[poi_id - i, 0] <= lon2 and lat1 <= poi[poi_id - i, 1] <= lat2:
                d1 = distance(u_lon, u_lat, poi[poi_id - i, 0], poi[poi_id - i, 1])
                if d1 <= dist:
                    p_matrix = np.append(p_matrix, poi_id - i)
        if poi_id + i < 87635:
            if lon1 <= poi[poi_id + i, 0] <= lon2 and lat1 <= poi[poi_id + i, 1] <= lat2:
                d2 = distance(u_lon, u_lat, poi[poi_id + i, 0], poi[poi_id + i, 1])
                if d2 <= dist:
                    p_matrix = np.append(p_matrix, poi_id + i)
        # if poi_id - i >= 0:
        #     if lon1 <= poi[poi_id - i, 0] <= lon2 and lat1 <= poi[poi_id - i, 1] <= lat2:
        #         p_matrix = np.append(p_matrix, poi_id - i)
        # if poi_id + i < 87635:
        #     if lon1 <= poi[poi_id + i, 0] <= lon2 and lat1 <= poi[poi_id + i, 1] <= lat2:
        #         p_matrix = np.append(p_matrix, poi_id + i)

    return p_matrix


def all_point_distance2(poi_id, dist, poi):
    p_matrix = np.array([], dtype=np.int32)
    u_lon = poi[poi_id, 0]
    u_lat = poi[poi_id, 1]

    for i in range(poi.shape[0]):
        d = distance(u_lon, u_lat, poi[i, 0], poi[i, 1])
        if 0 < d <= dist:
            p_matrix = np.append(p_matrix, i)
    return p_matrix
