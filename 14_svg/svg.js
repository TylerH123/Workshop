//Tyler Huang
//SoftDev1 pd2
//K14: Ask Circles [Change || Die] While Moving, etc.
//2020-04-01


var pic = document.getElementById("vimage");
var wipe = document.getElementById("clear");
var animate = document.getElementById("move");

var id;
var dx = Math.floor(Math.random() * 3 - 1);
var dy = Math.floor(Math.random() * 3 - 1);
var r = 20;

var clear = function(){
  window.cancelAnimationFrame(id);
  while (pic.lastChild) {
    pic.removeChild(pic.lastChild);
  }
};

var move = function(e){
  window.cancelAnimationFrame(id);
  var children = pic.children;
  for (var i = 0; i < children.length; i++){
    cx = parseInt(children[i].getAttribute("cx"));
    cy = parseInt(children[i].getAttribute("cy"));

    if (cx - r < 0 || cx + r > pic.getAttribute("width")){
			dx = dx * -1;
		}
		if (cy - r < 0 || cy + r > pic.getAttribute("height")) {
			dy = dy * -1;
		}

    children[i].setAttribute("cx", cx + dx);
    children[i].setAttribute("cy", cy + dy);
  }
  id = window.requestAnimationFrame(move);
}

var createDot = function(e){
  if (this == e.target){
    var newDot = document.createElementNS(
      "http://www.w3.org/2000/svg", "circle");
    newDot.setAttribute("fill", "blue");
    newDot.setAttribute("cx", e.offsetX);
    newDot.setAttribute("cy", e.offsetY);
    newDot.setAttribute("r", 20);

    newDot.addEventListener("click", change);
    pic.appendChild(newDot);
  }
};

var change = function(e){
  if (this.getAttribute("fill") == "blue"){
    this.setAttribute("fill", "cyan");
  }
  else{
    this.setAttribute("cx", Math.floor(Math.random() * 501));
    this.setAttribute("cy", Math.floor(Math.random() * 501));
    this.setAttribute("fill", "blue");
  }
};

wipe.addEventListener("click", clear);
animate.addEventListener("click", move);
pic.addEventListener("click", createDot);