 
function validate() {
  var fn = document.forms["myForm"]["fname"].value;
  var ln = document.forms["myForm"]["lname"].value;

  if (fn == "") {
    // document.getElementById("demo").innerHTML = "Name must be filled out";
    alert("First Name must be filled out");
    // return false;
  }
   if (ln == "") {
    
    alert("Last Name must be filled out");
    
  }
//   var password = document.forms["myForm"]["psw"].value;
//   var repassword = document.forms["myForm"]["repwd"].value;
//         errors = [];
//         if (password.length < 8) {
//             errors.push("Your password must be at least 8 characters"); 
//         }
//         if (password.search(/[a-z]/i) < 0) {
//             errors.push("Your password must contain at least one letter.");
//         }
//         if (password.search(/[0-9]/) < 0) {
//             errors.push("Your password must contain at least one digit."); 
//         }
//         if (password.search(/[a-z]/) < 0) {
//             errors.push("Your password must contain at least one lowercase letter.");
//         }
//         if (password.search(/[A-Z]/) < 0)
//         {
//             errors.push("Your password must contain at least one uppercase letter.");
//         }
//         if (errors.length > 0) {
//             alert(errors.join("\n"));
//             return false;
//         }
//         return true;
//   if(password != repassword){
//     alert("Password mismatch");

//   }

  // dropdown validation
   var e = document.getElementById("dptm");
      var strUser = e.options[e.selectedIndex].value;

      var strUser1 = e.options[e.selectedIndex].text;
      if(strUser==0)
      {
          alert("Please select a Department");
         
        }
    
      
}
