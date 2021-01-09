import numpy as np

def calculate(list):
    calculations = dict()
    mtrx = np.array(list).reshape(3, 3)
    calculations["mean"] = [mtrx.mean(0).tolist(), mtrx.mean(1).tolist(), mtrx.mean()]
    calculations["variance"] = [mtrx.var(0).tolist(), mtrx.var(1).tolist(), mtrx.var()]
    calculations["standared deviation"] = [mtrx.std(0).tolist(), mtrx.std(1).tolist(), mtrx.std()]
    calculations["sum"] = [mtrx.sum(0).tolist(), mtrx.sum(1).tolist(), mtrx.sum()]
    calculations["max"] = [mtrx.max(0).tolist(), mtrx.max(1).tolist(), mtrx.max()]
    calculations["min"] = [mtrx.min(0).tolist(), mtrx.min(1).tolist(), mtrx.min()]
    return calculations
