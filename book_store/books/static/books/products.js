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
   

    if (id === 1){
     var div = document.getElementById('customalert');
    /*div.innerHTML = "<h1>✓ </h1>"+msg + "<br>"   +"<a href='../../login/test/'>Rückgängig?</a>";*/
     div.innerHTML = "<h1>✓ </h1>"+msg;
    await sleep(600);
    document.querySelector('.myalert-success').classList.add('aktiv')

    }
    if (id === 2){
      var div = document.getElementById('customalertfailed');
      div.innerHTML = "<h1>X </h1>"+msg + " ist zurzeit nicht vorhanden!";
      await sleep(600);
      document.querySelector('.myalert-failed').classList.add('aktiv')
 
      }
      if (id === 4){
        var div = document.getElementById('customalertinfo');
        div.innerHTML = "<h1>! </h1>" + " Sie haben Ihre Bücherabgaben nicht eingehalten, bitte verlängern Sie ihre Bücher oder geben Sie diese bitte zum nächstmöglichen Termin in der Bibiliothek ab";
        await sleep(600);
        document.querySelector('.myalert-info').classList.add('aktiv')
   
        }
        if (id === 5){
          var div = document.getElementById('customalertmaxbooks');
          div.innerHTML = "<h1>! </h1>" + " Sie haben Ihre maximale Anzahl an Büchern, die Sie ausleihen können erreicht.";
          await sleep(600);
          document.querySelector('.myalert-maxbooks').classList.add('aktiv')
          }
          if (id === 6){
            var div = document.getElementById('customalertfailed');
            div.innerHTML = "<h1>X </h1> Beim ausleihen von "+msg + " ist ein Problem aufgetreten bitte versuche es später noch einmal";
            await sleep(600);
            document.querySelector('.myalert-failed').classList.add('aktiv')
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