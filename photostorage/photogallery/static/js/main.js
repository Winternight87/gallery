//(function() {
  function initializeTooltip(dataTitle, dataDate) {
    var tooltipFrame = document.createElement("div"),
        tooltipTitle = document.createTextNode(dataTitle),
        tooltipDate = document.createTextNode(dataDate);
    
    tooltipFrame.setAttribute("id", "tooltip-frame");
    tooltipFrame.appendChild(tooltipTitle);
    tooltipFrame.appendChild(document.createElement("br"));
    tooltipFrame.appendChild(tooltipDate);
    
    document.querySelector(".content").appendChild(tooltipFrame);
    
    return tooltipFrame;
  }
  
  function showTooltip(x) {
    var tooltipDate = x.dataset.date,
        tooltipTitle = x.dataset.title;

    curTooltip = initializeTooltip(tooltipTitle, tooltipDate);
    moveTooltip(curTooltip);
  }
  
  function moveTooltip(tooltipFrame) {
    document.addEventListener('mousemove', move, false);
    function move(e) {
      tooltipFrame.style.left = e.pageX + 10 + 'px';
      tooltipFrame.style.top = e.pageY + 20 + 'px'; 
    }
  }  

  function hideTooltip() {
    var tooltipFrame = document.getElementById("tooltip-frame");
    tooltipFrame.parentNode.removeChild(tooltipFrame);
    //document.removeEventListener('mousemove', move, false);
  }

//})();

