var c = document.getElementById("slate");
var ctx = c.getContext("2d");
ctx.fillStyle = "#ff0000";
	
var clear = function(){
	var width = c.width;
	var height = c.height;
	ctx.clearRect(0,0,width,height);
}

var createRect = function(){
	var x = event.clientX;
	var y = event.clientY;
	ctx.fillRect(x , y, 100, 200);
}

var button = document.getElementById("clear");
button.addEventListener("click", clear);
c.addEventListener("click", createRect)