$(document).ready(function (e) {
    //page 1
    $("#img2").click(function () {
        window.location.href = "2";
    });

    //page 2
    $("#msite2-back").click(function () {
        window.history.back();
    });
    $("#msite2-submit").click(function () {
        window.location.href = "/storeSite/3";
    });

    //page 3
    $("#msite3-back").click(function () {
        window.history.back();
    });
    $("#msite3-submit").click(function () {
        window.location.href = "";
    });

    $(window).resize(function () {
        var width_ = $(window).width();

        if (width_ > 600) {
            $(".msite3-visa").css({
                "border-bottom": "3px solid transparent"
            });
            $(".msite3-amex").css({
                "border-bottom": "3px solid transparent"
            });
            $(".msite3-master").css({
                "border-bottom": "3px solid transparent"
            });
        }
    });

    //set master card
    $(".msite3-master").click(function () {
        $("#visa_radio").prop("checked", false);
        $("#master_radio").prop("checked", true);
        $("#amex_radio").prop("checked", false);
        var width_ = $(window).width();
        if (width_ > 600) {
            $(".msite3-triangle > .msite3-pos1").css({
                "width": "33.333%",
                "margin": "0 66.33% 0 0"
            });
        } else {
            $(".msite3-visa").css({
                "border-bottom": "3px solid transparent"
            });
            $(".msite3-amex").css({
                "border-bottom": "3px solid transparent"
            });
            $(this).css({
                "border-bottom": "3px solid #f4b459"
            });
        }

    });

    //set visa card
    $(".msite3-visa").click(function () {
        $("#visa_radio").prop("checked", true);
        $("#master_radio").prop("checked", false);
        $("#amex_radio").prop("checked", false);
        var width_ = $(window).width();
        if (width_ > 600) {
            $(".msite3-triangle > .msite3-pos1").css({
                "width": "100%",
                "margin": "0 0 0 0"
            });
        } else {
            $(".msite3-master").css({
                "border-bottom": "3px solid transparent"
            });
            $(".msite3-amex").css({
                "border-bottom": "3px solid transparent"
            });
            $(this).css({
                "border-bottom": "3px solid #2394bc"
            });
        }

    });

    //set amex card
    $(".msite3-amex").click(function () {
        $("#visa_radio").prop("checked", false);
        $("#master_radio").prop("checked", false);
        $("#amex_radio").prop("checked", true);
        var width_ = $(window).width();
        if (width_ > 600) {
            $(".msite3-triangle > .msite3-pos1").css({
                "width": "33.333%",
                "margin": "0 0 0 66.33%"
            });
        } else {
            $(".msite3-master").css({
                "border-bottom": "3px solid transparent"
            });
            $(".msite3-visa").css({
                "border-bottom": "3px solid transparent"
            });
            $(this).css({
                "border-bottom": "3px solid #306fc5"
            });
        }

    });

});
