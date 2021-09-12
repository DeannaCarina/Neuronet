
// Fade return to top button in based on scroll position
$(window).scroll(function () {
    if ($(this).scrollTop() > 75) {
        $('#toTopBtn').fadeIn();
    } else {
        $('#toTopBtn').fadeOut();
    }
});

// Smooth scroll to top on click
$('#toTopBtn').click(function () {
    $('html, body').stop().animate({
        scrollTop: 0
    }, 100);
});