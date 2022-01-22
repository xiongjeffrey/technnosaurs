def enter(id, tagList):
    if id >= len(database):
        database.append(tagList)
        idNums.append(1)

    else:
        database[id] = [database[id][i] + tagList[i] for i in range(len(database[id]))]
        idNums[id] += 1
