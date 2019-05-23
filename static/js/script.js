function check_chinese(obj) {
    obj_str = obj.delegateTarget.value
    console.log(obj.delegateTarget.value)
    var reg = /^[\u0391-\uFFE5]+$/;
    if (obj_str != "" && !reg.test(obj_str)) {
        alert('必须输入中文！');
        return false;
    }
}




$(document).ready(function () {

        //显示欢迎的mmodal
  $('#welcomeModal').modal('toggle');

  function checkexamtype(examtype){

      $('#welcomeModal').modal('toggle')
      timerStart()
      $.ajax(
          {
              url:examtype.data,
              type:'GET',
          }
      )

  }

  $('#practice').click(eventData='practice',handler=checkexamtype)
    $('#formal').click('forma',handler=checkexamtype)



    //验证姓名

    $("#id_name").blur(check_chinese);
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
            obj = $(this).val();
            var reg = /^[0-9]+$/;
            if (obj != "" && !reg.test(obj)) {
                alert('只能输入数字');
                return false;

            }
        }
    );

    question_total_num = parseInt($('#total_quesiton_number').text());

    function checkradio() {

        for (var i = 1; i <= question_total_num; i++) {
            var radios = document.getElementsByName('choiceans' + i.toString());

            for (radio in radios) {
                if (radios[radio].checked) {
                    $('#btn' + i).removeClass('btn-secondary');
                    $('#btn' + i).addClass('btn-primary');
                    break;
                }

            }
        }
    };






    $('.carousel').carousel({
        interval: false
    });

    $('#prequestion').click(function () {
        $('.carousel').carousel('prev');
        checkradio();
        putquestionid();
    });

    $('#nextquestion').click(function () {
        $('.carousel').carousel('next');
        checkradio();
        putquestionid();
    });


    $('.questionID').click(function () {
        var que_id = $(this).text().trim();
        current_question_id = que_id;
        que_id = parseInt(que_id) - 1;
        $('.carousel').carousel(que_id);
        checkradio();
        putquestionid();


    });

        function putquestionid() {
        var current_question_id = $('.active.carousel-item').attr('id').slice(1,);
        console.log(current_question_id)
        $('#question_id').html(current_question_id);
    }


    function timerStart() {

        var oDate = new Date();
        var nowTime = oDate.getTime(); //现在的毫秒数
        oDate.setMinutes(oDate.getMinutes() + 60); // 设定截止时间为60分钟后
        var targetDate = new Date(oDate.toString());
        run(targetDate);
    }




});

var timer;

function run(enddate) {
    getDate(enddate);
    timer = setInterval("getDate('" + enddate + "')", 1000);
}

function getDate(enddate) {

    var oDate = new Date(); //获取日期对象

    var nowTime = oDate.getTime(); //现在的毫秒数
    var enddate = new Date(enddate);
    var targetTime = enddate.getTime(); // 截止时间的毫秒数

    var second = Math.floor((targetTime - nowTime) / 1000); //截止时间距离现在的秒数

    var day = Math.floor(second / 24 * 60 * 60); //整数部分代表的是天；一天有24*60*60=86400秒 ；
    second = second % 86400; //余数代表剩下的秒数；
    var hour = Math.floor(second / 3600); //整数部分代表小时；
    second %= 3600; //余数代表 剩下的秒数；
    var minute = Math.floor(second / 60);
    second %= 60;
    var spanH = $('.se-txt')[0];
    var spanM = $('.se-txt')[1];
    var spanS = $('.se-txt')[2];

    spanH.innerHTML = tow(hour);
    spanM.innerHTML = tow(minute);
    spanS.innerHTML = tow(second);

    if (minute == 0 && second == 0 && hour == 0) {
        clearInterval(timer);
        alert('times up, pls submit your form.....')
    }
}

function tow(n) {
    return n >= 0 && n < 10 ? '0' + n : '' + n;
}

