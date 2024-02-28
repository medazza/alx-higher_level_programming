$(document).ready(function () {
    const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  
    $.get(apiUrl, function (data) {
      $('#hello').text(data.hello);
    });
  });