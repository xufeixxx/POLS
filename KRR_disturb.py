import numpy as np
import random

N_loc = 87635

def krr_disturb(poi_id, N_loc, epsilon):
    prob_p = np.exp(epsilon) / (np.exp(epsilon) + N_loc - 1)
    # prob_q = (1 - prob_p) / (N_loc - 1)

    temp_prob = random.random()
    if temp_prob < prob_p:
        return poi_id
    else:
        temp_list = list(range(N_loc))
        del (temp_list[poi_id])
        return random.choice(temp_list)


dis_id = krr_disturb(125,N_loc,0.01)
print(dis_id)