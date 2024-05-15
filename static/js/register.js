function username_check() { 
    var namelengths 
    namelengths = document.getElementById('username').value.length;
    if (namelengths > 10) {
        alert("用户名不能超过10个字符");
        document.getElementById('username').value = '';
        return false;
    } else {
        return true;
    }
}

function password_check() {
    var pattern = /^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[~!@#$%^&*)(_+}{|:?><]).{8,16}$/;
    var passwordleaths = document.getElementById('password').value.length;
    if (passwordleaths < 20 && pattern.test(document.getElementById('password').value)) {
        return true;

    } else {
        alert("密码必须包含大小写字母、数字和特殊字符，长度在8-20位之间");
        document.getElementById('password').value = '';
        return false;
    }
}

function password_confirm() {
    password_check();
    p1 = document.getElementById('password').value;
    p2 = document.getElementById('confirm_password').value;
    if (p1 == p2) {
        return true;
    } else {
        alert("两次输入的密码不一致，请重新输入");
        document.getElementById('confirm_password').value = '';
        return false;
    }
}


function email_check() {
    var pattern = /^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/;
    var emailleaths = document.getElementById('email').value.length;
    if (emailleaths > 0 && pattern.test(document.getElementById('email').value)) {
        return true;
    } else {
        alert("请输入正确的邮箱地址");
        document.getElementById('email').value = '';
        return false;
    }
}

function register() { 
    if (username_check() && password_check() && password_confirm() && email_check()) {
        register_form();
    } else {
        return false;
    }
}