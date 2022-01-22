import math
import numpy as np

global phi
phi = 0.35

def sigmoid(x, phi):
    if x < phi:
        return 0

    else:
        return (1 / (1 + math.exp(-x - 0.5)))

def sigmoidWrapper(phi):

    def retFunc(x):
        return sigmoid(x, phi)

    return retFunc

def normalize(inputVec, phi, n):
    retVec = list(map(sigmoidWrapper(phi), inputVec))
    retVec = np.array(retVec)/np.sqrt(n)
    return retVec

def recommend(userVec, findMat, topK):
    numMatches = len(findMat)
    recVals = [0]*numMatches

    for i in range(numMatches):
        recVals[i] = np.dot(userVec, numMatches[i])

    # find index of largest K values in recVals
    # Complexity: O(n + k log k)
    indices = np.argpartition(recVals, -1 * topK)[-1 * topK:]
    return np.argsort(indices)

if __name__ == '__main__':
    arr = [0.1, 0.5, 0.9, 0.3, 0.4]
    phi = 0.35

    wrap = sigmoidWrapper(phi)
    print(wrap(x = 0.3))
    print(normalize(arr, phi))