## Install PyMySQL
```
pip install pymysql
```
PyMysql is a replacement for MySQL.
We are going to save username and email in database. 
```
create table userdata
(
id int(2) primary key auto_increment,
username text,
email text
)
```
