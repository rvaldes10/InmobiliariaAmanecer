///^[0-9]+.{1,2}[0-9]+.{3}[0-9]+.{3}[0-9]$/

const formulario = document.getElementById('formulario')

const inputs = document.querySelectorAll('#formulario input')

const expresiones = {
	
    nombre: /^[a-z A-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
    apellido: /^[a-z A-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
    mail: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
    telefono: /^\d{1,14}$/, // 1 a 14 numeros.
}

const campos = {

    nombre:false,
    apellido:false,
    mail:false,
    telefono:false

}

const validarFormulario = (e) => {

    switch (e.target.name) {
        case "nombre":

            validarCampo(expresiones.nombre,e.target, 'nombre')

            break;
        
        case "apellido":

            validarCampo(expresiones.apellido,e.target, 'apellido')

        case "mail":

            validarCampo(expresiones.mail,e.target, 'mail')
            
            break;
        case "telefono":

            validarCampo(expresiones.telefono,e.target, 'telefono')
            
            break;
    
    }

};

const validarCampo = (expresion, input, campo) =>{

    if (expresion.test(input.value)) {

        document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-incorrecto');
        document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-correcto');
        document.querySelector(`#grupo__${campo} i`).classList.add('fa-check-circle')
        document.querySelector(`#grupo__${campo} i`).classList.remove('fa-times-circle')
        document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.remove('formulario__input-error-activo')
        campos[campo] = true;
        
    } else {
        
        document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-incorrecto');
        document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-correcto');
        document.querySelector(`#grupo__${campo} i`).classList.remove('fa-check-circle');
        document.querySelector(`#grupo__${campo} i`).classList.add('fa-times-circle');
        document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.add('formulario__input-error-activo')
        campos[campo] = false;

    }

};

inputs.forEach((input) =>{

    input.addEventListener('keyup', validarFormulario);

});

formulario.addEventListener('submit', (e)  => {

    e.preventDefault();

    if (campos.nombre && campos.apellido && campos.mail && campos.telefono) {
        
        formulario.reset();

        document.getElementById('formulario__mensaje-exito').classList.add('formulario__mensaje-exito-activo')
        setTimeout(() => {
            document.getElementById('formulario__mensaje-exito').classList.remove('formulario__mensaje-exito-activo')
        }, 3000);


    }else{

        document.getElementById('formulario__mensaje').classList.add('formulario__mensaje-activo')

        setTimeout(() => {
            
            document.getElementById('formulario__mensaje').classList.remove('formulario__mensaje-activo')

        }, 5000);

    }

});
