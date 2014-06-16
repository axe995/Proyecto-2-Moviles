var WSURL = "https://complete-trees-607.appspot.com/";


$( document ).ready(function() {
  var useremail = getCookie("useremail");
  LoadClientInfo(useremail);
  LoadTienda();
  document.getElementById("userEmail").value = useremail;
});


function LoadDesktop(){
	window.location = "https://x-fabric-612.appspot.com/HTML/desktop.html";	
}


function LoadClientInfo(strClienteEmail){
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
      var clienteJson = jQuery.parseJSON(mainJson.RETURNVALUE[0]);
      document.getElementById('nombreCliente').innerHTML = clienteJson.mNombreCliente;
    }
  }
  xmlhttp.open("GET",WSURL + "?EXECOP=SCL&MOD=GC&GCKEY="+strClienteEmail,true);
  xmlhttp.send();
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