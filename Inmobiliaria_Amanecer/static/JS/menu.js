$(document).ready(function(){

    var altura = $('.navbarMaster').offset().top;
    
    $(window).on('scroll', function (){
        
        if ($(window).scrollTop() > altura) {
            
            $('.navbarMaster').addClass('navbar-fixed')

        } else {
            
            $('.navbarMaster').removeClass('navbar-fixed')

        }

    });
});
