from flask import Flask, jsonify, request
from flask_cors import CORS

import numpy as np
import recommendation
import database

db = database.database
idNums = database.idNums
tagList = database.tagList

dbTagged = np.vstack(tagList, db)

app = Flask(__name__)
CORS(app)

@app.route('/addmedia')
def add(id, tags):
    database.enter(id, tags)
    return "Executed"

@app.route('/user')
def getProfile(id):
    profileTagged = np.vstack(tagList, db[id])
    return jsonify(profileTagged)

@app.route('/rec')
def getRecs(userVec, k):
    return jsonify(recommendation.recommend(userVec, db, k))

@app.route('/addTag')
def addTag(id, tag):
    database.addTag(id, tag)
    return('Added!')

@app.route('/addTag')
def removeTag(id, tag):
    database.removeTag(id, tag)
    return('Removed!')