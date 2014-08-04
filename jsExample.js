///___someJavaScriptFunction
///a: where x
///b: where y
///c: where z
function ___someJavaScriptFunction(a, b, c) {
}
/// someJavaScriptFunction 
/// a: where x
/// b: where y
/// c: where z
function someJavaScriptFunction(a, b, c) {
	hello
	someJavaScriptFunction(a, b, c);
	someJavaScriptFunction(a, b, c);
	___someJavaScriptFunction(a, b, c);
	helloWorld();
	//Type a function name here and see what happens
}

function helloWorld() {
	joe();
	someJavaScriptFunction(a, b, c);

}
