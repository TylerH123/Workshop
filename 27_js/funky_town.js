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
  else {
    return fib(n-1) + fib(n-2);
  }
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
