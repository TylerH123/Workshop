//Tyler Huang
//SoftDev1 pd2
//K13: Ask Circles [Change || Die]
//2020-03-31


var pic = document.getElementById("vimage");
var wipe = document.getElementById("clear");

var clear = function(){
  while (pic.lastChild) {
    pic.removeChild(pic.lastChild);
  }
}

var createDot = function(e){
  if (e.target == pic){
    var newDot = document.createElementNS(
      "http://www.w3.org/2000/svg", "circle");
    newDot.setAttribute("fill", "blue");
    newDot.setAttribute("cx", e.offsetX);
    newDot.setAttribute("cy", e.offsetY);
    newDot.setAttribute("r", 20);

    newDot.addEventListener("click", change);
    pic.appendChild(newDot);
  }
}

var change = function(e){
  if (e.target.getAttribute("fill") == "blue"){
    e.target.setAttribute("fill", "cyan");
  }
  else{
    e.target.setAttribute("cx", Math.floor(Math.random() * 501));
    e.target.setAttribute("cy", Math.floor(Math.random() * 501));
    e.target.setAttribute("fill", "blue");
  }
}

wipe.addEventListener("click", clear);
pic.addEventListener("click", createDot);