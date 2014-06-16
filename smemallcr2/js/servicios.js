$( document ).ready(function() {
	LoadCatalogoServicios();
});


var WSURL = "https://complete-trees-607.appspot.com/";

function LoadCatalogoServicios(){
	var useremail = getCookie("useremail");
	var contenido = "<div id='contenedorProductos' class='row-fluid'>";
	contenido += "<div class='col-xs-6'><a class='thumbnail btn-success animated flipInY' onclick='LoadFormEditarProductos()'><img src='../img/nuevoServicio.png' /></a></div>";
	var xmlhttp;
	if (window.XMLHttpRequest)
	{// code for IE7+, Firefox, Chrome, Opera, Safari
	xmlhttp=new XMLHttpRequest();
	}
	else
	{// code for IE6, IE5
	xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	}
	xmlhttp.onreadystatechange=function()
	{
	if (xmlhttp.readyState==4 && xmlhttp.status==200)
	{
	  var mainJson = jQuery.parseJSON(xmlhttp.responseText);
	  contenido = "";
	  for (var i = 0; i < mainJson.RETURNVALUE.length; i++) {
	    var productoJson = jQuery.parseJSON(mainJson.RETURNVALUE[i]);
	    contenido += "<div class='col-xs-6'><a class='thumbnail btn-success animated flipInY'onclick='LoadFormEditarProductos2(\""+ productoJson.mKeyValue +"\")'><img src='"+ "../img/Servicio.png" +"' /></a></div>";
	  }
	  document.getElementById("contenedorProductos").innerHTML += contenido;
	}
	}
	xmlhttp.open("GET",WSURL + "?EXECOP=SSR&MOD=GSR&GSRKEY="+useremail,true);
	xmlhttp.send();	
	contenido += "</div>";
	document.getElementById("servicios").innerHTML = contenido;
	
}

function LoadFormEditarProductos(){
  setCookie("operacion","insert",1);
  $( "#dinamicContent" ).addClass("animated fadeOutDown");
  $( "#dinamicContent" ).load("/HTML/formEditarServicios.html", function (response, status, xhr) {
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

function LoadFormEditarProductos2(strIdProducto){
  setCookie("operacion","editar",1);
  setCookie("idProducto",strIdProducto,1);
  $( "#dinamicContent" ).addClass("animated fadeOutDown");
  $( "#dinamicContent" ).load("/HTML/formEditarServicios.html", function (response, status, xhr) {
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

function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires="+d.toGMTString();
    document.cookie = cname + "=" + cvalue + "; " + expires;
  }