from flask import Blueprint, render_template,jsonify
get = Blueprint('get', __name__)
import pymongo
client = pymongo.MongoClient('mongodb+srv://RAKESH:9959664094@cluster0.t4r4x.mongodb.net/test')
db = client['RAKESH']
mydb = db['SRIPELLY']
@get.route('/')
def sample_route():
    return 'welcome to the home page...'
@get.route('/getusers',methods=['GET'])
def getusers():
    users =mydb.find()
    multipleuser = []
    for i in users:
        i.pop('_id')
        multipleuser.append(i)
    return jsonify({'users':multipleuser})
@get.route('/getuser/<name>',methods=['GET'])
def getuser(name):
    user=mydb.find_one({'name':str(name)})
    user.pop('_id')
    return jsonify({'users':user})