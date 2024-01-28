var locatioString = window.location.search;
alert(locatioString);
var urlSearchParam = new URLSearchParams(locatioString);
var firstName = urlSearchParam.get('First_name');alert(firstName);
var lastName = urlSearchParam.get('Last_name');alert(lastName);
var pno=urlSearchParam.get('phone');alert(pno);
var adress=urlSearchParam.get('address');alert(adress);
var mail=urlSearchParam.get('email');alert(mail);
document.getElementById("displayMessage")
const displayMessage = document.getElementById('displayMessage');

displayMessage.innerHTML =  " "+firstName+" "+lastName+" "+pno+" "+adress+" "+mail+".";