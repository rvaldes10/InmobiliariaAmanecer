///^[0-9]+.{1,2}[0-9]+.{3}[0-9]+.{3}[0-9]$/

const expresiones = {
	
    nombreCompleto: /^[a-z A-ZÀ-ÿ\s]{1,50}$/, // Letras y espacios, pueden llevar acentos.
    //apellido: /^[a-z A-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
    mail: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
    telefono: /^\d{1,14}$/, // 1 a 14 numeros.
}

const campos = {

    nombreCompleto:true,
    mail:true,
    telefono:true

}

formulario.addEventListener('submit', (e)  => {

    e.preventDefault();

    if (campos.nombreCompleto && campos.mail && campos.telefono) {
        
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
