function LoadRegresar(){
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

var WSURL = "https://complete-trees-607.appspot.com/";

$( document ).ready(function() {
  var useremail = getCookie("useremail");
  var operacion = getCookie("operacion");
  getInfoContrato();
  getInfoDisponibilidad();
  if(operacion == "editar"){
    getInfoProducto(getCookie("idProducto"));
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
      if(productoJson.mPrecioContrato != ""){
        document.getElementById('strPrecioContrato').value=productoJson.mPrecioContrato;
      }
      getInfoMercaderia(productoJson.mKeyMerc)
    }
  }
  xmlhttp.open("GET",WSURL + "?EXECOP=SSR2&MOD=GSR&GSRKEY="+strIdProducto,true);
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
        document.getElementById('strNombreServicio').value=productoJson.mNombreMerc;
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
    var strNombreServicio     = document.getElementById("strNombreServicio").value;
    var strDescription        = document.getElementById("strDescription").value;
    var strKeyContrato        = document.getElementById("strTipoDeContrato").value;
    var strKeyDisponibilidad  = document.getElementById("strDisponibilidad").value;
    var strPrecioContrato     = document.getElementById("strPrecioContrato").value;
    var useremail = getCookie("useremail");
    if(strNombreServicio == "" || strKeyContrato == "" || strKeyDisponibilidad == "" || strDescription == "" || strPrecioContrato == ""){
      alert("Por favor no dejar espacios en blanco...");
    
    } else {
      var parametros = "EXECOP=ASR&MOD=GSR&GMKTI="+useremail;
      var strGMNOM = "&GMNOM=" + strNombreServicio;
      var strGMDSC = "&GMDES=" + strDescription;
      var strGPRCAN = "&GSRPPC=" + strPrecioContrato;
      var strGPRPUN = "&GMKCO=" + strKeyContrato;
      var strGMKDI  = "&GMKDI=" + strKeyDisponibilidad;
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
      xmlhttp.open("GET",WSURL + "/?"+ parametros + strGMNOM + strGMDSC + strGPRCAN + strGPRPUN + strGMKDI,true);
      xmlhttp.send();
    }
  }
}

function updateProducto(strProductoID){
  var useremail = getCookie("useremail");
    var parametros = "EXECOP=USR&MOD=GSR&GSRKEY="+strProductoID;
    var strGMNOM = "&GSRPPC=" + document.getElementById("strPrecioContrato").value;
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
        else if(mainJson.RETURNVALUE == "0"){ alert("Ha fallado la actualizacion del Servicio"); }
        else { alert("Operacion desconocida por el servidor."); }
      }
    }
    xmlhttp.open("GET",WSURL + "/?"+ parametros + strGMNOM  ,true);
    xmlhttp.send();
}

function updateMercaderia(strIdMercaderia){
  var useremail = getCookie("useremail");
    var parametros = "EXECOP=UMC&MOD=GM&GMKEY="+strIdMercaderia;
    var strGMNOM = "&GMNOM=" + document.getElementById("strNombreServicio").value;
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
        else if(mainJson.RETURNVALUE == "0"){ alert("Ha fallado la actualizacion del Servicio"); }
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
    xmlhttp.open("GET",WSURL + "?"+ "EXECOP=BSR&MOD=GSR&GSRKEY="+strProductoID ,true);
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

function getInfoContrato()
{
  var select = document.getElementById("strTipoDeContrato");
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
      for (var i = 0; i < mainJson.RETURNVALUE.length; i++) {
        var productoJson = jQuery.parseJSON(mainJson.RETURNVALUE[i]);
        var option = document.createElement("option");
        option.text = productoJson.mTipoContrato;
        option.value = productoJson.mKeyValue;
        select.add(option);
      }
    }
  }
  xmlhttp.open("GET",WSURL + "?EXECOP=SCO&MOD=GCT",true);
  xmlhttp.send();
}

function getInfoDisponibilidad()
{
  var select = document.getElementById("strDisponibilidad");
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
      for (var i = 0; i < mainJson.RETURNVALUE.length; i++) {
        var productoJson = jQuery.parseJSON(mainJson.RETURNVALUE[i]);
        var option = document.createElement("option");
        option.text = productoJson.mTipoDisponibilidad;
        option.value = productoJson.mKeyValue;
        select.add(option);
      }
    }
  }
  xmlhttp.open("GET",WSURL + "?EXECOP=SDS&MOD=GDS",true);
  xmlhttp.send();
}
