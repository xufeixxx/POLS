function dis_id = geo_disturb(poi_id,epsilon,poi)

    N_loc = 87635;
    dis_mat = zeros(1,N_loc);
    for i = 1:N_loc
        if i ~= poi_id
            dis = dis_bet_latlon(poi(poi_id,1),poi(poi_id,2),poi(i,1),poi(i,2));
            dis_mat(i) = exp(-epsilon*dis);
        end
    end
    dis_mat = dis_mat/sum(dis_mat);
    dis_id = randsrc(1,1,[1:N_loc;dis_mat]);
            
   
end

