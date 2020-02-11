/*
Tyler Huang
SoftDev Pd. 2
K #05: ...and I want to Paint It Better
2020-02-06
*/

// e.preventDefault() stops the default action of an element
// ctx.beginPath() starts drawing a line
// e.offsetX returns the x-coordinate of the mouse pointer relative to a target element
// e.offsetY returns the x-coordinate of the nouse pointer relative to a target element

var c = document.getElementById("slate");
var ctx = c.getContext("2d");
ctx.fillStyle = "#ff0000";
var shape = "rect";

var clear = function(){
	var width = c.width;
	var height = c.height;
	ctx.clearRect(0,0,width,height);
}

var createRect = function(){
	var x = event.offsetX;
	var y = event.offsetY;
	ctx.fillRect(x , y, 20, 40);
}

var createDot = function(){
  var x = event.offsetX;
	var y = event.offsetY;
	ctx.beginPath();
	ctx.arc(x, y, 10, 0, 2 * Math.PI);
	ctx.fill();
}

var createShape = function(){
  if (shape == "rect") {
    createRect();
  }
  else {
    createDot();
  }
}

var toggle = document.getElementById("toggle");
console.log(toggle.checked);

toggle.addEventListener("click", function(){
  console.log(toggle.isChecked);
  if (toggle.checked){
    shape = "dot";
    document.getElementById("message").innerHTML = "Now drawing dots. Toggle to switch to rectangles."
    // console.log("CHANGED TO CIRCLE");
  }
  else{
    shape = "rect";
    document.getElementById("message").innerHTML = "Now drawing rectangles. Toggle to switch to dots."
    // console.log("testing");
  }
  // console.log("toggled");
})

var button = document.getElementById("clear");
button.addEventListener("click", clear);

c.addEventListener("click", createShape);