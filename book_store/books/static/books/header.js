


window.onload = function() {
  ismenubutton = false;
  mustclosenavbar = false;


$('body').click(function(e){
  var $elem = $(e.target);
 


  if ( ismenubutton === false ){
    if ($elem.attr('id') === 'toggle') {
        ismenubutton = true;
        mustclosenavbar = true;
    }
    }
    else{
    if ( ismenubutton === true ){
    if ($elem.attr('id') === 'toggle') {
        ismenubutton = false;
        mustclosenavbar = false;
    }
    }
    }

});



};


var myNode= document.querySelector('.hidescrollbarmenu ul'); 
myNode.addEventListener("click",function(e){    
  window.scrollTo(0, 0);
 document.querySelector('.toggle-btn__cross').click();
}); 