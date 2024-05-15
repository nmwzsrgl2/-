from flask import *
from datetime import timedelta
import SQL
import Mail
# 创建一个Flask应用,设置静态文件目录和url
app = Flask(__name__, static_folder='static', static_url_path='/static')
#session认证密码
app.secret_key = '1122334455'
#设置session过期时间
app.permanent_session_lifetime = timedelta(days=1)
#登录拦截验证
@app.before_request
def before_request():
    if request.path == '/':
        if session.get('islogin') == 'true':
            return redirect('/index')
        
        else:
            return redirect('/login')


#首页
@app.route('/')
def home():
        return redirect('/index')

#登录页面
@app.route('/login/')
def login():
    if session.get('islogin') == 'true':
        return redirect('/index')
    return render_template('login.html')

#登录验证
@app.route('/login/post', methods=['Post'])
def action():
    username = request.form['username']
    password = request.form['password']
    remember = request.form['remember']
    login_result = SQL.users_login(username, password)
    if login_result == True and remember == 'false':
        session['islogin'] = "false"
        session['username']= username
        session['password']= password
        session['domain']='localhost'
        session['path']='./'  
        resp = make_response(jsonify({'status':200,'url':"/index"}))
        resp.set_cookie('islogin', 'false')
        return resp
    elif login_result == True and remember == 'true':
        session['islogin'] = "true"
        session['username']= username
        session['password']= password
        session['domain']='localhost'
        session['path']='./'
        session.permanent = True
        resp = make_response(jsonify({'status':200,'url':"/index"}))
        resp.delete_cookie('islogin')
        resp.set_cookie('islogin', 'true', max_age=30*24*60*60)
        return resp
    else:
        return jsonify({'status':500,'msg':"用户名或密码错误"})
    

#注册页面    
@app.route('/login/register/')
def register_page():
    return render_template('register.html')

@app.route('/exit')
def exit():
    session.clear()
    return redirect('/login')
# 注册请求
@app.route('/registering',methods=['post'])
def registering():
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    register_result=SQL.users_register(username, password, email)
    if register_result == True:
        return jsonify({'status':200,'url':"/login"})
    else:
        return jsonify({'status':100,'data':"注册失败"})
    
    
# 忘记密码网页
@app.route('/login/forget',methods=['GET'])
def forget_page():
    return render_template('forget.html')

    
# 发送邮件
@app.route('/login/send_email/',methods=['GET'])
def send_mail():
    mail = Mail
    user_mail = request.args['mail']
    try:
        mail.Mail(user_mail).run()
    except:
        return "邮件发送失败"
    return "邮件发送成功"

# 验证验证码
@app.route('/login/reset/',methods=['Get'])
def reset():
    user_mail = request.args['email']
    user_captcha = request.args['captcha']
    check_captcha = SQL.captcha_check(user_mail)
    username = SQL.get_name_by_mail(user_mail)
    print(user_mail,user_captcha,check_captcha)
    if user_captcha == check_captcha:
        response_data = {
            'status':'success',
            'data':"验证码正确",
            'url': "/login/reset_password"
        }
        resp = make_response(jsonify(response_data))
        resp.set_cookie('user', username)
        return resp
    else:
        return jsonify({'status':'fail','data':"验证码错误"})
    
#密码修改页面及修改处理    
@app.route('/login/reset_password/',methods=['Get','POST'])
def reset_password():
    if request.method == 'GET':
        return render_template('reset_password.html')
    else:
        user_password = request.form['password']
        user_name = request.form['username']
        result = SQL.password_change(user_name,user_password)
        if result == True:
            return jsonify({'status':200,'url':"/login"})
        else:
            return jsonify({'status':500,'msg':"密码重置失败"})
#首页
@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=80)