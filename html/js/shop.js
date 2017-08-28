$(function(){ 
$(".accordion dt").click(function(){
    $(this).next("dd").slideToggle();
    $(this).toggleClass("open");
    $(this).siblings("dt").removeClass("open");
});
});