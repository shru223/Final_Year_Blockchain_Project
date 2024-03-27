# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 11:07:14 2020

@author: raju
"""


# Using flask to make an api 
# import necessary libraries and functions 
from flask import Flask, jsonify, request 
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
# creating a Flask app 
app = Flask(__name__) 
gmail_list=[]
# on the terminal type: curl http://127.0.0.1:5000/ 
# returns hello world when we use GET. 
# returns the data that we send when we use POST. 
@app.route('/register', methods = ['GET','POST']) 
def register():
    
    logu=request.json["gmail"]
    passw=request.json["password"]
    
    r1=logu
    
    r2=passw
    

   # if int_features2[0]==12345 and int_features2[1]==12345:

    import MySQLdb


# Open database connection
    db = MySQLdb.connect("localhost","root","","ddbb" )

# prepare a cursor object using cursor() method
    cursor = db.cursor()
    cursor.execute("SELECT user FROM user_register")
    result1=cursor.fetchall()
              #print(result1)
              #print(gmail1)
    for row1 in result1:
                      print(row1)
                      print(row1[0])
                      gmail_list.append(str(row1[0]))
                      
                      #gmail_list.append(row1[0])
                      #value1=row1
                      
    print(gmail_list)
    if logu in gmail_list:
                      return jsonify({'result':'this gmail is already in use '})  
    else:

                  #return jsonify({'result':'this  gmail is not registered'})
              

# Prepare SQL query to INSERT a record into the database.
                  sql = "INSERT INTO user_register(user,password) VALUES (%s,%s)"
                  val = (r1, r2)
   
                  try:
   # Execute the SQL command
                                       cursor.execute(sql,val)
   # Commit your changes in the database
                                       db.commit()
                  except:
   # Rollback in case there is any error
                                       db.rollback()

# disconnect from server
                  db.close()
                  return jsonify({'result':'succesfully registered'})

                      
   
                          



if __name__ == '__main__':
    app.run("0.0.0.0", port=5000, debug=True)
