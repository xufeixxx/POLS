function min_dis_id = pl_disturb(poi_id,epsilon,poi)

    p_lon = poi(poi_id,1);
    p_lat = poi(poi_id,2);
    [newlon, newlat] = newLatLon_Epsilon(epsilon, p_lon, p_lat);
    min_dis = realmax('double');
    min_dis_id = 0;
    if (epsilon == 0.004) || (epsilon == 0.005) || (epsilon == 0.007)
        add_id = 10000;
    else 
        add_id = 5000;
    end
    for i = 1:add_id
        if poi_id-i >= 1
            dis = dis_bet_latlon(newlon,newlat,poi(poi_id-i,1),poi(poi_id-i,2));
            if dis < min_dis
                min_dis = dis;
                min_dis_id = poi_id-i;
            end
        end
        if poi_id+i<=87635
            dis = dis_bet_latlon(newlon,newlat,poi(poi_id+i,1),poi(poi_id+i,2));
            if dis < min_dis
                min_dis = dis;
                min_dis_id = poi_id+i;
            end
        end
    end
        

end

