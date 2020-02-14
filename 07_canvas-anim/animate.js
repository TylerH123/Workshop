/*
Tyler Huang
SoftDev Pd. 2
K #07: They lock us in the tower whenever we get caught
2020-02-12
*/

var c = document.getElementById("slate");
var ctx = c.getContext("2d");
ctx.fillStyle = "#6a0dad";
var id;
var radius = 10;
var growth = 1;

var clear = function(){
	var width = c.width;
	var height = c.height;
	ctx.clearRect(0,0,width,height);
}

var animate = function(){
	window.cancelAnimationFrame(id);
	clear();
	var x = c.width / 2;
	var y = c.height / 2;
	ctx.beginPath();
	ctx.arc(x, y, radius, 0, 2 * Math.PI);
	ctx.stroke();
	ctx.fill();
	if (radius == c.width / 2){
		growth = -1;
		//console.log(growth);
	}
	else if (radius == 0){
		growth = 1;
	}
	radius += growth;
	//console.log(radius);
	id = window.requestAnimationFrame(animate);
}

var stop = function(){
	window.cancelAnimationFrame(id);
}

var stopButton = document.getElementById("stop");
stopButton.addEventListener("click", stop);

var button = document.getElementById("animate");
button.addEventListener("click", animate);