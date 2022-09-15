function dsHandler(e){
    e.dataTransfer.setData("elem",e.target.id);
}

function doHandler(e){
    e.preventDefault();
}

function dpHandler(e){
    e.preventDefault();
    var elId = e.dataTransfer.getData("elem");
    e.target.appendChild(document.getElementById(elId));
}

var showPrompt = function(){
    var resCont = document.querySelectorAll(".forpromp p");
    var res = "";
    for (let m of resCont){
        res+=(m.textContent+", ");
    }
    alert("Name : " + document.getElementById('managerName').value + "\n" +
    "Email: " + document.getElementById('groupEmail').value + "\n" + 
    "Username : " + document.getElementById('serverUsername').value + "\n" + 
    "Team Lead : " + document.getElementById('teamLead').value + "\n" +
    "Team Members : " + res);
};
var check = function() {
    if (document.getElementById('serverPassword').value !=
        document.getElementById('confirmPassword').value) {
        document.getElementById('message').style.color = 'red';
        document.getElementById('message').innerHTML = '    Not Matching';
    }else{
        document.getElementById('message').innerHTML = '';
    }
};
var checkUsername = function() {
    var usrname = document.getElementById('serverUsername').value;
    if (/[A-Z]/.test(usrname) && /[0-9]/.test(usrname)){
        document.getElementById('messageUsername').style.color = 'green';
        document.getElementById('messageUsername').innerHTML = 'Valid Username';
    }else{
        document.getElementById('messageUsername').style.color = 'red';
        document.getElementById('messageUsername').innerHTML = 'Username Invalid';
    }
};
document.addEventListener ("keydown", function (zEvent) {
    if (zEvent.ctrlKey  &&  zEvent.key === "m") {  
        var element = document.body;
        element.classList.toggle("dark-mode");
    }
});

