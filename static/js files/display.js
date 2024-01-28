var locatioString = window.location.search;
var urlSearchParam = new URLSearchParams(locatioString);
var firstName = urlSearchParam.get('First_name');
var lastName = urlSearchParam.get('Last_name');

if (firstName !== null && lastName !== null) {
    const succeeMessage = document.getElementById('succeeMessage');
    succeeMessage.innerHTML = "Welcome " + firstName + " " + lastName + "!!";
} else {
    console.error("Error: Both first name and last name are required.");
}
