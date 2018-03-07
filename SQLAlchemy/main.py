# MySQL coonection
from sqlalchemy import create_engine, MetaData, Table
from flask import Flask, render_template,request,json

app = Flask(__name__)

engine = create_engine('mysql+pymysql:////username:password@localhost/db_name', convert_unicode=True)
metadata = MetaData(bind=engine)

# connect to particular table. users is table in mysql database.
users = Table('users', metadata, autoload=True)

#retrieve data
@app.route("/getdata")
def getdata():
  r = users.select(users.c.id == 1).execute().first()
  return r['name']
 
# using execute() for our own query
# engine.execute('select * from users where id = :1', [1]).first()

# inserting data using insert after connection. Also no need to commit explicitly
# con = engine.connect()
# con.execute(users.insert(), name='raja', email='raja@mail.com')

@app.route("/")
def index():
    return "welcome"

if __name__ == "__main__":
    app.run()
