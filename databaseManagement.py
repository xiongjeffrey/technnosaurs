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

# initialization for demo, normally this is usergenerated through the extant functions below
database = np.random.randint(100, size=(100, 10))
idNums = [100]*100
tagList = ["Sky", "Rain", "Afternoon", "Birds", "Smiles", "Dumplings", "Wooden Bench", "Rainbow", "Old Man", "School"]
tagList.sort()

# enter new data to database when new media is uploaded
def enter(db, id, tagList):
    if id >= len(db): # if this is for new creator
        db = np.vstack((db, tagList))
        idNums.append(1)

    else: # if this is upload by existing creator
        db[id] = [db[id][i] + tagList[i] for i in range(len(db[id]))]
        idNums[id] += 1

    return db

# create new tag
def newTag(db, list, tagName):
    list.append(tagName)
    db = np.append(db, np.zeros((len(db), 1)), axis=1) # update existing creator profiles assuming nothing falls under new tag
                                                            # creators can add tags to photos if they wish

    return db, list

# add tags to photos
def addTag(db, id, tagName):
    db[id][tagList.index(tagName)] += 1

# remove tags from photos
def removeTag(db, id, tagName):
    if db[id][tagList.index(tagName)] > 0:
        db[id][tagList.index(tagName)] -= 1
    else: # if nothing is tagged under this for the creator, print error!
        print('Oops! No tags found for creator')
