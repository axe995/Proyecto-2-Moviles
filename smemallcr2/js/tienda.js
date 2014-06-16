$( document ).ready(function() {
  //LoadMinifigures();
  LoadFormDueno();
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
function LoadFormTienda(){
  $( "#FormValues" ).addClass("animated fadeOutDown");
  $( "#FormValues" ).load("/HTML/formTienda.html", function (response, status, xhr) {
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