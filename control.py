from app import app 
from model.user_model import model
from model.auth_model import auth
from flask import request
from colorama import Fore

obj=model()
auth=auth()
@app.route('/getall')
@auth.auth_token()
def sale():
    return obj.get()
# @app.route('/addone',methds=["POST"])
# def addone():
    
#     return obj.addone(request.form)
@app.route('/addone', methods=['POST'])
def addone():
    return obj.addone(request.form)

@app.route('/update', methods = ["PUT"])
@auth.auth_token()
def update():
    return obj.update_model(request.form)

# @app.route('/delete/<id>' , methods=["DELETE"])
@app.route('/delete', methods=['DELETE'])
@auth.auth_token()
def delete():
    return obj.delete_model(id=request.form['id'])

@app.route('/patch/<id>' , methods=["PATCH"])
def patch(id):
    
    return obj.patch_model(request.form,id) 


@app.route('/user/login',methods=['POST'])
def userlogin():
    
    return obj.login(request.form)