function checkform() {
    email = document.getElementById('email').value
    username = document.getElementById('username').value
    password1 = document.getElementById('password1').value
    password2 = document.getElementById('password2').value
    phone_number = document.getElementById('phone_number').value

    function validatePasswordComplexity(password) {
        let alphaRegex = /[a-zA-Z]/;
        let numericRegex = /\d/;
        return alphaRegex.test(password) && numericRegex.test(password);
    }

    if (email != email, username != '' || phone_number != '' || password1 != '' || password2 != ''){
        
    }else{
        msg.textContent = 'Fields cannot be emtpy check the fields and try again!!!'
        return false
    }
    
    if (password1.length <8){
        msg.textContent = 'Password must contain 8 characters or more'
        return false
    }else{

    }

    if (password1 != password2){
        msg.textContent = 'Passwords must be thesames'
        return false
    }

    if (!validatePasswordComplexity(password1)) {
        msg.textContent = "Password must contain alphanumerics.";
        return false;
    }

    return true
}

document.addEventListener('DOMContentLoaded', () =>{
    form = document.getElementById('signupform')
    btnMSG = document.getElementById('btnMSG')
    msg = document.getElementById('msg')

    form.addEventListener('submit', async(e)=>{
        e.preventDefault();
        alert(checkform())
        if (checkform()){
            btnMSG.textContent = 'Signing Up...'
            form.submit()
        }
    })
})