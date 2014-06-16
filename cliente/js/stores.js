$( document ).ready(function() {
	LoadCatalogoTiendas();
});


var WSURL = "https://complete-trees-607.appspot.com/";

function LoadCatalogoTiendas(){
	var contenido = "<div id='contenedorTiendas' class='row-fluid'>";
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
	    contenido += "<div class='col-xs-6'><a class='thumbnail btn-success animated flipInY' data-toggle='modal' data-target='.bs-example-modal-sm' onclick='getInfoTienda(\""+ productoJson.mKeyValue +"\")'><img src='"+ "../img/Tienda.png" +"' /></a></div>";
	  }
	  document.getElementById("contenedorTiendas").innerHTML += contenido;
	}
	}
	xmlhttp.open("GET",WSURL + "?EXECOP=STI&MOD=GT",true);
	xmlhttp.send();	
	contenido += "</div>";
	document.getElementById("stores").innerHTML = contenido;
	
}

function getInfoTienda(strIdTienda)
{
  //document.getElementById("idProducto").value = strIdProducto;
  document.getElementById("modalBody").innerHTML = "<div class='progress progress-striped active'><div class='progress-bar'  role='progressbar' aria-valuenow='100' aria-valuemin='0' aria-valuemax='100' style='width: 100%'><span class='sr-only'>100% Complete</span></div></div>";
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
      var productoJson = jQuery.parseJSON(mainJson.RETURNVALUE[0]);
      getInfoDueno(productoJson.mKeyDuenoTienda, productoJson.mNombreTienda, productoJson.mDescripcionTienda, productoJson.mHorarioTienda, productoJson.mLatitud, productoJson.mLongitud);
    }
  }
  xmlhttp.open("GET",WSURL + "?EXECOP=STI2&MOD=GT&GTKEY="+strIdTienda,true);
  xmlhttp.send();
}

function getInfoDueno(strKeyDuenoTienda, strNombreTienda, strDescripcionTienda, strHorarioTienda, strLAT, strLNG)
{
  //document.getElementById("idMercaderia").value = strIdMercaderia;
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
      var productoJson = jQuery.parseJSON(mainJson.RETURNVALUE[0]);
      contenido = "";
	  contenido += "<div class='thumbnail'><img src='../img/Tienda.png' <div class='caption'><h3>" + strNombreTienda + "</h3><p>Dueño: " + productoJson.mNombreDueno +"</p><p>Correo del Dueño: " + productoJson.mCorreoDueno +"</p><p>Horario de Atención: " + strHorarioTienda + "</p><p>Description: " + strDescripcionTienda + "</p><button type='button' class='btn btn-default' data-dismiss='modal' onclick='LoadMap(\""+strLAT+"\",\""+strLNG+"\")'>Ver Posicion</button></div>";
      document.getElementById("modalBody").innerHTML = contenido;
    }
  }
  xmlhttp.open("GET",WSURL + "?EXECOP=SDU2&MOD=GD&GDKEY="+strKeyDuenoTienda,true);
  xmlhttp.send();
}

function LoadMap(strLAT, strLNG){
  setCookie("LAT",strLAT,1);
  setCookie("LNG",strLNG,1);
  $( "#dinamicContent" ).addClass("animated fadeOutDown");
  $( "#dinamicContent" ).load("/HTML/mapaRuta.html", function (response, status, xhr) {
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