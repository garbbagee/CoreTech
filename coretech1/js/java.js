//CONSUMO API
document.addEventListener('DOMContentLoaded', function() {
    fetchCharacters();
});

function fetchCharacters() {
    fetch('https://rickandmortyapi.com/api/character')
        .then(response => response.json())
        .then(data => {
            const characters = data.results.slice(0, 6); // Obtén los primeros 6 personajes
            const cards = document.querySelectorAll('.card.custom-size');

            characters.forEach((character, index) => {
                if (cards[index]) {
                    const img = cards[index].querySelector('img');
                    const title = cards[index].querySelector('.card-title');
                    const text = cards[index].querySelector('.card-text');

                    img.src = character.image;
                    img.alt = character.name;
                    title.textContent = character.name;
                    text.textContent = `Status: ${character.status}`;
                }
            });
        })
        .catch(error => console.error('Error fetching characters:', error));
}

function aumentarCard(cardId) {
    const card = document.getElementById(cardId);
    card.style.transform = "scale(1.1)";
    card.style.transition = "transform 0.3s ease-in-out";
    card.style.boxShadow = "10px 10px 30px rgba(0, 0, 0, 0.3)";
}

function reducirCard(cardId) {
    const card = document.getElementById(cardId);
    card.style.transform = "scale(1)";
    card.style.boxShadow = "none";
}

document.addEventListener("DOMContentLoaded", function() {
    const cards = document.querySelectorAll('.card');

    cards.forEach(card => {
        card.addEventListener('mouseover', function() {
            card.style.transform = "scale(1.1)";
            card.style.transition = "transform 0.3s ease-in-out";
            card.style.boxShadow = "10px 10px 30px rgba(0, 0, 0, 0.3)";
        });

        card.addEventListener('mouseout', function() {
            card.style.transform = "scale(1)";
            card.style.boxShadow = "none";
        });
    });
});

//H1 Slider

const marcasHeading = document.querySelector('.marcas');

marcasHeading.addEventListener('mouseover', () => {
  marcasHeading.style.transform = 'scale(1.1)'; // Aumenta el tamaño en un 20%
});

marcasHeading.addEventListener('mouseout', () => {
  marcasHeading.style.transform = 'scale(1)'; // Restaura el tamaño original
});


// animacion






// Inicializar todas las animaciones
function initAnimations() {
    if (document.getElementById('loader')) {
        pageLoader();
    }
    scrollAnimations();
    buttonHoverAnimations();
    menuAnimations();
}

// Inicializar animaciones al cargar la página
window.addEventListener('load', initAnimations);


/* ANIMACION DE INICIO DE SESION Y REGISTRO*/
const btnSignIn = document.getElementById("sign-in"),
      btnSignUp = document.getElementById("sign-up");
      formRegister = document.querySelector(".register"),
      formLogin = document.querySelector(".login");

btnSignIn.addEventListener("click", e => {
    formRegister.classList.add("hide");
    formLogin.classList.remove("hide");
    document.getElementById("correo2").value = "";
    document.getElementById("contra2").value = "";
})

btnSignUp.addEventListener("click", e => {
    formLogin.classList.add("hide");
    formRegister.classList.remove("hide");
    document.getElementById("nombre").value = "";
    document.getElementById("user").value = "";
    document.getElementById("fono").value = "";
    document.getElementById("correo").value = "";
    document.getElementById("contra").value = ""
})/* FIN ANIMACION*/


/* VALIDACIONES REGISTRARSE*/

/* INICIO VALIDACION NOMBRE*/
document.getElementById("nombre").addEventListener("blur", function() {
    validarNombre(this.value);
});
function validarNombre(){
    var nombre = document.getElementById("nombre").value;
    var regex = /^[a-zA-Z\s]{0,150}$/;
    if(regex.test(nombre)){
        cantidad = document.getElementById("nombre").value.length;
        valor = document.getElementById("nombre").value;

        if(cantidad == 0){
            Swal.fire({
                icon: "error",
                title: "Nombre sin datos",
                text: "Ingrese su nombre completo"
            });
        }
    }else {
        Swal.fire({
            icon: "error",
            title: "Nombre no valido",
            text: "Solo se permiten letras"
        });
        return false;
    }return true;
}/* FIN VALIDACION NOMBRE */

