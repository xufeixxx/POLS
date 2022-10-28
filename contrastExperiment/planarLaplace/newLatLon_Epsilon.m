function [newlon, newlat] = newLatLon_Epsilon(epsilon, longitude, latitude)

earth_radius = 6378137; % meters

angle = 2*pi*rand;
x = (rand-1)/exp(1);
    
r = -(LambertW(x)+1)/epsilon;

any_distance = r/earth_radius;
lat1 = rad_of_deg(latitude);
lon1 = rad_of_deg(longitude);
lat2 = asin(sin(lat1)*cos(any_distance)+cos(lat1)*sin(any_distance)*cos(angle));
lon2 = lon1 + atan2(sin(angle)*sin(any_distance)*cos(lat1),cos(any_distance)-sin(lat1)*sin(lat2));
lon2 = mod((lon2+3*pi),(2*pi))-pi;

newlat = deg_of_rad(lat2);
newlon = deg_of_rad(lon2);

end

