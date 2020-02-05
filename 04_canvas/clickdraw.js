var c = document.getElementById("slate");
//console.log(c);
var ctx = c.getContext("2d");
//console.log(ctx);
ctx.fillStyle = "#ff0000";
ctx.fillRect(50 , 50, 100, 200);
//console.log(ctx);
	
var clear = function(){
	var c = document.getElementById("slate");
	var ctx = c.getContext("2d");
	var width = c.width;
	var height = c.height;
	ctx.clearRect(0,0,width,height);
}

var button = document.getElementById("clear");
button.addEventListener("click", clear);