import numpy as np


global database
database = [] # matrix of how many times creator's product contains a given tag
                # row := each user
                # column := each tag

global idNums
idNums = [] # vector containing the ID of each user
                # integer starting from 1

global tagList # vector containing strings associated with each possible tag
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

def addTag(id, tagName):
    id[tagList.index(tagName)] += 1

def removeTag(id, tagName):
    id[tagList.index(tagName)] -= 1
