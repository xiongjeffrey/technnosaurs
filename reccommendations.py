import math
import numpy as np

global database
database = [] # matrix of how many times user's product contains a given tag
                # row := each user
                # column := each tag

global idNums
idNums = [] # vector containing the ID of each user
                # integer starting from 1

global phi
phi = 0.35 # each function generally also allows you to modify the phi threshold as needed

# define modified sigmoid function where all values less than phi are set to 0
# sigmoid is also shifted right by 0.5
    # function inputs should be greater than 0
def sigmoid(x, phi):
    if x < phi:
        return 0

    else:
        return (1 / (1 + math.exp(-x - 0.5)))

# wrapper function for any given value of phi
def sigmoidWrapper(phi):

    def retFunc(x):
        return sigmoid(x, phi)

    return retFunc

# normalize values of a given matched user's tag profile
def normalize(inputVec, phi, n):
    retVec = np.array(retVec)/np.sqrt(n)
    retVec = list(map(sigmoidWrapper(phi), inputVec))
    
    return retVec

# normalizes database to be processed for recommendation
def normalizeDatabase():
    retMat = []
    for i in range(len(database)):
        retMat.append(normalize(database[i], phi, idNums[i]))

    return retMat

# recommends the top K number of closest matches to a user 
def recommend(userVec, findMat, topK):
    numMatches = len(findMat)
    recVals = [0]*numMatches

    for i in range(numMatches):
        recVals[i] = np.dot(userVec, numMatches[i])

    # find index of largest K values in recVals
    # Complexity: O(n + k log k)
    indices = np.argpartition(recVals, -1 * topK)[-1 * topK:]
    return np.argsort(indices)
