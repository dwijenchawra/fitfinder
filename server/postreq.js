


var XMLHttpRequest = require('xhr2');
var xhr = new XMLHttpRequest();
xhr.open("POST", "http://127.0.0.1:5000/testRoute", true);
xhr.setRequestHeader('Content-Type', 'application/json');
xhr.send(JSON.stringify({
    info: "this is the information"
}));