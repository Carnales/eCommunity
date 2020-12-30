function checkUser()
{
    if (user === 'AnonymousUser')
        document.getElementById("user").innerHTML = "You are not logged in";
    else
        document.getElementById("user").innerHTML = "Hello, " + user;
}
