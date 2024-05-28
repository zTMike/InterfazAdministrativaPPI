document.getElementById('togglePassword').addEventListener('click', function () {
    var passwordInput = document.getElementById('password');
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
    } else {
        passwordInput.type = 'password';
    }
});



document.getElementById('Cerrar').addEventListener('click', function () {
    var passwordInput = document.getElementById('password');
    passwordInput.type = 'password';
    // Obtén todos los campos de entrada del formulario
    var inputs = document.getElementsByTagName('input');

    // Recorre todos los campos de entrada y establece su valor en una cadena vacía
    for (var i = 0; i < inputs.length; i++) {
        inputs[i].value = '';
    }
    
});


