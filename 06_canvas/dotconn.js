/*
Tyler Huang
SoftDev Pd. 2
K #06: Dot Dot Dot
2020-02-06
*/

// screenX gives the horizontal coordinate of the mouse pointer relative to the top left of the physical screen/monitor
// offsetX returns the x-coordinate of the mouse pointer relative to a target element
// clientX returns the x-coordinate of the mouse pointer relative to the upper left edge of the content area of the browser window
// pageX returns the x-coordinate of the mouse pointer relative to the top left of the fully rendered content area in the browser

var c = document.getElementById("slate");
var ctx = c.getContext("2d");
ctx.fillStyle = "#ff0000";
var x,y,prevX,prevY;

var clear = function(){
	var width = c.width;
	var height = c.height;
	ctx.clearRect(0,0,width,height);
	prevY = null;
	prevX = null;
}

var createDot = function(){
	x = event.offsetX;
	y = event.offsetY;
	ctx.beginPath();
	ctx.arc(x, y, 10, 0, 2 * Math.PI);
	ctx.fill();
	ctx.stroke();
}

var connectLine = function(){
	if (prevX != null && prevY != null){
		ctx.moveTo(prevX,prevY);
		ctx.lineTo(x,y);
		ctx.stroke();
		prevX = x;
		prevY = y;
		//console.log("prevX: " + prevX + " prevY: " + prevY);
	}
	else {
		//console.log("x: " + x + " y: " + y);
		prevX = x;
		prevY = y;
		//console.log("prevX: " + prevX + " prevY: " + prevY);
	}
}

var button = document.getElementById("clear");
button.addEventListener("click", clear);

c.addEventListener("click", function(e){
	createDot(),
	connectLine()
	//console.log("offsetX: " + e.offsetX),
	//console.log("clientX: " + e.clientX),
	//console.log("pageX: " + e.pageX),
	//console.log("screenX: " + e.screenX)
});