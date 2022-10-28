function kk = score(epsilon, id1, id2, poi)

    dis = dis_bet_latlon(poi(id1,1),poi(id1,2),poi(id2,1),poi(id2,2));
    kk = exp(-0.5*epsilon*dis);

end

