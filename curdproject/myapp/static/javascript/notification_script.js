const notification = document.getElementById('notification');


if(notification){
    // Automatically hide the notification after 2 seconds
    setTimeout(hideNotification, 2000);
    function hideNotification() {
       notification.classList.remove('show');
    }
    document.getElementById('close-btn').addEventListener('click', hideNotification);

}


































// try{
//     const messages = document.getElementById('messages');

//     messages.value
//     notification.classList.add('show');

//     // Automatically hide the notification after 2 seconds
//     setTimeout(hideNotification, 2000);


//     function hideNotification() {
//         const notification = document.getElementById('notification');
//         notification.classList.remove('show');
//     }

//     document.getElementById('close-btn').addEventListener('click', hideNotification);
// }
// catch(e){

// }

