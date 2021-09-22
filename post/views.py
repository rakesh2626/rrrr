from flask import Blueprint,request,jsonify
post = Blueprint('post', __name__)
import pymongo
client = pymongo.MongoClient('mongodb+srv://RAKESH:9959664094@cluster0.t4r4x.mongodb.net/test')
db = client['RAKESH']
mydb = db['SRIPELLY']

@post.route('/add',methods=['POST'])
def add():
    json = request.json
    _name = json['name']
    _email= json['email']
    _password = json['password']

    if _name and _email and _password and request.method == 'POST':

        id = mydb.insert({'name':_name,'email':_email,'password':_password})

        response = jsonify('user added sucessfully')

        response.status_code = 200

        return response