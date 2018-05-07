// 全局变量a和b，分别获取用户框和密码框的value值

//用户框失去焦点后验证value值
function oBlur_1() {
    var name = document.getElementById("name").value;
    if (!name) { //用户框value值为空
        document.getElementById("remind_1").innerHTML = "请输入用户名！";
        document.getElementById("change_margin_1").style.marginBottom = 1 + "px";
    } else { //用户框value值不为空
        document.getElementById("remind_1").innerHTML = "";
        document.getElementById("change_margin_1").style.marginBottom = 19 + "px";
    }
}

//密码框失去焦点后验证value值
function oBlur_2() {
    var psw = document.getElementById("psw").value;
    if (!psw) { //密码框value值为空
        document.getElementById("remind_2").innerHTML = "请输入密码！";
        document.getElementById("change_margin_2").style.marginBottom = 1 + "px";
        document.getElementById("change_margin_3").style.marginTop = 2 + "px";
    } else { //密码框value值不为空
        document.getElementById("remind_2").innerHTML = "";
        document.getElementById("change_margin_2").style.marginBottom = 19 + "px";
        document.getElementById("change_margin_3").style.marginTop = 19 + "px";
    }
}

//用户框获得焦点的隐藏提醒
function oFocus_1() {
    document.getElementById("remind_1").innerHTML = "";
    document.getElementById("change_margin_1").style.marginBottom = 19 + "px";
}

//密码框获得焦点的隐藏提醒
function oFocus_2() {
    document.getElementById("remind_2").innerHTML = "";
    document.getElementById("change_margin_2").style.marginBottom = 19 + "px";
    document.getElementById("change_margin_3").style.marginTop = 19 + "px";
}

//若输入框为空，阻止表单的提交
function submitTest() {
    var name = document.getElementById("name").value;
    var psw = document.getElementById("psw").value;
    if (!name && !psw) { //用户框value值和密码框value值都为空
        document.getElementById("remind_1").innerHTML = "请输入用户名！";
        document.getElementById("change_margin_1").style.marginBottom = 1 + "px";
        document.getElementById("remind_2").innerHTML = "请输入密码！";
        document.getElementById("change_margin_2").style.marginBottom = 1 + "px";
        document.getElementById("change_margin_3").style.marginTop = 2 + "px";
        return false; //只有返回true表单才会提交
    } else if (!name) { //用户框value值为空
        document.getElementById("remind_1").innerHTML = "请输入用户名！";
        document.getElementById("change_margin_1").style.marginBottom = 1 + "px";
        return false;
    } else if (!psw) { //密码框value值为空
        document.getElementById("remind_2").innerHTML = "请输入密码！";
        document.getElementById("change_margin_2").style.marginBottom = 1 + "px";
        document.getElementById("change_margin_3").style.marginTop = 2 + "px";
        return false;
    } else if (name) {
        alert("逗你呢，真注册啊！")
    }
}