/* VALIDAR USUARIO */
document.getElementById("user").addEventListener("blur", function() {
    validarUsuario(this.value);
});
function validarUsuario(){
    var user = document.getElementById("user").value;
    var regex = /^[a-zA-Z0-9_-\s]{0,50}$/;
    if (regex.test(user)){
        cantidad = document.getElementById("user").value.length;
        valor = document.getElementById("user").value;

        if(cantidad == 0){
            Swal.fire({
                icon: "error",
                title: "Usuario sin datos",
                text: "Ingrese un usuario"
            });
        }
    } else {
        Swal.fire({
            icon: "error",
            title: "Usuario no valido",
            text: "Solo se permiten letras, numeros, puntos, guion y guion bajos."
        });
        return false;
    }return true;
}/* FIN VALIDACION USUARIO */

/* VALIDACION DE TELEFONO */
document.getElementById("fono").addEventListener("blur", function() {
    validarNumeros(this.value);
});
function validarNumeros(){
    var fono = document.getElementById("fono").value;
    var regex = /^[0-9]{0,}$/;

    if(regex.test(fono)){
        cantidad = document.getElementById("fono").value.length;
        valor = document.getElementById("fono").value;
        
        if(cantidad < 9 || cantidad > 9){
            Swal.fire({
                icon: "error",
                title: "Teléfono invalido",
                text: "El número debe ser de 9 digitos (añadir el 9)"
            });
            return false;
        }

        if(cantidad == 0){
            Swal.fire({
                icon: "error",
                title: "Teléfono sin datos...",
                text: "Por favor introduzca un numero de telefono"
            });
            return false;
        }
    }else{
        Swal.fire({
            icon: "error",
            title: "Teléfono invalido",
            text: "solo se permiten números"
        });
        return false;
    }return true;
}/* FIN VALIDACION TELEFONO */

/* VALIDACION CORREO*/
document.getElementById("correo").addEventListener("blur", function() {
    validarCorreo(this.value);
});
function validarCorreo(){
    cantidad = document.getElementById("correo").value.length;
    valor = document.getElementById("correo").value;

    if(cantidad == 0){
        Swal.fire({
            icon: "error",
            title: "Correo Eléctronico sin datos...",
            text: "Por favor introduzca un Correo Eléctronico"
        });
        return false;
    }else{
        var correo = document.getElementById("correo").value;
        var regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

        if(regex.test(correo)){
            if(correo == "mart.rozas@duocuc.cl"){
                Swal.fire({
                    icon: "error",
                    title: "Correo Eléctronico ya existe",
                    text: "Ingrese otro correo"
                });
                return false;
            }
        }else{
            Swal.fire({
                icon: "error",
                title: "Correo Eléctronico no valido",
                text: "Ingrese un correo valido ej: damianpizarro@gmail.com"
            });
            return false;
        }
    }return true;
}/* FIN VALIDACION CORREO */

/* VALIDACION CONTRASEÑA*/
function validarContraseña(){
    cantidad = document.getElementById("contra").value.length;
    valor = document.getElementById("contra").value;

    if(cantidad == 0){
        Swal.fire({
            icon: "error",
            title: "Contraseña sin datos...",
            text: "Ingrese una contraseña válida"
        });
        return false;
    }else{
        var contra = document.getElementById("contra").value;
        var regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^a-zA-Z\d\s])[a-zA-Z\d\S]{8,}$/;

        if(regex.test(contra)){
        }else{
            Swal.fire({
                icon: "error",
                title: "Contraseña no valida",
                text: "Requiere minimo 8 digitos, al menos una letra minúscula, una letra mayúscula, un número y un signo especial"
            });
            return false;
        }
    }return true;
}/* FIN VALIDACION CONTRASEÑA */ 

/* MOSTRAR CONTRASEÑA */
var eye = document.getElementById("eye");
var contra = document.getElementById("contra");
eye.addEventListener("click", function(){
    if(contra.type == "password"){
        contra.type = "text"
        eye.className = 'idolo bx bx-show'
    }else{
        contra.type = "password"
        eye.className = 'idolo bx bx-low-vision'
    }
})

