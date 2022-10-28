import math

import gurobipy as gp
import numpy as np
from gurobipy import GRB
from pl.planarLaplace import distance


def optql(x_list, pi_list, dQ, epsilon=0.5):
    """
            This function implements a geo-indistinguishable mechanism of optimal utility without graph spanner. For more
            details, please check the paper: https://hal.inria.fr/hal-01114241/document.
            Privacy Level: epsilon

            Parameters
            ----------
            x_list : list
                The list of locations for generating the spanner. Eg. [(1, 3), (-2, 2), (4, 1)]
            pi_list : list
                The weight of each location in x_list. It should have the same number of elements as x_list. Normalization
                will be done during the mechanism. Eg. [3, 5, 2]
            dQ : function
                The distance metric used for assigning weights to edges. The function should take two locations and return
                a scaler distance.
                Eg. dQ = lambda (x, y): math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)
            epsilon (optional) : float, default 0.5
                The parameter determining privacy level for this mechanism. The final privacy level would be epsilon.

            Returns
            -------
            matrix : numpy.ndarray
                The generated stochastic transition matrix. Given n locations, the shape of this matrix would be (n, n).
            pre_prob : numpy.ndarray
                The normalized pre-process probability distribution
            post_prob : numpy.ndarray
                The post-process probability distribution
        """
    try:
        assert len(x_list) == len(pi_list)
    except AssertionError:
        print('x_list and pi_list should have the same length.')
    print(f'Start building a linear program for {len(x_list)} locations...')
    pre_prob = np.array(pi_list) / sum(pi_list)  # normalize probability distribution
    n = len(x_list)  # get number of elements
    threshold = math.exp(epsilon)

    # define a model
    model = gp.Model('OptQL')

    # add variables accessed as (0, 0), (0, 1), (1, 1), ...
    variables = model.addVars(n, n, lb=0.0, ub=1.0, name='k')

    # set objective function
    model.setObjective(
        gp.quicksum(pre_prob[i] * variables[i, j] * dQ(x_list[i][0], x_list[i][1], x_list[j][0], x_list[j][1]) \
                    for i in range(n) for j in range(n)), GRB.MINIMIZE)

    # add constraints (1)
    print('Adding differential privacy constraints...')
    model.addConstrs(
        variables[i, k] <= pow(threshold, dQ(x_list[i][0], x_list[i][1], x_list[j][0], x_list[j][1])) * variables[j, k] \
        for i in range(n) for j in range(n) for k in range(n))

    # add constraints (2)
    print('Add probability sum constraints...')
    model.addConstrs(gp.quicksum(variables.select(i, '*')) == 1 for i in range(n))

    # constraints (3) are already satisfied

    # optimize the model
    print('Start solving the model...')
    model.optimize()

    # build a matrix to store the stochastic matrix
    variables = model.getAttr('x', variables)
    matrix = np.zeros((n, n))
    for key, value in variables.items():
        matrix[key] = value

    # get post-process probability distribution
    # post_prob = pre_prob @ matrix

    # return matrix, pre_prob, post_prob
    return matrix


def opt_select(poi_m, epsilon, time, numPeo, poi):
    # s = poi_m.size
    if poi_m.size == 1:
        return -1
    x_list = []
    pi_list = []
    for i in poi_m:
        x_list.append((poi[i, 0], poi[i, 1]))
        pi_list.append(numPeo[int(poi[i, 4]), time])

    distur_matrix = optql(x_list, pi_list, distance, epsilon)
    # dm = np.array(distur_matrix[0],dtype=np.int64)
    try:
        real_dis_mat = distur_matrix[0][1:]
        if np.all(real_dis_mat == 0):
            return np.random.choice(poi_m[1:], size=1, replace=True, p=None)
        # return np.random.choice(poi_m, size=1, replace=True, p=distur_matrix[0]/sum(distur_matrix[0]))
        return np.random.choice(poi_m[1:], size=1, replace=True, p=real_dis_mat / sum(real_dis_mat))
    except ValueError:


        for i in range(len(real_dis_mat)):
            if real_dis_mat[i] < 0:
                real_dis_mat[i] = 0
        # return np.random.choice(poi_m, size=1, replace=True, p=distur_matrix[0] / sum(distur_matrix[0]))
        return np.random.choice(poi_m[1:], size=1, replace=True, p=real_dis_mat / sum(real_dis_mat))
