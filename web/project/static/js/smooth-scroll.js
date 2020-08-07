/* activate scrollspy menu */
$('body').scrollspy({
  target: '#navbar-collapsible',
  offset: 52
});

/* smooth scrolling sections */
$('a[href*=\\#]:not([href=\\#])').click(function() {
    if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
      if (target.length) {
        $('html,body').animate({
          scrollTop: target.offset().top - 50
        }, 1000);
        return false;
      }
    }
});

/* scroll reveal */
window.sr = ScrollReveal();
sr.reveal('#home');
sr.reveal('#about');
sr.reveal('#work');
sr.reveal('#blog');
sr.reveal('#contact');

// Customizing a reveal set
sr.reveal('.foo', {duration: 1000});
// Can be any valid CSS distance, e.g. '5rem', '10%', '20vw', etc.
sr.reveal('.foo', {distance: '50px'});