const field = document.querySelector('[name="room_code"]');

field.addEventListener('keypress', function ( event ) {  
   let key = event.keyCode;
    if (key === 32) {
      event.preventDefault();
    }
});