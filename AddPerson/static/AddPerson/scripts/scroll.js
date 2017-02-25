$(document).ready(function() {
  $( "#box" ).scroll(function() {
    console.log('plzscroll');
    $('#header').scrollToFixed({
      preFixed: function() { console.log('pre!!!') },
      postFixed: function() { console.log('post!!!') }
    });
  });
});