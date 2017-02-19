$( document ).ready(function() {
  $(".addbutton").on('click', function() {
    console.log('hi');
    var target = $(this).attr('value').toLowerCase();
    window.location.href=target
  });
});
