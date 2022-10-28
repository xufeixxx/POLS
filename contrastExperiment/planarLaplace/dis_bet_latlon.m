function distance = dis_bet_latlon(lon1,lat1,lon2,lat2)
earth_radius = 6378137; % meters

% def distance(lon1, lat1, lon2, lat2):
%     delta_lon = rad_of_deg(lon2 - lon1)
%     delta_lat = rad_of_deg(lat2 - lat1)
% 
%     a = np.sin(delta_lat / 2) * np.sin(delta_lat / 2) + np.cos(rad_of_deg(lat1)) * np.cos(rad_of_deg(lat2)) * np.sin(
%         delta_lon / 2) * np.sin(delta_lon / 2)
%     c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
% 
%     return earth_radius * c

delta_lon = rad_of_deg(lon2 - lon1);
delta_lat = rad_of_deg(lat2 - lat1);
a = sin(delta_lat/2)^2 + cos(rad_of_deg(lat1))*cos(rad_of_deg(lat2))*sin(delta_lon/2)^2;
c = 2*atan2(sqrt(a),sqrt(1-a));
distance = earth_radius*c;

end

