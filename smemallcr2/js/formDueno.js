var WSURL = "https://complete-trees-607.appspot.com/";

$( document ).ready(function() {
  var useremail = getCookie("useremail");
  getDuenoInfo(useremail);
});


function getDuenoInfo(strDuenoEmail)
{
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
      var duenoJson = jQuery.parseJSON(mainJson.RETURNVALUE[0]);
      document.getElementById('strNombre').value=duenoJson.mNombreDueno;
      document.getElementById('strCorreo').value=duenoJson.mCorreoDueno;
      if(duenoJson.mResidenciaDueno != ""){
      	document.getElementById("strResidencia").value = duenoJson.mResidenciaDueno;
      }
      if(duenoJson.mDescripcionDueno != ""){
      	document.getElementById("strDescription").value = duenoJson.mDescripcionDueno;
      }
    }
  }
  xmlhttp.open("GET",WSURL + "/?EXECOP=SDU&MOD=GD&GDKEY="+strDuenoEmail,true);
  xmlhttp.send();
}

function updateDueno(){
	var useremail = getCookie("useremail");
    var parametros = "EXECOP=UDU&MOD=GD&GDKEY="+useremail;
    var strGMNOM = "&GDNOM=" + document.getElementById("strNombre").value;
    var strGMDSC = "&GDCOR=" + useremail;
    var strGMFIA = "&GDRES=" + document.getElementById("strResidencia").value;
    var strGMFFA = "&GDDES=" + document.getElementById("strDescription").value;
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
        if (mainJson.RETURNVALUE == "1"){ window.location = "https://smemallcr.appspot.com/HTML/desktop.html"; }
        else if(mainJson.RETURNVALUE == "0"){ window.location = "https://smemallcr.appspot.com/HTML/desktop.html"; }
        else { alert("Operacion desconocida por el servidor."); }
      }    
    }
    xmlhttp.open("GET",WSURL + "/?"+ parametros + strGMNOM + strGMDSC + strGMFIA + strGMFFA,true);
    xmlhttp.send();
  }