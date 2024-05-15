from pymysql import *
# 验证用户名和密码
def users_login(name,userpassword):    
    db = connect(
    host='localhost', 
    user='root', 
    password='123456', 
    port=3306, 
    autocommit=True
    )
    db.select_db('users_sys')
    cursor = db.cursor()      
    cursor.execute("SELECT * FROM users where name = '%s' and password = '%s';" % (name, userpassword))
    results = cursor.fetchall()
    print(results)
    try:
        if results[0][1] == name and results[0][2] == userpassword:
            print('Login successful')
            return True
        else:
            print('login failed')
            return False
    except:
        return False

# 注册新用户
def users_register(name,password,mail):
    db = connect(
    host='localhost', 
    user='root', 
    password='123456', 
    port=3306, 
    autocommit=True
    )
    db.select_db('users_sys')
    cursor = db.cursor()   
    cursor.execute("SELECT * FROM users where name = '%s'" % (name))
    result = cursor.fetchall()
    print(result)
    try:
        if result[0][1]== name:
            return False
    except:
        cursor.execute(f"INSERT INTO users (name, password, mail) VALUES('{name}','{password}','{mail}')")
        return True
    db.close()
# 获取邮箱对应的用户名
def get_name_by_mail(mail):
    db = connect(
    host='localhost', 
    user='root', 
    password='123456', 
    port=3306, 
    autocommit=True
    )
    db.select_db('users_sys')
    cursor = db.cursor()   
    cursor.execute("SELECT * FROM users where mail = '%s';" % (mail))
    try:
        result = cursor.fetchall()[0][1]
        return result
    except:
        return False
# 验证码存储
def captcha_add(mail,captcha):
    db = connect(
    host='localhost', 
    user='root', 
    password='123456', 
    port=3306, 
    autocommit=True
    )
    db.select_db('users_sys')
    cursor = db.cursor()   
    cursor.execute("INSERT INTO users_captcha(mail, captcha) VALUES('%s', '%s');" % (mail, captcha))
    db.close()
# 验证码删除
def captcha_rm (mail):
    db = connect(
    host='localhost', 
    user='root', 
    password='123456', 
    port=3306, 
    autocommit=True
    )
    db.select_db('users_sys')
    cursor = db.cursor()   
    result=cursor.execute("DELETE FROM users_captcha WHERE mail = '%s'" % (mail))
    db.close()

# 验证码验证
def captcha_check(mail):
    db = connect(
    host='localhost', 
    user='root', 
    password='123456', 
    port=3306, 
    autocommit=True
    )
    db.select_db('users_sys')
    cursor = db.cursor()
    cursor.execute("SELECT captcha FROM users_captcha WHERE mail = '%s'" % (mail))
    result = cursor.fetchall()
    if result:
        return result[0][0]
    else:
        return False
    
#用户密码重置    
def password_change(name,password):
    db = connect(
    host='localhost', 
    user='root', 
    password='123456', 
    port=3306, 
    autocommit=True
    )
    db.select_db('users_sys')
    cursor = db.cursor()
    cursor.execute("UPDATE users SET password = '%s' WHERE name = '%s'" % (password, name))
    if cursor:
        return True
    else:
        return False
