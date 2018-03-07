import pymysql.cursors

#connect to the database
connection = pymysql.connnect (host='localhost',
                               user='user',
                               password='passwd',
                               db='db',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)

# Create a registration form with username and email as inpput field.
# Catch form values and save them in database using insert query and close the connection.

from flask import Flask, render_template, request, json

app = Flask(__name__)

@app.route("/get-reg")
def login():
  return render_template('reg.html')

@app.route("/save-post", methods=['POST', 'GET'])
def signup():
  if request.method == 'POST':
    name = request.form['name']
    email = request.form['email']
    try:
      with connection.cursor() as cursor:
        #read a single record:
        sql = "INSERT INTO userdata (username, email) VALUES (%s, %s)"
        cursor.execute(sql, (name, email))
        connection.commit()
    finally:
      connection.close()
      return "Saved Successfully"
  else:
    return 'error'
  
if __name__ == '__main__':
  app.run()
