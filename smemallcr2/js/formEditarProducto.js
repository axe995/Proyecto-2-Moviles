function LoadRegresar(){
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

var WSURL = "https://complete-trees-607.appspot.com/";

$( document ).ready(function() {
  var useremail = getCookie("useremail");
  var operacion = getCookie("operacion");
  if(operacion == "editar"){
    getInfoProducto(getCookie("idProducto"))
  }
});


function getInfoProducto(strIdProducto)
{
  document.getElementById("idProducto").value = strIdProducto;
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
      if(productoJson.mCantidadDisponibleProd != ""){
        document.getElementById('strCantidadDisponible').value=productoJson.mCantidadDisponibleProd;
      } if(productoJson.mPrecioUnitarioProd != "") {
        document.getElementById('strPrecioUnitario').value=productoJson.mPrecioUnitarioProd;
      }
      getInfoMercaderia(productoJson.mKeyMerc)
    }
  }
  xmlhttp.open("GET",WSURL + "?EXECOP=SPR2&MOD=GPR&GPRKEY="+strIdProducto,true);
  xmlhttp.send();
}

function getInfoMercaderia(strIdMercaderia)
{
  document.getElementById("idMercaderia").value = strIdMercaderia;
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
        document.getElementById('strNombreProducto').value=productoJson.mNombreMerc;
      } if(productoJson.mDescripcionMerc != "") {
        document.getElementById('strDescription').value=productoJson.mDescripcionMerc;
      }
    }
  }
  xmlhttp.open("GET",WSURL + "?EXECOP=SMC&MOD=GM&GMKEY="+strIdMercaderia,true);
  xmlhttp.send();
}


function guardarProducto(){
   var operacion = getCookie("operacion");
  if(operacion == "editar"){
    updateProducto(document.getElementById("idProducto").value);
    updateMercaderia(document.getElementById("idMercaderia").value);
  } else {
    var strNombreProducto     = document.getElementById("strNombreProducto").value;
    var strCantidadDisponible = document.getElementById("strCantidadDisponible").value;
    var strPrecioUnitario     = document.getElementById("strPrecioUnitario").value;
    var strDescripcion        = document.getElementById("strDescription").value;
    var useremail = getCookie("useremail");
    if(strNombreProducto == "" || strCantidadDisponible == "" || strPrecioUnitario == "" || strDescription == ""){
      alert("Por favor no dejar espacios en blanco...");
    
    } else {
      
      var parametros = "EXECOP=APR&MOD=GPR&GMKTI="+useremail;
      var strGMNOM = "&GMNOM=" + strNombreProducto;
      var strGMDSC = "&GMDES=" + strDescripcion;
      var strGPRCAN = "&GPRCAN=" + strCantidadDisponible;
      var strGPRPUN = "&GPRPUN=" + strPrecioUnitario;
      // Ejecutar la insercion
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
          if (mainJson.RETURNVALUE == "1"){LoadRegresar(); }
          else if(mainJson.RETURNVALUE == "0"){alert("Error al crea el producto, por favor vuelva a intentar."); }
          else { alert("Operacion desconocida por el servidor."); }
        }    
      }
      xmlhttp.open("GET",WSURL + "/?"+ parametros + strGMNOM + strGMDSC + strGPRCAN + strGPRPUN,true);
      xmlhttp.send();
    }
  }
}

function updateProducto(strProductoID){
  var useremail = getCookie("useremail");
    var parametros = "EXECOP=UPR&MOD=GPR&GPRKEY="+strProductoID;
    var strGMNOM = "&GPRCAN=" + document.getElementById("strCantidadDisponible").value;
    var strGMFIA = "&GPRPUN=" + document.getElementById("strPrecioUnitario").value;
    // Ejecutar la insercion
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
        if (mainJson.RETURNVALUE == "1"){ LoadRegresar(); }
        else if(mainJson.RETURNVALUE == "0"){ alert("Ha fallado la actualizacion del Producto"); }
        else { alert("Operacion desconocida por el servidor."); }
      }
    }
    xmlhttp.open("GET",WSURL + "/?"+ parametros + strGMNOM  + strGMFIA ,true);
    xmlhttp.send();
}

function updateMercaderia(strIdMercaderia){
  var useremail = getCookie("useremail");
    var parametros = "EXECOP=UMC&MOD=GM&GMKEY="+strIdMercaderia;
    var strGMNOM = "&GMNOM=" + document.getElementById("strNombreProducto").value;
    var strGMFIA = "&GMDES=" + document.getElementById("strDescription").value;
    // Ejecutar la insercion
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
        if (mainJson.RETURNVALUE == "1"){ LoadRegresar(); }
        else if(mainJson.RETURNVALUE == "0"){ alert("Ha fallado la actualizacion del Producto"); }
        else { alert("Operacion desconocida por el servidor."); }
      }
    }
    xmlhttp.open("GET",WSURL + "/?"+ parametros + strGMNOM  + strGMFIA ,true);
    xmlhttp.send();
}

function userDelete(){
  var operacion = getCookie("operacion");
  if(operacion == "editar"){
    borrarProducto(document.getElementById("idProducto").value);
    borrarMercaderia(document.getElementById("idMercaderia").value);
  }
}

function borrarProducto(strProductoID){
    // Ejecutar la insercion
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
        if (mainJson.RETURNVALUE == "1"){ LoadRegresar(); }
        else if(mainJson.RETURNVALUE == "0"){ alert("Ha fallado la actualizacion del Producto"); }
        else { alert("Operacion desconocida por el servidor.Prod"); }
      }
    }
    xmlhttp.open("GET",WSURL + "?"+ "EXECOP=BPR&MOD=GPR&GPRKEY="+strProductoID ,true);
    xmlhttp.send();
}

function borrarMercaderia(strIdMercaderia){
    // Ejecutar la insercion
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
        if (mainJson.RETURNVALUE == "1"){ LoadRegresar(); }
        else if(mainJson.RETURNVALUE == "0"){ alert("Ha fallado la actualizacion del Producto"); }
        else { alert("Operacion desconocida por el servidor.Merc"); }
      }
    }
    xmlhttp.open("GET",WSURL + "?"+ "EXECOP=BMC&MOD=GM&GMKEY=" + strIdMercaderia ,true);
    xmlhttp.send();
}
