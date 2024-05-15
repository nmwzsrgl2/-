function scrollToHeight() {
    // 使用window.scrollTo()滚动到指定高度  
    window.scrollTo({
        top: 812,
        behavior: 'smooth' // 平滑滚动（可选，取决于浏览器支持）  
    });

    // 确保在滚动完成后执行回调  
    // 注意：由于scroll事件是连续触发的，所以我们不能直接使用scroll事件来检测滚动结束  
    // 这里我们使用setTimeout作为一个简单的模拟，但在实际项目中可能需要更复杂的逻辑来检测滚动结束  
    // setTimeout(function () {
    //     if (window.scrollY === 812) {
    //         // 滚动到指定位置后执行回调  
    //         callback();
    //     }
    // }, 500); // 这里的延迟时间需要根据你的实际情况来调整  
}
function td_list() {
    var td_list = document.getElementsByTagName("td");
    var timers = setInterval(td_list_active, 250);
    var i = -1;
    function td_list_active() {
        i = i + 1;
        td_list[i].className = "td_title_active";
        if (i == 5) {
            clearInterval(timers);
            for (var j = 0; j < 5; j++) {
                td_list[j].className = "td_title";
            }
            setTimeout(function () {
                td_list[5].className = "td_title";
            }, 250);
        }
    }
}


function show_hide() { 
    window.scrollTo({
        top: 1621,
        // 平滑滚动（可选，取决于浏览器支持）  
    });
}

function show_img() { 
    var img =document.getElementsByClassName('images')
    for (var i = 0; i < img.length; i++) { 
        img[i].className = "images_active";
    };
    for (var j = 0; j < img.length; j++) {
        img[j].className = "images";
    }
}
window.onscroll = function () {
    var scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
    if (scrollTop >=0 && scrollTop < 812) {
        document.getElementById("header_1").style.backgroundColor = " #00b3ff";
        document.getElementById("header_1").style.color = "white";
        document.getElementById("header_2").style.backgroundColor = "";
        document.getElementById("header_2").style.color = "#000000";
        document.getElementById("header_3").style.backgroundColor = "";
        document.getElementById("header_3").style.color = "#000000";
        document.getElementById("header_4").style.backgroundColor = "";
        document.getElementById("header_4").style.color = "#000000";
    } 
    if (scrollTop >= 812 && scrollTop < 1621) {
        document.getElementById("header_1").style.backgroundColor = "";
        document.getElementById("header_1").style.color = "#000000";
        document.getElementById("header_2").style.backgroundColor = " #00b3ff";
        document.getElementById("header_2").style.color = "white";   
        document.getElementById("header_3").style.backgroundColor = "";
        document.getElementById("header_3").style.color = "#000000";
        document.getElementById("header_4").style.backgroundColor = "";
        document.getElementById("header_4").style.color = "#000000";
        
    }
    if (scrollTop == 812) { 
        var a = 0;
        a= a + 1;
        if (a == 1) {
            td_list();
            a = 0;
        } 
    }
    if (scrollTop >= 1600) { 
        document.getElementById("header_1").style.backgroundColor = "";
        document.getElementById("header_1").style.color = "#000000";
        document.getElementById("header_2").style.backgroundColor = "";
        document.getElementById("header_2").style.color = "#000000";
        document.getElementById("header_3").style.backgroundColor = " #00b3ff";
        document.getElementById("header_3").style.color = "white";    
        document.getElementById("header_4").style.backgroundColor = "";
        document.getElementById("header_4").style.color = "#000000";
    }
    if (scrollTop >= 1621) {
        show_img()
    }
    if (scrollTop >= 3300) {
        document.getElementById("header_1").style.backgroundColor = "";
        document.getElementById("header_1").style.color = "#000000";
        document.getElementById("header_2").style.color = "#000000";
        document.getElementById("header_2").style.backgroundColor = "";
        document.getElementById("header_3").style.color = "#000000";
        document.getElementById("header_3").style.backgroundColor = "";
        document.getElementById("header_4").style.backgroundColor = " #00b3ff";
        document.getElementById("header_4").style.color = "white";
    }
}

function incudice() {
    window.scrollTo({
        top: 3500,
        behavior: 'smooth' // 平滑滚动（可选，取决于浏览器支持）  
    });
}