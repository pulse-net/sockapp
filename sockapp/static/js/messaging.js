$(document).ready(function() {
    $("#send-message-nav").addClass("selected-nav-button");
    $("#send-file-nav").removeClass("selected-nav-button");

    $("#send").click(function() {
        var recv_ip = $("#recv_ip").val();
        var send_msg = $("#send_msg").val();

        if(recv_ip && send_msg) {
            $.ajax({
                url: "/send-message",
                type: "post",
                dataType: "json",
                data: {"recv_ip": recv_ip, "send_msg": send_msg},
                success: function(result) {
                    Swal.fire({
                        icon: result.icon,
                        title: result.title,
                        text: result.status,
                    });
                }
            });
        } else {
            Swal.fire({
                icon: "error",
                title: "Error",
                text: "Both receiver IP and message are required!",
            });
        }
    });
});