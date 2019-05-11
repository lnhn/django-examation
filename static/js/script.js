$(document).ready(function () {
    //验证姓名
    $("#id_name").blur(function () {
        obj = $(this).val();
        var reg = /^[\u0391-\uFFE5]+$/;
        if (obj != "" && !reg.test(obj)) {
            alert('必须输入中文！');
            return false;
        }
    });
    //验证手机
    $("#id_phone").blur(function () {
            mobile = $(this).val();
            console.log(mobile)
            if (mobile.length == 0) {
                alert('手机号码不能为空！');
                return false;
            }
            console.log(mobile);
            if (mobile.length != 11) {
                alert('请输入有效的手机号码，需是11位！');
                return false;
            }

            var myreg = /^(((13[0-9]{1})|(15[0-9]{1})|(18[0-9]{1}))+\d{8})$/;
            if (!myreg.test(mobile)) {
                alert('请输入有效的手机号码！');
                return false;
            }
        }
    );

    //验证年龄
    $("#id_age").blur(function () {
            //验证只能为数字
            obj=$(this).val();
            var reg = /^[0-9]+$/;
            if (obj != "" && !reg.test(obj)) {
                alert('只能输入数字');
                return false;

            }
        }

    );
})