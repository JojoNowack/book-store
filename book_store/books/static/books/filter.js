
function suchfensteroeffnen() {
  document.querySelector('.container-filter').classList.add('aktiv')
}

function suchfensterschließen() {
  let divfilter = document.querySelector('.container-filter')

  divfilter.classList.remove('aktiv')
}

// register the handler 

document.addEventListener('keyup', doc_keyUp, false);

// define a handler
function doc_keyUp(e) {

  // this would test for whichever key is 40 (down arrow) and the ctrl key at the same time
  if (e.ctrlKey && e.key === 'ArrowDown' ) {
    suchfensteroeffnen();
  }

  if (e.ctrlKey && e.key === 'ArrowUp' ) {
    suchfensterschließen();
  }
}