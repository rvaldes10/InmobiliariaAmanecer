var imagenes = ['Inmo_Amanecer/static/Imgs/Galeria/img1.jpg','Inmo_Amanecer/staticImgs/Galeria/img2.jpg','Inmo_Amanecer/staticImgs/Galeria/img3.jpg','Inmo_Amanecer/staticImgs/Galeria/img4.jpg','Inmo_Amanecer/staticImgs/Galeria/img5.jpg','Inmo_Amanecer/staticImgs/Galeria/img6.jpg','Imgs/Galeria/img7.jpg','Imgs/Galeria/img8.jpg','Imgs/Galeria/img9.jpg','Imgs/Galeria/img10.jpg','Imgs/Galeria/img11.jpg','Imgs/Galeria/img12.jpg','Imgs/Galeria/img13.jpg','Imgs/Galeria/img14.jpg'],
cont = 0;

function carrousel(Galeria) {

    Galeria.addEventListener('click', e => {

        let retroceder = Galeria.querySelector('.retroceder'),
            avanzar = Galeria.querySelector('.avanzar'),
            img = Galeria.querySelector('img'),
            tgt = e.target;

        if(tgt == retroceder){

            if(cont > 0){

                img.src = imagenes[cont -1];
                cont --;

            }else{

                img.src = imagenes[imagenes.length -1 ];
                cont = imagenes.length -1;

            }

        }else if (tgt == avanzar) {

            if(cont < imagenes.length - 1){

                img.src = imagenes[cont + 1];
                cont ++;

            }else{

                img.src = imagenes[0];
                cont = 0;

            }
            
        }

    });

}

document.addEventListener("DOMContentLoaded",() => {

    let Galeria = document.querySelector('.Galeria');

    carrousel(Galeria);

});