from pymysql import *


# Connect to the database
db = connect(
    host='localhost', 
    user='root', 
    password='123456', 
    port=3306, 
    autocommit=True
)
db.select_db('users_sys')
cursor = db.cursor()      

def select_all_users():     
    cursor.execute("SELECT * FROM users;")
    result = cursor.fetchall()[0]
    print(result)
def select_captcha():
    cursor.execute("SELECT * FROM users_captcha WHERE mail='3533033347@qq.com';")
    result = cursor.fetchone()
    print(result)
    #删除
def delete_captcha():
    cursor.execute("DELETE FROM users_captcha WHERE mail='3533033347@qq.com';")
    result = cursor.fetchone()
    print(result)

# delete_captcha()
select_captcha()