function htmlEncode (value){
  return $('<div/>').text(value).html();
}

$(function() {
  
});

window.onload = function() {
        var div = document.getElementById('qrcontent');
          $(".qr-code").attr("src", "https://chart.googleapis.com/chart?cht=qr&chl=" + htmlEncode($("#qrcontent").val()) + "&chs=220x220&chld=L|0");

        
        
};


$(document).ready(function() {
  // messages timeout for 10 sec 
  setTimeout(function() {
      $('.message').fadeOut('slow');
  }, 5000); // <-- time in milliseconds, 1000 =  1 sec
 
});

