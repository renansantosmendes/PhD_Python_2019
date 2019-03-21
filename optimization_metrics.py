import numpy as np

def pareto(p,q):#p domina q? a resposta é um booleano
    y = False
    if sum(p >= q) == len(p):
        if sum(p == q) != len(p):
            y = True
    return y

def set_coverage_metric(X,Y):
    p_is_dominated = 0
    q_is_dominated = 0
    X_bool = np.zeros(X.shape[0])
    Y_bool = np.zeros(Y.shape[0])
    
    #q dominates p?
    for p in range(Y.shape[0]):
        p_ = Y[p]
        for q in X:
            if pareto(p_,q):
                Y_bool[p] = 1
                
    #q dominates p?
    for q in range(X.shape[0]):
        q_ = X[q]
        for p in Y:
            if pareto(q_,p):
                X_bool[q] = 1
   
    print('Returning C(A,B) and C(B,A)')
    return sum(Y_bool)/len(Y), sum(X_bool)/len(X)