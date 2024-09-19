# import json
# import mysql.connector as cont
# from flask import make_response,request
# from datetime import datetime, timedelta
# import re
# import jwt
# class auth:
#     def __init__(self):
#         try:
#             self.con=cont.connect(host='localhost',user='root',password="subhan971",database='flask_first')
#             self.cur=self.con.autocommit=True
#             self.cur=self.con.cursor(dictionary=True)
#         except:
#             print("Error connecting")
    
#     def auth_token(self,endpoit):
        
#         def innear1(func):
#             def innear2(*args):
#                 authorization=request.headers.get('Authorization')
#                 # if re.match(r'^Bearer\s*(\S+)\s*$', authorization):
#                 if re.match(r'^Bearer\s*(\S+)\s*$', authorization):
#                     token=authorization.split(" ")[1]
#                     try:
#                         jwtcoded=jwt.decode(token,'key',algorithms='HS256')
#                     except jwt.ExpiredSignatureError:
#                         return make_response({'message':'token expired'},401)
                    
#                     role_id=jwtcoded['payload']['role_id']
#                     self.cur.execute(f"SELECT roles FROM accessibility_view WHERE endpoint='{endpoit}")
#                     result=self.cur.fetchall()
#                     if len(result) > 0:
#                         alowed_roles=json.loads(result[0]['roles'])
#                         if role_id in alowed_roles:
#                             return func(*args)
#                         else:
#                             return make_response({'message':'unauthorized access'},401)
#                 else:
#                     return make_response({'message':'invalid token'},401)
#             return innear2
#         # return innear1
# import json
# import mysql.connector as cont
# from flask import make_response, request
# from datetime import datetime, timedelta
# import re
# import jwt

# class auth:
#     def __init__(self):
#         try:
#             self.con = cont.connect(host='localhost', user='root', password="subhan971", database='flask_first')
#             self.cur = self.con.autocommit=True
#             self.cur = self.con.cursor(dictionary=True)
#         except:
#             print("Error connecting")
    
#     def auth_token(self, endpoint=""):  # Fixed typo in 'endpoit' to 'endpoint'
#         def innear1(func):
#             @wraps(func)
#             def innear2(*args):
#                 endpoint=request.url_rule()
#                 print(endpoint)
#                 authorization = request.headers.get('Authorization')
#                 if re.match(r'^Bearer\s*(\S+)\s*$', authorization):
#                     token = authorization.split(" ")[1]
#                     try:
#                         jwtcoded = jwt.decode(token, 'key', algorithms='HS256')
#                     except jwt.ExpiredSignatureError:
#                         return make_response({'message': 'token expired'}, 401)
                    
#                     role_id = jwtcoded['payload']['role_id']
                    
#                     # Using parameterized queries to prevent SQL injection
#                     self.cur.execute("SELECT roles FROM accesibility_view WHERE endpoint = %s", (endpoint,))
#                     result = self.cur.fetchall()
                    
#                     if len(result) > 0:
#                         allowed_roles = json.loads(result[0]['roles'])
#                         if role_id in allowed_roles:
#                             return func(*args)
#                         else:
#                             return make_response({'message': 'unauthorized access'}, 401)
#                 else:
#                     return make_response({'message': 'invalid token'}, 401)
#             return innear2
#         return innear1

import json
import mysql.connector as cont
from flask import make_response, request
from datetime import datetime, timedelta
import re
import jwt
from functools import wraps  # Add the missing import

class auth:
    def __init__(self):
        try:
            self.con = cont.connect(host='localhost', user='root', password="subhan971", database='flask_first')
            self.cur = self.con.autocommit=True
            self.cur = self.con.cursor(dictionary=True)
        except:
            print("Error connecting")
    
    def auth_token(self, endpoint=""):  # Fixed typo in 'endpoit' to 'endpoint'
        def innear1(func):
            @wraps(func)  # Use @wraps to retain the original function's metadata
            def innear2(*args):
                # Correct usage of request.url_rule
                endpoint = request.url_rule.rule
                print(endpoint)
                
                authorization = request.headers.get('Authorization')
                # if re.match(r'^Bearer\s*(\S+)\s*$', authorization):
                if re.match("^Bearer *([^ ]+) *$", authorization, flags=0):
                    token = authorization.split(" ")[1]
                    try:
                        jwtcoded = jwt.decode(token, 'key', algorithms='HS256')
                    except jwt.ExpiredSignatureError:
                        return make_response({'message': 'token expired'}, 401)
                    
                    role_id = jwtcoded['payload']['role_id']
                    
                    # Using parameterized queries to prevent SQL injection
                    self.cur.execute("SELECT roles FROM accesibility_view WHERE endpoint = %s", (endpoint,))
                    result = self.cur.fetchall()
                    
                    if len(result) > 0:
                        allowed_roles = json.loads(result[0]['roles'])
                        if role_id in allowed_roles:
                            return func(*args)
                        else:
                            return make_response({'message': 'unauthorized access'}, 401)
                else:
                    return make_response({'message': 'invalid token'}, 401)
            return innear2
        return innear1
