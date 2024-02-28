$('document').ready(function () {
    $('#btn_translate').click(translate);
    $('#language_code').focus(function () {
      $(this).keydown(function (enter) {
        if (enter.keycode === 13) {
            translate();
        }
    });
    });
});
  
function translate () {
    const apiUrl = 'https://www.fourtonfish.com/hellosalut/?';
    $.get(apiUrl + $.param({ lang: $('#language_code').val() }), function (data) {
        $('#hello').html(data.hello);
    });
}