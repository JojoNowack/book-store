window.onload = function() {
	/*document.getElementById("cart123").hidden=false;*/
	/*document.getElementById("kategoriebutton").hidden=false;*/
  alertopened = false;


  var win = $(this);
  var element = document.getElementById("changeclass1");
  var element2 = document.getElementById("changeclass2")
  if (win.width() < 768) { 
      element.classList.remove("row");
      element2.classList.add("col-md-6");
      element2.classList.remove("col-md-12");
     
   
  }


  if (win.width() > 980) { 

      element.classList.add("row");
      element2.classList.remove("col-md-12");
      element2.classList.add("col-md-6");
     
    

  }

  if (win.width() < 990 && win.width() > 768) { 


      element.classList.remove("row");
      element2.classList.remove("col-md-6");
      element2.classList.add("col-md-12");
     
  
  }
}



function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
  
  
  
  async function showalert(msg,id,bookid) {
    await sleep(500);
    if (  alertopened === true){
      closealert(id);
      await sleep(1200);
      showalert(msg,id,bookid);
    }
      else{
    if (id === 1){
    var div = document.getElementById('customalert');
    div.innerHTML = "<br>"+ alertopened + "<br>"   +"<a href='cancel/?bookID="+bookid+"'>Test</a>";
    document.querySelector('.myalert-success').classList.add('aktiv')
    alertopened = true;
    }
  }
  }
  
  function closealert(id) {
    if (id === 1){
    let clearalert = document.querySelector('.myalert')
    clearalert.classList.remove('aktiv')
    alertopened = false;
    }
  }
  
  
  
  
  $(window).on('resize', function() {
    var win = $(this);
    var element = document.getElementById("changeclass1");
    var element2 = document.getElementById("changeclass2")
  
    if (win.width() < 768) { 
      if ( document.getElementById("changeclass1").classList.contains('col-md-12') )
      {
        element.classList.remove("row");
        element2.classList.add("col-md-6");
        element2.classList.remove("col-md-12");
       
      }
     
    }
  
  
    if (win.width() > 980) { 
      if ( document.getElementById("changeclass2").classList.contains('col-md-12') )
      {
        element.classList.add("row");
        element2.classList.remove("col-md-12");
        element2.classList.add("col-md-6");
       
      }
  
    }
  
    if (win.width() < 990 && win.width() > 768) { 
  
      if ( document.getElementById("changeclass1").classList.contains('row') ||  document.getElementById("changeclass2").classList.contains('col-md-6') )
      {
        element.classList.remove("row");
        element2.classList.remove("col-md-6");
        element2.classList.add("col-md-12");
       
      }
    }
  
  
    
     
  
  
  
  });