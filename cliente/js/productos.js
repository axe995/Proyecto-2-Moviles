$( document ).ready(function() {
	LoadCatalogoProductos();
});


var WSURL = "https://complete-trees-607.appspot.com/";

function LoadCatalogoProductos(){
	var useremail = getCookie("useremail");
	var contenido = "<div id='contenedorProductos' class='row-fluid'>";
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
	    contenido += "<div class='col-xs-6'><a class='thumbnail btn-success animated flipInY' data-toggle='modal' data-target='.bs-example-modal-sm' onclick='getInfoProducto(\""+productoJson.mKeyValue+"\")'><img src='"+ "../img/Producto.png" +"' /></a></div>";
	  }
	  document.getElementById("contenedorProductos").innerHTML += contenido;
	}
	}
	xmlhttp.open("GET",WSURL + "?EXECOP=SPR&MOD=GPR&GPRKEY="+useremail,true);
	xmlhttp.send();	
	contenido += "</div>";
	document.getElementById("productos").innerHTML = contenido;
	
}

function getInfoProducto(strIdProducto)
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
      getInfoMercaderia(productoJson.mKeyMerc, productoJson.mCantidadDisponibleProd, productoJson.mPrecioUnitarioProd);
    }
  }
  xmlhttp.open("GET",WSURL + "?EXECOP=SPR2&MOD=GPR&GPRKEY="+strIdProducto,true);
  xmlhttp.send();
}

function getInfoMercaderia(strIdMercaderia, strCantidad, strPrecioUnitario)
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
      if(productoJson.mNombreMerc != ""){
        //document.getElementById('strNombreProducto').value=productoJson.mNombreMerc;
      } if(productoJson.mDescripcionMerc != "") {
        //document.getElementById('strDescription').value=productoJson.mDescripcionMerc;
      }
      contenido = "";
	  contenido += "<div class='thumbnail'><img src='../img/Producto.png' <div class='caption'><h3>" + productoJson.mNombreMerc + "</h3><p>CantidadDisponible: " + strCantidad +"</p><p>Precio Unitario: " + strPrecioUnitario +" colones</p><p>Description: " + productoJson.mDescripcionMerc + "</p></div>";
      document.getElementById("modalBody").innerHTML = contenido;
    }
  }
  xmlhttp.open("GET",WSURL + "?EXECOP=SMC&MOD=GM&GMKEY="+strIdMercaderia,true);
  xmlhttp.send();
}

function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires="+d.toGMTString();
    document.cookie = cname + "=" + cvalue + "; " + expires;
  }