/* VALIDACION REGISTRO*/
document.getElementById("miFormulario").addEventListener("submit", function(event) {
    event.preventDefault(); // Evita que el formulario se envíe automáticamente
    
    var nombre = document.getElementById("nombre").value;
    var usuario = document.getElementById("user").value;
    var fono = document.getElementById("fono").value;
    var correo = document.getElementById("correo").value;
    var contra = document.getElementById("contra").value;
    var validacionesExitosas = 0;

    if (nombre.trim() == '' || usuario.trim() == '' || fono.trim() == '' || correo.trim() == '' || contra.trim() == '') {
        // Si el nombre, Usuario, Fono, Correo o contraseña están vacíos, muestra un mensaje de error
        Swal.fire({
            icon: "error",
            title: "Formulario no válido...",
            text: "Ingrese todos los datos"
        });

    }else{ // Si el formulario está completo, validara que si esten correctos
        if (validarNombre()) validacionesExitosas++;
        if (validarUsuario()) validacionesExitosas++;
        if (validarNumeros()) validacionesExitosas++;
        if (validarCorreo()) validacionesExitosas++;
        if (validarContraseña()) validacionesExitosas++;
        // Verificar si todas las validaciones fueron exitosas
        if (validacionesExitosas === 5) {
            // Si todas las validaciones son exitosas, muestra un mensaje de éxito
            Swal.fire({
                icon: "success",
                title: "Formulario válido",
                text: "¡El formulario ha sido validado correctamente!"
            });

            document.getElementById("nombre").value = "";
            document.getElementById("user").value = "";
            document.getElementById("fono").value = "";
            document.getElementById("correo").value = "";
            document.getElementById("contra").value = "";
        }   
    };
}
);/* FIN VALIDACION REGISTRO */

/* TERMINO DE VALIDACIONES REGISTRARSE */


/* INICIO VALIDACIONES INICIO SESION */

/* VALIDACION CORREO INCIO SESION*/
document.getElementById("correo2").addEventListener("blur", function() {
    validarCorreo2(this.value);
});
function validarCorreo2(){
    cantidad = document.getElementById("correo2").value.length;
    valor = document.getElementById("correo2").value;

    if(cantidad == 0){
        Swal.fire({
            icon: "error",
            title: "Correo Eléctronico sin datos...",
            text: "Por favor introduzca un Correo Eléctronico"
        });
    }else{
        var correo2 = document.getElementById("correo2").value;
        var regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

        if(regex.test(correo2)){
        }else{
            Swal.fire({
                icon: "error",
                title: "Correo Eléctronico no valido",
                text: "Ingrese un correo valido ej: damianpizarro@gmail.com"
            });
        }
    }
}/* FIN VALIDACION CORREO */ 

/* VALIDACION DE CONTRASEÑA */
document.getElementById("contra2").addEventListener("blur", function() {
    validarContraseña2(this.value);
});
function validarContraseña2(){
    cantidad = document.getElementById("contra2").value.length;
    valor = document.getElementById("contra2").value;

    if(cantidad == 0){
        Swal.fire({
            icon: "error",
            title: "Contraseña sin datos...",
            text: "Ingrese una contraseña válida"
        });
    }else{
        var contra2 = document.getElementById("contra2").value;
        var regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^a-zA-Z\d\s])[a-zA-Z\d\S]{8,}$/;

        if(regex.test(contra2)){
        }else{
            Swal.fire({
                icon: "error",
                title: "Contraseña no valida",
                text: "Requiere al menos una letra minúscula, una letra mayúscula, un número y un signo especial"
            });
        }
    }
}


/* INICIO VALIDACION CORREO VALIDO*/
document.getElementById("total").addEventListener("submit", function(event) {
    event.preventDefault(); // Evita que el formulario se envíe automáticamente
    
    cantidadC = document.getElementById("correo2").value.length;
    cantidadPass = document.getElementById("contra2").value.length;
    


    if(cantidadC == 0 || cantidadPass == 0){
        Swal.fire({
            icon: "error",
            title: "Inicio Sesión sin datos...",
            text: "Ingrese Correo Eléctronico o Usuario y Contraseña"
        });
    }else{
        var correo2 = document.getElementById("correo2").value;
        var contra2 = document.getElementById("contra2").value;

        if(correo2 == "mart.rozas@duocuc.cl" && contra2 == "M4rtin_123"){
            Swal.fire({
                position: "center",
                icon: "success",
                title: "Inicio Sesión con exito!",
                showConfirmButton: false,
                timer: 1500
            })

            document.getElementById("correo2").value = "";
            document.getElementById("contra2").value = "";
        }else{
            Swal.fire({
                icon: "error",
                title: "Correo Eléctronico o Contraseña incorrecto",
                text: "Intente Otra Vez"
            });
        }
    }
}
);/* FIN VALIDACION INICIO DE SESION VALIDO */
document.addEventListener('DOMContentLoaded', function() {
  document.body.classList.add('fade-in');
});
