function showTooltip(x) {
  Tooltip = x.childNodes[1];
  document.addEventListener('mousemove', fn, false);
  
  function fn(e) {
    Tooltip.style.left = e.pageX + 10 + 'px';
    Tooltip.style.top = e.pageY + 20 + 'px'; 
  }
  
}