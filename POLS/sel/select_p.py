import numpy as np


# def cosine_similarity(typeid1, typeid2, numPeo):
#     t1_time = numPeo[typeid1,:]
#     t2_time = numPeo[typeid2,:]
#     num = float(np.dot(t1_time, t2_time))  # 向量点乘
#     denom = np.linalg.norm(t1_time) * np.linalg.norm(t2_time)  # 求模长的乘积
#     return 0.5 + 0.5 * (num / denom) if denom != 0 else 0
#     # return num / denom
def cosine_similarity(typeid1, typeid2, numPeo):
    t1_time = np.zeros(24)
    t2_time = np.zeros(24)
    for i in range(24):
        t1_time[i] = numPeo[typeid1, i]
        t2_time[i] = numPeo[typeid2, i]
    num = np.dot(t1_time.T, t2_time.T)  # 向量点乘
    denom = np.linalg.norm(t1_time) * np.linalg.norm(t2_time)  # 求模长的乘积
    # return 0.5 + 0.5 * (num / denom) if denom != 0 else 0
    return num / denom


def select_point(cos, num_p, time, pmatrix, userType, numPeo, poi, poi_id):
    new_matrix = np.array([], dtype=np.int32)
    for id in pmatrix:
        if int(poi[id, 4]) != userType and cosine_similarity(userType, int(poi[id, 4]), numPeo) <= cos and numPeo[
            int(poi[id, 4]), time] >= num_p:
            new_matrix = np.append(new_matrix, id)
    new_matrix = np.insert(new_matrix, 0, poi_id)
    return new_matrix


def cos_sim(a, b):
    a_norm = np.linalg.norm(a)
    b_norm = np.linalg.norm(b)
    num = a_norm * b_norm
    o = np.dot(a, b)
    cos = o / num
    return cos
