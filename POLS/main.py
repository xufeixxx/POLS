from load_mat import load_matrix
import numpy as np
from pl.distance_epsilon import distanceOfEpsilon
from sel.allPoint import all_point_distance, all_point_distance2
from sel.select_p import select_point
from sel.optGL import opt_select
import time

poi = load_matrix("mat/poi.mat")
num_peo = load_matrix("mat/numPeo.mat")

people_num = 500000
epsilon = 0.004
tim = 18
min_people = 30
cos = 0.8

poi_amount = poi.shape[0]

# peoples = np.random.choice(a=range(poi_amount), size=people_num, replace=True, p=None)
# np.savetxt("real_position/peo_100000.txt", peoples)
# people_filename = "peo_site/" + str(epsilon) + "/peo_" + str(epsilon) + "_" + str(people_num) + "_" + str(tim) + ".txt"
people_filename = "real_position/peo_500000.txt"
peoples = np.loadtxt(people_filename, dtype=int)

new_peoples = np.zeros(people_num, dtype=np.int32)
# new_peoples = np.loadtxt("time==18.txt", dtype=int)
ed = distanceOfEpsilon(epsilon)


def main():
    time_start = time.time()
    for i in range(people_num):
        p_id = peoples[i]
        p_type = int(poi[p_id, 4])
        pmatrix = all_point_distance(p_id, ed, poi)
        # pmatrix2 = all_point_distance2(p_id, ed, poi)
        new_pmatrix = select_point(cos, min_people, tim, pmatrix, p_type, num_peo, poi, p_id)
        pid = opt_select(new_pmatrix, epsilon, tim, num_peo, poi)
        new_peoples[i] = pid
    end_time = time.time()

    spend_time = (end_time - time_start) / 3600
    print('totally cost', spend_time)

    np.savetxt("newpeo.txt", new_peoples)

    print("end")


if __name__ == "__main__":
    main()
    print("end")
