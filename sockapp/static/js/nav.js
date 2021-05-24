$(document).ready(function() {

    $("#send-file-nav").addClass("selected-nav-button");

    $("#send-message-nav").click(function() {
        $("#send-message-nav").addClass("selected-nav-button");
        $("#send-file-nav").removeClass("selected-nav-button");
    });

    $("#send-file-nav").click(function() {
        $("#send-file-nav").addClass("selected-nav-button");
        $("#send-message-nav").removeClass("selected-nav-button");
    });
});