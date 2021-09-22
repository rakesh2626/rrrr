from flask import Blueprint,request,jsonify
put11 = Blueprint('put', __name__)
import pymongo
client = pymongo.MongoClient('mongodb+srv://RAKESH:9959664094@cluster0.t4r4x.mongodb.net/test')
db = client['RAKESH']
mydb = db['SRIPELLY']


@put11.route('/put/<name>',methods=['PUT'])
def put(name):
    _name1 = name
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _password = _json['password']

    if _name and _email and _password and _name and request.method=='PUT':

        data = ({'name':_name,'email':_email,'password':_password})
        query = {'name':_name1}
        mydb.update_one(query,{'$set':data})

        return jsonify('user updated succesfully')