import numpy as np

def calculate(list):
    
        result = dict()
        mtrx = np.array(list).reshape(3, 3)
        result["mean"] = [mtrx.mean(0).tolist(), mtrx.mean(1).tolist(), mtrx.mean()]
        result["variance"] = [mtrx.var(0).tolist(), mtrx.var(1).tolist(), mtrx.var()]
        result["standared deviation"] = [mtrx.std(0).tolist(), mtrx.std(1).tolist(), mtrx.std()]
        result["sum"] = [mtrx.sum(0).tolist(), mtrx.sum(1).tolist(), mtrx.sum()]
        result["max"] = [mtrx.max(0).tolist(), mtrx.max(1).tolist(), mtrx.max()]
        result["min"] = [mtrx.min(0).tolist(), mtrx.min(1).tolist(), mtrx.min()]
        
        return result
