function distance = dis_epsilon(longitude,latitude,epsilon)
total_dis = 0;
for i = 1:100000
    [long,lati] = newLatLon_Epsilon(epsilon, longitude, latitude);

    total_dis = total_dis + dis_bet_latlon(longitude,latitude,long,lati);
end
distance = total_dis/100000;
end

