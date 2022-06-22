import numpy as np

def calculate(list):
    #ValueError : "List must contain nine numbers"
    try:
        a = np.array(list)
        b = a.reshape((3,3))
        a1 = np.mean(b, axis=0)
        a2 = np.mean(b, axis=1)
        a3 = np.mean(b[:])
        b1 = np.var(b,axis=0)
        b2 = np.var(b,axis=1)
        b3 = np.var(b[:])
        c1 = np.std(b,axis=0)
        c2 = np.std(b,axis=1)
        c3 = np.std(b[:])
        d1 = np.max(b,axis=0)
        d2 = np.max(b,axis=1)
        d3 = np.max(b[:])
        e1 = np.min(b,axis=0)
        e2 = np.min(b,axis=1)
        e3 = np.min(b[:])
        f1 = np.sum(b,axis=0)
        f2 = np.sum(b,axis=1)
        f3 = np.sum(b[:])
        A = [a1.tolist(), a2.tolist(), a3.tolist()]
        B = [b1.tolist(), b2.tolist(), b3.tolist()]
        C = [c1.tolist(), c2.tolist(), c3.tolist()]
        D = [d1.tolist(), d2.tolist(), d3.tolist()]
        E = [e1.tolist(), e2.tolist(), e3.tolist()]
        F = [f1.tolist(), f2.tolist(), f3.tolist()]

        calculations = {
            'mean' : A,
            'variance' : B,
            'standard deviation' : C,
            'max' : D,
            'min' : E,
            'sum' : F
        }    
        return calculations
    except ValueError : 
        raise ValueError("List must contain nine numbers.")
calculate([0,1,2,3,4,5,6,7,8])