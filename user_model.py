import mysql.connector as cont
import json
from flask import make_response
from datetime import datetime, timedelta
import jwt
class model:
    def __init__(self):
        try:
            self.con=cont.connect(host='localhost',user='root',password="subhan971",database='flask_first')
            self.cur=self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)
        except:
            print("Error connecting")
    
    def get(self):
        self.cur.execute("SELECT * FROM new_table")
        result=self.cur.fetchall()
        if len(result)>0:
            result1= make_response({'Data':result},200)
            # result1.headers["Access-Control-Allow-Origin"] = "*"
            return result1
        
        else:
            return make_response({'message':'no found data'}, 204)
    
    def addone(self,data):
        self.cur.execute(f"INSERT INTO new_table (name,email,phone,password,role_id) VALUES('{data['name']}','{data['email']}','{data['phone']}','{data['password']}',{data['role_id']})")
        return make_response({'message':"the data is enter into the new table successfully"},201)
    
    def update_model(self,data):
        
        self.cur.execute(f"UPDATE new_table SET name='{data['name']}',email='{data['email']}',phone='{data['phone']}',password='{data['password']}',role_id={data['role_id']} WHERE id={data['id']}")
        
        if self.cur._rowcount >0:
            return make_response({'message':"your data is update succesfully"},201)
        else:
            return make_response({'message':'your data is not update suceesfully'},204)
    
    def delete_model(self,id):
        self.cur.execute(f"DELETE FROM new_table WHERE id={id}")
        if self.cur._rowcount >0:
            return make_response({'message':f"your {id} is deleted suceesfully"},201)
        else:
            return make_response({'message':f"your {id} is not deleted suceesfully"},204)

    def patch_model(self,data,id):
        qry="UPDATE new_table SET "
        for key in data:
            qry=qry + f"{key}='{data[key]}' ,"
            
        qr=qry[:-1] +f" WHERE id={id}"
        self.cur.execute(qr)
        if self.cur.rowcount >0:
            return make_response({'Message':'Data updated suceesfully'},201)
        else:
            return make_response({'Message':'Data not updated suceesfully'},204)
        
    def login(self,data):
        self.cur.execute(f"SELECT id,name,email,phone,role_id FROM new_table WHERE email='{data['email']}' AND password='{data['password']}'")
        result=self.cur.fetchall()
        userdata=result[0]
        exp_time=datetime.now()+ timedelta(minutes=15)
        epoch_time=int(exp_time.timestamp())
        payload={
            'payload':userdata,
            'exp':epoch_time
        }
        
        jt_token=jwt.encode(payload,'key',algorithm='HS256')
        
        return make_response({'token':jt_token},200)

