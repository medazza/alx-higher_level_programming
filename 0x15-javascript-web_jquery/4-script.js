$(document).ready(function () {
    $('#toggle_header').click(function () {
      const headerElmnt = $('header');
  
      if (headerElmnt.hasClass('red')) {
        headerElmnt.removeClass('red').addClass('green');
      } else if (headerElmnt.hasClass('green')) {
        headerElmnt.removeClass('green').addClass('red');
      } else {
        headerElmnt.addClass('red');
      }
    });
  });