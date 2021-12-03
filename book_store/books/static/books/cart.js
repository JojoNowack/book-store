$(window).bind('beforeunload', function(){
  if ( mustclosekategorie === true){
    document.querySelector('.toggle2-btn__cross').click();
  }
  if ( mustclosenavbar === true){
    document.querySelector('.toggle-btn__cross').click();
  }
  window.scrollTo(0, 0);

});



  
   






window.onload = function() {
	/*document.getElementById("cart123").hidden=false;*/
	/*document.getElementById("kategoriebutton").hidden=false;*/
  document.getElementById("scales").value=true
  document.getElementById("scales").checked = true;
  $("#scales").prop("checked", true);
  isopen = false;
  ismenubutton = false;
  mustclosekategorie = false;
  mustclosenavbar = false;
  iskategoriebutton = false;
  alertopened = false;








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







  if ( iskategoriebutton === false ){
  if ($elem.attr('id') === 'toggle2') {
      document.getElementById("menubutton").hidden=true
	 iskategoriebutton = true;
   mustclosekategorie = true;
	 var scrolbutton = document.getElementById("kategoriebutton");
	 scrolbutton.style.position="fixed";
  }
  }
  else{
  if ( iskategoriebutton === true ){
  if ($elem.attr('id') === 'toggle2') {
      document.getElementById("menubutton").hidden=false
	 iskategoriebutton = false;
   mustclosekategorie = false;
	 var scrolbutton = document.getElementById("kategoriebutton");
	 scrolbutton.style.position="absolute";
  }
  }
  }

});



};
