$("#menu-toggle").click(function(e) {
    e.preventDefault();
    $("#wrapper").toggleClass("toggled");
});

$("#sidebar-wrapper #close").click(function(e) {
    e.preventDefault();
    $("#wrapper").toggleClass("toggled");
});