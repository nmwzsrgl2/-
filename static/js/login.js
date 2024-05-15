function keyboardsubmit(event) {
    if (event.keyCode == 13) {
        login();
    }
}
var a = 0;
function checkbox() { 
    a+=1;
    if (a % 2 == 0) {
        document.getElementById("remember").checked = false;
        document.getElementById("remember").value = "false";
    } else {
        document.getElementById("remember").checked = true;
        document.getElementById("remember").value = "true";
    }
}