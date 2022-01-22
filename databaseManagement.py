import numpy as np

global database
database = []

global idNums
idNums = []

global tagList
tagList = []

def enter(id, tagList):
    if id >= len(database):
        database.append(tagList)
        idNums.append(1)

    else:
        database[id] = [database[id][i] + tagList[i] for i in range(len(database[id]))]
        idNums[id] += 1

def addTag(tagName):
    tagList.append(tagName)
    np.append(database, np.zeros((len(database), 1)), axis=1)

    return database
