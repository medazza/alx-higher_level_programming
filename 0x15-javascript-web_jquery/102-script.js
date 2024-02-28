$(document).ready(function() {
  $("#btn_translate").click(function() {
    var languageCode = $("#language_code").val();
      const apiUrl = "https://www.fourtonfish.com/hellosalut/hello/"

      $.get(apiUrl, { lang: languageCode }, function(data) {

        $("#hello").text(data.hello);
    });
  });
});