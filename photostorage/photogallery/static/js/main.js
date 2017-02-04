var popup = document.getElementsByClassName('popup-frame');

document.addEventListener('mousemove', fn, false);


function fn(e) {
  
  for (var i=popup.length; i--;) {
    popup[i].style.left = e.pageX + 10 + 'px';
    popup[i].style.top = e.pageY + 20 + 'px';    
  }

}

