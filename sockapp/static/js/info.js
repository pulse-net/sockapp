$(document).ready(function() {

    function get_input_html_tags(id, placeholder, span_id) {
        var current_value = $("#" + span_id).html();
        return `<input type='text' id='${id}' class='inputData' placeholder='${placeholder}' value='${current_value}'>`;
    }

    $("#edit").click(function() {
        var current_value = $("#edit").attr('value');
        var new_value = current_value == "Edit" ? "Save" : "Edit";
        $("#edit").attr('value', new_value);

        if(current_value == "Edit") {
            var protocol_select = "<select id='protocol-inp' class='inputData'";

            var current_protocol = $("#protocol-span").html();
            tcp_current_protocol = current_protocol == "TCP" ? "selected" : "";
            udp_current_protocol = current_protocol == "UDP" ? "selected" : "";

            protocol_select += `><option value='TCP' ${tcp_current_protocol}>TCP</option>`;
            protocol_select += `<option value='UDP' ${udp_current_protocol}>UDP</option>`;
            protocol_select += "</select>";

            $("#port-span").html(get_input_html_tags("port-inp", "Enter port number", "port-span"));
            $("#protocol-span").html(protocol_select);
            $("#cur-dir-span").html(get_input_html_tags("cur-dir-inp", "Enter working directory", "cur-dir-span"));
        } else if(current_value == "Save") {
            var port = $("#port-inp").val();
            var protocol = $("#protocol-inp").val();
            var cur_dir = $("#cur-dir-inp").val();

            if(port && protocol && cur_dir) {
                $.ajax({
                    url: "/update-args",
                    type: "post",
                    data: {"port": port, "protocol": protocol, "cur_dir": cur_dir},
                    success: function(result) {
                        Swal.fire({
                            icon: result.icon,
                            title: result.title,
                            text: result.status,
                        });

                        window.location.reload();
                    }
                });
            } else {
                Swal.fire({
                    icon: "error",
                    title: "Error",
                    text: "Cannot leave empty values for any of these fields!",
                });
            }
        }
    });

});