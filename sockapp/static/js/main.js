$(document).ready(function() {
    
    $("#send").click(function() {
        var recv_ip = $("#recv_ip").val();
        var send_path = $("#send_path").val();

        if(recv_ip && send_path) {
            $.ajax({
                url: "/send",
                type: "post",
                dataType: "json",
                data: {"recv_ip": recv_ip, "send_path": send_path},
                success: function(result) {
                    alert(result.status);
                }
            });
        } else {
            alert("Both receiver IP and file path are required!");
        }
    });

    $("#receive").click(function() {
        $("#receive").addClass("selected-button");
        $.ajax({
            url: "/receive",
            type: "post",
            dataType: "json",
            success: function(result) {
                alert(result.status);
                $("#receive").removeClass("selected-button");
            }
        });
    });

});