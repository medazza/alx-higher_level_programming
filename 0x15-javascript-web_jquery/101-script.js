$(document).ready(function () {
    let count = 1;
  
    $('#add_item').click(function () {
      const nwItem = $('<li>Item ' + count + '</li>');
      $('ul.my_list').append(nwItem);
      count++;
    });
  
    $('#remove_item').click(function () {
      $('ul.my_list li:last-child').remove();
    });
  
    $('#clear_list').click(function () {
      $('ul.my_list').empty();
    });
  });