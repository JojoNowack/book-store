/*Copyright (c) 2021 by Mathew Sachin (https://codepen.io/MathewSachin/pen/LxPzob)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
*/

function htmlEncode (value){
  return $('<div/>').text(value).html();
}

$(function() {
  
});

window.onload = async function() {
        var div = document.getElementById('qrcontent');
          $(".qr-code").attr("src", "https://chart.googleapis.com/chart?cht=qr&chl="+div.value+"&chs=220x220&chld=L|0");
          var element = document.getElementById("loaderdiv");
          await sleep(200);
         

};

$( document ).ready(function() {
  element.classList.remove("loader");
});

$(document).ready(function() {
  // messages timeout for 10 sec 
  setTimeout(function() {
      $('.message').fadeOut('slow');
  }, 5000); // <-- time in milliseconds, 1000 =  1 sec
 
});

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}