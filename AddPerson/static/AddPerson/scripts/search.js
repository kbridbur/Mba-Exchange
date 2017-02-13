$( document ).ready(function() {
  $(".selectsearch").on('click', function() {
    $('.hidden').css('display', 'none');
    var type = $(this).attr('value').toLowerCase();
    var c = '_search';
    var id = type.concat(c);
    console.log('#'+id);
    $('#'+id).css('display', 'inline-block');
    $('#searchbutton').css('display', 'inline-block');
  });
});
