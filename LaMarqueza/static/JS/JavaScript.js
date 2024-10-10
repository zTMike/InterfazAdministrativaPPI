function toggleHeart(button) {
    button.classList.toggle('btn-danger');
    button.classList.toggle('btn-outline-danger');
}
document.addEventListener('DOMContentLoaded', function () {

    


    
    const cantidadInputs = document.getElementsByClassName('cantidad');
    const cantidadErrors = document.getElementsByClassName('cantidadError');
    const agregarButtons = document.getElementsByClassName('Agregar');
    const resenaInputs = document.getElementsByClassName('resena');
    const resenaErrors = document.getElementsByClassName('resenaError');
    const enviarResenaButtons = document.getElementsByClassName('EnviarResena');

    const palabrasProhibidas = [
        // Español
        'coño', 'hijueputa', 'hp', 'HP', 'Hp', 'gonorrea', 'pendejo', 'maricón', 'zorra', 'puta', 'cabron', 'hijaputa', 'mierda',
        'chingar', 'estúpido', 'imbécil', 'gilipollas', 'hijo de puta', 'tonto', 'puta', 'cabrón', 'cagón',
        'pelotudo', 'polla', 'pito', 'choto', 'bastardo', 'mamón', 'asqueroso', 'carajo', 'vulgar',
        'trapo', 'mamarracho', 'borracho', 'golfo', 'soplón', 'patán', 'rata', 'culero', 'fufurufa',
        'maraca', 'mierdero', 'guarro', 'chabacano', 'cínico', 'necio', 'bufón', 'gordo', 'lechón',
        'teta', 'pito', 'trasero', 'cogido', 'churro', 'zangolote', 'culo', 'picha', 'borracho',
        'pachucho', 'rufián', 'codo', 'ventoso', 'chafaldrana', 'bacalao', 'pijo', 'pelao', 'mocho',
        'petardo', 'trapero', 'marrajo', 'chopas', 'chulo', 'potro', 'peluso', 'mamón', 'falso', 'rufián',
        'grano', 'cerdo', 'cochina', 'tonto', 'perra', 'chancho', 'chiflado', 'pelota', 'chueco', 'pepo',
        'fofo', 'cuchitril', 'desgraciado', 'sarnoso', 'carrero', 'juerguista', 'mocoso', 'vago', 'tacaño',

        // Inglés
        'fuck', 'shit', 'bitch', 'cunt', 'dick', 'pussy', 'asshole', 'motherfucker', 'nigga', 'slut',
        'whore', 'cock', 'prick', 'twat', 'wanker', 'faggot', 'retard', 'bastard', 'cocksucker',
        'cunt', 'douchebag', 'fistfuck', 'gook', 'homo', 'jizz', 'kike', 'mothafucka', 'nappy',
        'nigger', 'pikey', 'piss', 'poof', 'pube', 'raghead', 'skank', 'slapper', 'tart', 'tramp',
        'turd', 'wop', 'arsehole', 'tosser', 'chav', 'clit', 'dumbass', 'eggplant', 'fuckwit',
        'gobshite', 'hellhound', 'knobhead', 'minger', 'minge', 'mofo', 'numpty', 'plonker', 'prat',
        'scrote', 'skite', 'smeghead', 'spastic', 'spunk', 'tit', 'wank', 'wanker', 'yobbo', 'yummy',
        'knob', 'butt', 'crap', 'crappy', 'shag', 'shithead', 'stupid', 'tit', 'tosser', 'arse',
        'bitch', 'boob', 'brat', 'idiot', 'imbecile'
    ];

    const caracteresEspeciales = /[%*#()&^@?/<>"']/;

    // Deshabilitar todos los botones al inicio
    Array.from(agregarButtons).forEach(button => button.disabled = true);
    Array.from(enviarResenaButtons).forEach(button => button.disabled = true);

    Array.from(cantidadInputs).forEach((cantidadInput, index) => {
        const cantidadError = cantidadErrors[index];
        const agregarButton = agregarButtons[index];

        cantidadInput.addEventListener('input', function () {
            const value = cantidadInput.value;
            const sanitizedValue = value.replace(/[^0-9]/g, '');

            // Si el valor contiene caracteres no permitidos, es menor que 1, está vacío o supera los 9 caracteres, mostrar mensaje de error
            if (sanitizedValue !== value || parseInt(sanitizedValue) < 1 || sanitizedValue === '' || sanitizedValue.length > 9) {
                cantidadInput.value = sanitizedValue ? sanitizedValue : '';
                cantidadError.textContent = 'Por favor, ingrese un número positivo de hasta 9 dígitos.';
                cantidadError.style.display = 'block';
                agregarButton.disabled = true;
            } else {
                cantidadError.style.display = 'none';
                agregarButton.disabled = false;
            }
        });
    });

    Array.from(resenaInputs).forEach((resenaInput, index) => {
        const resenaError = resenaErrors[index];
        const enviarResenaButton = enviarResenaButtons[index];

        resenaInput.addEventListener('input', function () {
            const value = resenaInput.value.toLowerCase();
            let esValido = true;

            // Verificar si contiene caracteres especiales
            if (caracteresEspeciales.test(value)) {
                esValido = false;
            }

            // Verificar si contiene palabras prohibidas
            for (const palabra of palabrasProhibidas) {
                if (value.includes(palabra)) {
                    esValido = false;
                    break;
                }
            }

            // Verificar la longitud de la reseña
            if (value.length < 2 || value.length > 255) {
                esValido = false;
            }

            // Mostrar mensaje de error si la entrada no es válida
            if (!esValido) {
                resenaError.textContent = 'La reseña no apta para publicarse.';
                resenaError.style.display = 'block';
                enviarResenaButton.disabled = true;
            } else {
                resenaError.style.display = 'none';
                enviarResenaButton.disabled = false;
            }
        });
    });


//------------------Validacion de datos de usuario------------------
       const form = document.querySelector('form');
    const idInput = document.getElementById('id_usuario_usu');
    const nombreInput = document.getElementById('nombre_usu');
    const apellidoInput = document.getElementById('apellido_usu');
    const correoInput = document.getElementById('correo_usu');
    const telefonoInput = document.getElementById('telefono_usu');
    const passwordInput = document.getElementById('password_usu');
    const submitButton = document.querySelector('input[type="submit"]');

    function validateForm() {
        let isValid = true;

        // Validar ID
        const idValue = idInput.value.trim();
        const idError = document.getElementById('idError');
        if (!/^\d{7,10}$/.test(idValue) || idValue.includes(' ') || parseInt(idValue) < 0) {
            isValid = false;
            idError.textContent = 'ID inválido. Debe ser un número entre 7 y 10 dígitos, sin espacios ni caracteres especiales.';
            idError.style.display = 'block';
        } else {
            idError.textContent = '';
            idError.style.display = 'none';
        }

        // Validar Nombre
        const nombreValue = nombreInput.value.trim();
        const nombreError = document.getElementById('nombreError');
        if (!/^[a-zA-Z\s]{1,50}$/.test(nombreValue)) {
            isValid = false;
            nombreError.textContent = 'Nombre inválido. No debe contener números, caracteres especiales, y debe tener menos de 50 caracteres.';
            nombreError.style.display = 'block';
        } else {
            nombreError.textContent = '';
            nombreError.style.display = 'none';
        }

        // Validar Apellido
        const apellidoValue = apellidoInput.value.trim();
        const apellidoError = document.getElementById('apellidoError');
        if (!/^[a-zA-Z\s]{1,50}$/.test(apellidoValue)) {
            isValid = false;
            apellidoError.textContent = 'Apellido inválido. No debe contener números, caracteres especiales, y debe tener menos de 50 caracteres.';
            apellidoError.style.display = 'block';
        } else {
            apellidoError.textContent = '';
            apellidoError.style.display = 'none';
        }

        // Validar Correo
        const correoValue = correoInput.value.trim();
        const correoError = document.getElementById('correoError');
        if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(correoValue) || correoValue.length > 50) {
            isValid = false;
            correoError.textContent = 'Correo inválido. Debe ser un correo válido y tener menos de 50 caracteres.';
            correoError.style.display = 'block';
        } else {
            correoError.textContent = '';
            correoError.style.display = 'none';
        }

        // Validar Teléfono
        const telefonoValue = telefonoInput.value.trim();
        const telefonoError = document.getElementById('telefonoError');
        if (!/^\d{7,15}$/.test(telefonoValue) || telefonoValue.includes(' ') || parseInt(telefonoValue) < 0) {
            isValid = false;
            telefonoError.textContent = 'Teléfono inválido. Debe ser un número entre 7 y 15 dígitos, sin espacios ni caracteres especiales.';
            telefonoError.style.display = 'block';
        } else {
            telefonoError.textContent = '';
            telefonoError.style.display = 'none';
        }

        // Validar Contraseña
        const passwordValue = passwordInput.value.trim();
        const passwordError = document.getElementById('passwordError');
        if (passwordValue.length < 7 || /[^\w\s]/.test(passwordValue) || passwordValue.includes(' ')) {
            isValid = false;
            passwordError.textContent = 'Contraseña inválida. Debe tener al menos 7 caracteres, sin caracteres especiales ni espacios.';
            passwordError.style.display = 'block';
        } else {
            passwordError.textContent = '';
            passwordError.style.display = 'none';
        }

        submitButton.disabled = !isValid;
    }

    // Añadir eventos de entrada para validar en tiempo real
    idInput.addEventListener('input', validateForm);
    nombreInput.addEventListener('input', validateForm);
    apellidoInput.addEventListener('input', validateForm);
    correoInput.addEventListener('input', validateForm);
    telefonoInput.addEventListener('input', validateForm);
    passwordInput.addEventListener('input', validateForm);

    // Validar el formulario al cargar la página
    validateForm();
});
