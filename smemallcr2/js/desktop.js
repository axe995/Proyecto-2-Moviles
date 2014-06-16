$( document ).ready(function() {
  LoadTienda();
  var useremail = getCookie("useremail");
  document.getElementById("userEmail").value = useremail;
});


function LoadDesktop(){
	window.location = "https://smemallcr.appspot.com/HTML/desktop.html";	
}


function LoadTienda(){
  $( "#dinamicContent" ).addClass("animated fadeOutDown");
  $( "#dinamicContent" ).load("/HTML/tienda.html", function (response, status, xhr) {
        if (status == "success"){
          //$( "#minifigures" ).trigger('create');
          $( "#dinamicContent" ).removeClass( "fadeOutDown" );
          $( "#dinamicContent" ).addClass("fadeInUp");
        }
        if (status == "error") {
            alert("There was an error loading the frame.");
        }
    });
}

function LoadProductos(){
  $( "#dinamicContent" ).addClass("animated fadeOutDown");
  $( "#dinamicContent" ).load("/HTML/productos.html", function (response, status, xhr) {
        if (status == "success"){
          //$( "#minifigures" ).trigger('create');
          $( "#dinamicContent" ).removeClass( "fadeOutDown" );
          $( "#dinamicContent" ).addClass("fadeInUp");
        }
        if (status == "error") {
            alert("There was an error loading the frame.");
        }
    });
}

function LoadServicios(){
  $( "#dinamicContent" ).addClass("animated fadeOutDown");
  $( "#dinamicContent" ).load("/HTML/servicios.html", function (response, status, xhr) {
        if (status == "success"){
          //$( "#minifigures" ).trigger('create');
          $( "#dinamicContent" ).removeClass( "fadeOutDown" );
          $( "#dinamicContent" ).addClass("fadeInUp");
        }
        if (status == "error") {
            alert("There was an error loading the frame.");
        }
    });
}

function LogOut(){
	FB.logout(function(response) {
  		window.location = "https://smemallcr.appspot.com";
	});
}

function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i=0; i<ca.length; i++) {
        var c = ca[i].trim();
        if (c.indexOf(name) == 0) return c.substring(name.length, c.length);
    }
    return "";
}