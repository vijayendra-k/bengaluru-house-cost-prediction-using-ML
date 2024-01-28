function completevalidate()
{
var fname =document.getElementById("firstname").value;
var lname =document.getElementById("lastname").value;
var em =document.getElementById("email_msg").value;
var pn =document.getElementById("phonenumber_msg").value;
if(fname!="" && lname!="" && em!="" && pn!="")
{
    alert("Thank You for the details!!");
    return true;
}
else
{
    alert("Please complete the form!!");
    return false;

}
}

