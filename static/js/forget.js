/*function send_mail() { 
    var email = document.getElementById("email").value; 
    var pattern = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+((\.[a-zA-Z0-9_-]{2,3}){1,2})$/; 
    if (pattern.test(email)) { 
        var button = document.getElementById("send_captcha");
        var countdown = setInterval(button_recovery, 1000);
        var times = 60;
        function button_recovery() {
            times = times - 1;
            button.innerText = times + "秒后重试";
            if (times == 0) {
                button.innerText = "重新发送";
                clearInterval(countdown)
            }
        } 
    } else { 
        alert("请输入正确的邮箱格式！");  
    } 

    }*/
    