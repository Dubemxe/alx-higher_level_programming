(function() {
function toggleColor(tag) {
  $('#toggle_header').on("click", function() {
    if($(tag).hasClass('red')) {
      $(tag).removeClass('red');
      $(tag).addClass('green'); }
      else if($(tag).hasClass('green')) {
      $(tag).removeClass('green');
      $(tag).addClass('red'); }

  });
}

toggleColor('header');
})();
