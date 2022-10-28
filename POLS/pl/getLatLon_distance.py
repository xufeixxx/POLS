# Formula:
# φ2 = asin( sin φ1 ⋅ cos δ + cos φ1 ⋅ sin δ ⋅ cos θ )
# λ2 = λ1 + atan2( sin θ ⋅ sin δ ⋅ cos φ1, cos δ − sin φ1 ⋅ sin φ2 )
# where	φ is latitude, λ is longitude, θ is the bearing (clockwise from north), δ is the angular distance d/R; d being the distance travelled, R the earth’s radius

import numpy as np
from pl.planarLaplace import distance, rad_of_deg, deg_of_rad

earth_radius = 6378137


def getLatLon_dis(longitude, latitude, dis):
    latitude2 = np.arcsin(
        np.sin(rad_of_deg(latitude)) * np.cos(dis / earth_radius) + np.cos(rad_of_deg(latitude)) * np.sin(
            dis / earth_radius) * np.cos(np.pi / 2))
    longitude2 = rad_of_deg(longitude) + np.arctan2(
        np.sin(np.pi / 2) * np.sin(dis / earth_radius) * np.cos(rad_of_deg(latitude)),
        np.cos(dis / earth_radius) - np.sin(rad_of_deg(latitude)) * np.sin(
            latitude2))
    new_long2 = deg_of_rad(longitude2)
    # new_lati2 = deg_of_rad(latitude2)
    latitude3 = np.arcsin(
        np.sin(rad_of_deg(latitude)) * np.cos(dis / earth_radius) + np.cos(rad_of_deg(latitude)) * np.sin(
            dis / earth_radius) * np.cos(0))
    # longitude3 = rad_of_deg(longitude) + np.arctan2(
    #     np.sin(0) * np.sin(dis / earth_radius) * np.cos(rad_of_deg(latitude)),
    #     np.cos(dis / earth_radius) - np.sin(rad_of_deg(latitude)) * np.sin(
    #         latitude2))
    new_lati3 = deg_of_rad(latitude3)
    return new_long2, new_lati3


def getLatLon_theta(longitude, latitude, dis, theta):
    latitude2 = np.arcsin(
        np.sin(rad_of_deg(latitude)) * np.cos(dis / earth_radius) + np.cos(rad_of_deg(latitude)) * np.sin(
            dis / earth_radius) * np.cos(theta))
    longitude2 = rad_of_deg(longitude) + np.arctan2(
        np.sin(theta) * np.sin(dis / earth_radius) * np.cos(rad_of_deg(latitude)),
        np.cos(dis / earth_radius) - np.sin(rad_of_deg(latitude)) * np.sin(
            latitude2))
    return deg_of_rad(longitude2), deg_of_rad(latitude2)


def square_LatLon(longitude, latitude, dis):
    reLon1,lat1 = getLatLon_theta(longitude,latitude,dis,np.pi*3/2)
    reLon2,lat2 = getLatLon_theta(longitude,latitude,dis,np.pi/2)

    lon1,reLat1 = getLatLon_theta(longitude,latitude,dis,np.pi)
    lon2,reLat2 = getLatLon_theta(longitude,latitude,dis,0)
    # lon_pi, lat_pi = getLatLon_theta(longitude, latitude, dis, np.pi)
    # reLon2, lat1 = getLatLon_theta(lon_pi, lat_pi, dis, np.pi / 2)
    # reLon1, lat2 = getLatLon_theta(lon_pi, lat_pi, dis, np.pi * 3 / 2)
    #
    # lon_32pi, lat_32pi = getLatLon_theta(longitude, latitude, dis, np.pi * 3 / 2)
    # lon1, reLat1 = getLatLon_theta(lon_32pi, lat_32pi, dis, np.pi)
    # lon2, reLat2 = getLatLon_theta(lon_32pi, lat_32pi, dis, 0)

    return [reLon1, reLon2], [reLat1, reLat2]


[lon1, lon2], [lat1, lat2] = square_LatLon(0.0, 0.0, 110000)

longitude = 0.0
latitude = 0.0
theta = np.pi * 3 / 2
dis = 110000
latitude2 = np.arcsin(
    np.sin(rad_of_deg(latitude)) * np.cos(dis / earth_radius) + np.cos(rad_of_deg(latitude)) * np.sin(
        dis / earth_radius) * np.cos(theta))
longitude2 = rad_of_deg(longitude) + np.arctan2(
    np.sin(theta) * np.sin(dis / earth_radius) * np.cos(rad_of_deg(latitude)),
    np.cos(dis / earth_radius) - np.sin(rad_of_deg(latitude)) * np.sin(
        latitude2))
# lon, lat = getLatLon_dis(longitude, latitude, dis)
# d = distance(longitude, latitude, deg_of_rad(longitude2), deg_of_rad(latitude2))
deg_lon = deg_of_rad(longitude2)
deg_lat = deg_of_rad(latitude2)

print("end")
