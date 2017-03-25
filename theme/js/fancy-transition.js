$(document).ready(function() {
    $("body").css("display", "none");
    $("body").fadeIn(1000);
    $(".transition").click(function(event){
        event.preventDefault();
        linkLocation = this.name;
        $("body").fadeOut(1000, redirectPage);
    });

    function redirectPage() {
        window.location = linkLocation;
    }
});