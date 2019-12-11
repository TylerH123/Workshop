var func = function(n){
  return n * 2;
}

var fib = function(n){
  if (n == 0) {
    return 0;
  }
  if (n == 1) {
    return 1;
  }
  return fib(n-1) + fib(n-2);
}

var gcd = function(a,b){
  if (b > a) {
    return gcd(b,a);
  }
  var num,i;
  for (i = 1; i < a; i++){
    if (a % i == 0 && b % i == 0){
      num = i;
    }
  }
  return num;
}

var students = ["coby","joseph","alex","tyler"]

var randomStudent = function(){
  var len = students.length;
  if (len > 1) len -= 1;
  //console.log(Math.round(Math.random() * len));
  return students[Math.round(Math.random() * len)];
}

var runFib = function(){
  var ele = document.getElementById("fib").value;
  //console.log(fib());
  //var x = fib(6);
  //console.log(x);
  console.log(fib(ele));
}

var runGcd = function(){
  var ele = document.getElementById("gcd").value;
  ele = ele.split(",");
  a = parseInt(ele[0]);
  b = parseInt(ele[1]);
  //console.log(fib());
  //var x = fib(6);
  //console.log(x);
  console.log(gcd(a,b));
}

var runRandomStudent = function(){
  var ele = document.getElementById("randomStudent").value;
  //console.log("element: " + ele);
  if (ele != "") {
    ele = ele.split(",");
    var i;
    for (i = 0; i < ele.length; i++){
      students.push(ele[i]);
    }
  }
  //console.log(fib());
  //var x = fib(6);
  //console.log(x);
  console.log(randomStudent());
}
