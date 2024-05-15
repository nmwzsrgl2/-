function loading() {
    // var name = document.cookie;
    // for (var i = 0; i < name.length; i++) {
    //     if (name[i] == 'user') {
    //         console.log(name[i][0]);
    //     }
    // }
    var name = document.cookie.split('=')[1];
    document.getElementById('username').innerHTML = name;
    return name;
}

function reset_password(input1password) {
    var paasword = document.getElementById(input1password).value;
    var pattern = /^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[~!@#$%^&*)(_+}{|:?><]).{8,16}$/;
    if (paasword == '') {
        alert('密码不能为空');
        return false;
    }
    if (paasword.length < 6 || paasword.length > 16) {
        alert('密码长度应在6-16位之间');
        document.getElementById(input1password).value = '';
        return false;
    }
    if (pattern.test(paasword) == false) {
        alert('密码至少包含大小写字母、数字、特殊字符中的三种')
        document.getElementById(input1password).value = '';
        return false;
    }

}

function password2(a) {
    reset_password(a);
    var password1 = document.getElementById('password').value;
    var password2 = document.getElementById('confirm_password').value;
    if (password1 != password2) {
        alert('两次输入的密码不一致，请重新输入');
        document.getElementById('confirm_password').value = '';
        return false;
    } else {
        return true;
    }
}