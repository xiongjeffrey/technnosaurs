import math
import numpy as np
import database

db = database.database
idNums = database.idNums
tagList = database.tagList

global phi
phi = 0.1 # each function generally also allows you to modify the phi threshold as needed

# define modified sigmoid function where all outputs less than phi are set to 0
def sigmoid(x, n, phi):
    sig = (1 / (1 + math.exp(-1*x + (n**(1./2))))) # normalize center of function on the range of [0, n] is 0.5
                                                        # n := number of media a creator has used
    if sig < phi:
        return 0
    return sig

# wrapper function for any given value of phi
def sigmoidWrapper(phi, n):

    def retFunc(x):
        return sigmoid(x, phi, n)

    return retFunc

# normalize values of a given matched user's tag profile
def normalize(inputVec, phi, n):
    retVec = np.true_divide(np.array(inputVec), (n**(1./5))) # root is adjusted based on user preferences on granularity and option breadth
                                                                # smaller the power, greater the granularity
    retVec = list(map(sigmoidWrapper(phi, n), retVec))

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
        recVals[i] = np.dot(userVec, findMat[i])

    print(recVals)

    # find index of largest K values in recVals
    # Complexity: O(n)
    indices = np.argpartition(recVals, -1 * topK)[-1 * topK:]
    return indices # don't particularly care about order, just need them to display!
