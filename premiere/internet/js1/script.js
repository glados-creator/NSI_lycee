var error = false
var typ = undefined

function clean(){
    console.log("clean")
    document.getElementById("s").innerHTML = "";
    document.getElementById("error").innerHTML = "";
    return;
}

function s(){
    console.log("s")
    if (!error){
    var title = document.createElement("h1");
    title.innerHTML = "SUCCESS";
    document.getElementById("s").appendChild(title);
    return true}
}

function fail(){
    console.log("fail " + error)
    if (!error){
    error = true;
    var title = document.createElement("h1");
    title.style="color: red;";
    title.innerHTML = "failed to enter correct " + typ;
    document.getElementById("error").appendChild(title);
    //thisFunctionDoesNotExistAndWasCreatedWithTheOnlyPurposeOfStopJavascriptExecutionOfAllTypesIncludingCatchAndAnyArbitraryWeirdScenario();
    throw 'stop'}
}

function get(){
    console.log("get")
    error = false;
    clean();
console.log("sexh"+document.getElementById("sexh").checked);
console.log("sexf"+document.getElementById("sexf").checked);
if (!document.getElementById("sexh").checked && !document.getElementById("sexf").checked){console.log("sex fail");typ = "sex"; fail();} // check a sex is selected

console.log(document.getElementById("name").value);
if (!document.getElementById("name").value){console.log("name fail");typ = "name";fail();} // check a name is enter

console.log(document.getElementById("age").value);
if (document.getElementById("age").value > 25 || document.getElementById("age").value < 18){console.log("age fail");typ = "age";fail();}} // check age