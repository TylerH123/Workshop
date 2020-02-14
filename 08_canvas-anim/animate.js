/*
Tyler Huang
SoftDev Pd. 2
K #08: What is it saving the screen from?
2020-02-20
*/

var c = document.getElementById("slate");
var ctx = c.getContext("2d");
ctx.fillStyle = "#6a0dad";
var id, dvdX, dvdY;
var radius = 10;
var growth = 1;
var dirX = 1;
var dirY = 1; 
var logo = new Image();
logo.src = "logo_dvd.jpg";

var clear = function(e){
	e.preventDefault();
	ctx.clearRect(0,0,c.width,c.height);
}

var growCircle = function(){
	window.cancelAnimationFrame(id);
	ctx.clearRect(0,0,c.width,c.height);
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
	id = window.requestAnimationFrame(growCircle);
}

var displayDVD = function(){
	ctx.clearRect(0,0,c.width,c.height);
	dvdX = Math.round(Math.random() * (c.width - 250) + 125); 
	dvdY = Math.round(Math.random() * (c.height - 250) + 125);
	ctx.drawImage(logo,dvdX,dvdY,50,50);
}

var animateDVD = function(){
	window.cancelAnimationFrame(id);
	ctx.clearRect(0,0,c.width,c.height);
	dvdX += dirX;
	dvdY += dirY;
	//console.log(dvdX);
	if (dvdX + 50 == c.width || dvdX + 2 == 0){
		dirX = -1 * dirX;
		//console.log(dvdX);
	}
	if (dvdY + 43 == c.height || dvdY + 7 == 0){
		dirY = -1 * dirY;
		//console.log(dvdY);
	}
	ctx.drawImage(logo,dvdX,dvdY);
	id = window.requestAnimationFrame(animateDVD);
}

var stop = function(){
	window.cancelAnimationFrame(id);
}

var stopButton = document.getElementById("stop");
stopButton.addEventListener("click", stop);

var circle = document.getElementById("animate");
circle.addEventListener("click", growCircle);

var dvd = document.getElementById("waiting");
dvd.addEventListener("click", function(e){displayDVD(); animateDVD()});