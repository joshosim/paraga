document.addEventListener('DOMContentLoaded', ()=>{
    var error = document.getElementById('error').value
    var message_box = document.getElementById('message_box')
    var message =  document.getElementById('message')
    if (error!=''){
        message.textContent = error
        message_box.style.marginRight='0px'
    }
})