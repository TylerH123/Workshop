//Tyler Huang
//SoftDev1 pd2
//K12: Connect the Dots
//2020-03-30

var pic = document.getElementById("vimage");
var clear = document.getElementById("clean");
var prevX, prevY;

var clean = function(){
  while (pic.lastChild) {
    pic.removeChild(pic.lastChild);
  }
  prevX = null;
  prevY = null;
}

var dot = function(e){
  var c = document.createElementNS("http://www.w3.org/2000/svg","circle");
  c.setAttribute("cx",e.offsetX);
  c.setAttribute("cy",e.offsetY);
  c.setAttribute("r",10);
  c.setAttribute("fill","red");
  c.setAttribute("stroke","black");
  pic.appendChild(c);
}

var line = function(e){
  var c = document.createElementNS("http://www.w3.org/2000/svg","line");
  c.setAttribute("x1",prevX);
  c.setAttribute("y1",prevY);
  c.setAttribute("x2",e.offsetX);
  c.setAttribute("y2",e.offsetY);
  c.setAttribute("stroke","black");
  pic.appendChild(c);

  prevX = e.offsetX
  prevY = e.offsetY
}

clear.addEventListener("click", clean);

pic.addEventListener("click", function(e){
  dot(e);
  if (prevX == null){
    prevX = e.offsetX
    prevY = e.offsetY
  }
  line(e);
});