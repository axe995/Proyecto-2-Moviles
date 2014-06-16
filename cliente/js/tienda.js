$( document ).ready(function() {
  //LoadMinifigures();
  LoadTienda();
});


function LoadFormDueno(){
	$( "#FormValues" ).addClass("animated fadeOutDown");
	$( "#FormValues" ).load("/HTML/formDueno.html", function (response, status, xhr) {
        if (status == "success"){
        	//$( "#minifigures" ).trigger('create');
        	$( "#FormValues" ).removeClass( "fadeOutDown" );
        	$( "#FormValues" ).addClass("fadeInUp");
        }
       	if (status == "error") {
            alert("There was an error loading the frame.");
        }
    });
}
function LoadTienda(){
  $( "#FormValues" ).addClass("animated fadeOutDown");
  $( "#FormValues" ).load("/HTML/stores.html", function (response, status, xhr) {
        if (status == "success"){
          //$( "#minifigures" ).trigger('create');
          $( "#FormValues" ).removeClass( "fadeOutDown" );
          $( "#FormValues" ).addClass("fadeInUp");
        }
        if (status == "error") {
            alert("There was an error loading the frame.");
        }
    });
}

function LoadProductos(){
  $( "#FormValues" ).addClass("animated fadeOutDown");
  $( "#FormValues" ).load("/HTML/productos.html", function (response, status, xhr) {
        if (status == "success"){
          //$( "#minifigures" ).trigger('create');
          $( "#FormValues" ).removeClass( "fadeOutDown" );
          $( "#FormValues" ).addClass("fadeInUp");
        }
        if (status == "error") {
            alert("There was an error loading the frame.");
        }
    });
}

function LoadServicios(){
  $( "#FormValues" ).addClass("animated fadeOutDown");
  $( "#FormValues" ).load("/HTML/servicios.html", function (response, status, xhr) {
        if (status == "success"){
          //$( "#minifigures" ).trigger('create');
          $( "#FormValues" ).removeClass( "fadeOutDown" );
          $( "#FormValues" ).addClass("fadeInUp");
        }
        if (status == "error") {
            alert("There was an error loading the frame.");
        }
    });
}