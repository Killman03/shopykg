let banners = $('.banner_image');
let current_banner = 0;

setInterval(function() {
  banners.eq(current_banner).fadeOut(1000, function() {
    current_banner++;
    if (current_banner >= banners.length) {
      current_banner = 0;
    }
    banners.eq(current_banner).fadeIn(1000);
  });
}, 5000);