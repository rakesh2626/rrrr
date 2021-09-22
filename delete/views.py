from flask import Blueprint,jsonify
delete11 = Blueprint('delete', __name__)
import pymongo
client = pymongo.MongoClient('mongodb+srv://RAKESH:9959664094@cluster0.t4r4x.mongodb.net/test')
db = client['RAKESH']
mydb = db['SRIPELLY']


@delete11.route('/delete/<name>',methods=['DELETE'])
def delete(name):
    
    users = mydb.delete_one({'name':str(name)})
    return {'users':users}
    