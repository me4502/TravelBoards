$(document).ready(function() {
    var body = $("body");

    body.css("display", "none");
    body.fadeIn(1000);
    $(".transition").click(function(event){
        event.preventDefault();
        var linkLocation = this.name;
        $("body").fadeOut(1000, redirectPage(linkLocation));
    });

    function redirectPage(linkLocation) {
        window.location = linkLocation;
    }
});