function tantan(a) {
    var result = confirm('狠心删除 T_T');
    if (result) {

        $.ajax({
            type: 'POST',
            url: '/delete/',
            data: {'id': a},
            dataType: "json",
            success: function (s_data) {
                if (s_data.status == 200) {
                    alert('删除成功，如果反悔，请在24小时之内想办法寻找！');
                    $('#f1')[0].reset();
                    window.location.href = window.location.href;
                    window.location.reload;
                } else if (s_data.status == 300) {
                    alert("没有找到要删除的文件，可能已丢失")
                }
            },
        });
    } else {
        return false;

    }
}

function fo(sr) {

    $.ajax({
        type: 'POST',
        url: '/download/',
        data: {'data': sr},
        success: function (s_data) {
            alert(s_data.error)
        },
        dataType: "json",
    });

}

function fun() {
    var msg = document.getElementById('files').value;
    if (msg == "") {
        alert("请先选择文件");
        return false;
    }
}

