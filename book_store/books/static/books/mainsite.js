




window.onload = function() {
	/*document.getElementById("cart123").hidden=false;*/
	/*document.getElementById("kategoriebutton").hidden=false;*/
  mustclosekategorie = false;
  iskategoriebutton = false;





$('body').click(function(e){
  var $elem = $(e.target);



  if ( iskategoriebutton === false ){
  if ($elem.attr('id') === 'toggle2') {
      document.getElementById("menubutton").hidden=true
	 iskategoriebutton = true;
   mustclosekategorie = true;
  }
  }
  else{
  if ( iskategoriebutton === true ){
  if ($elem.attr('id') === 'toggle2') {
      document.getElementById("menubutton").hidden=false
	 iskategoriebutton = false;
   mustclosekategorie = false;
  }
  }
  }

});



};


var myNode= document.querySelector('.hidescrollbarmenu2 ul'); 
myNode.addEventListener("click",function(e){    
  window.scrollTo(0, 0);
 document.querySelector('.toggle2-btn__cross').click();
}); 