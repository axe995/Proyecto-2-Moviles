/*function uploadphoto(){
    var imgFile = document.getElementById('strFileFoto');
    if (imgFile.files && imgFile.files[0]) {
        var reader = new FileReader();
        reader.onload = function(event) {
            var dataUri = event.target.result;
            console.log(dataUri);
            alert(dataUri);
       };
       reader.onerror = function(event) {
           console.error("File could not be read! Code " + event.target.error.code);
       };
       var url = reader.readAsDataURL(imgFile.files[0]);
       console.log(url);
       alert(url);
       FB.api(
    "/me/photos",
    "POST",
    {
          "object": {
              "source": url
          }
      },
      function (response) {
        if (response && !response.error) {
          alert(response);
        }
      }
  );
    }



    /*var imgURL = "http://www.mydomain.se/armani1.jpg";
 
    FB.api('/album_id/photos', 'post', {
        message:'photo description',
        url:imgURL        
    }, function(response){
        if (!response || response.error) {
            alert('Error occured');
        } else {
            alert('Post ID: ' + response.id);
        }
    });*/
//}


var WSURL = "https://complete-trees-607.appspot.com/";

$( document ).ready(function() {
  var useremail = getCookie("useremail");
  getTiendaInfo(useremail);
  getEtiquetasTienda();
});

function getTiendaInfo(strDuenoEmail){
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
      var tiendaJson = jQuery.parseJSON(mainJson.RETURNVALUE[0]);
      if(tiendaJson.mNombreTienda != "" && tiendaJson.mNombreTienda != "None"){
        document.getElementById('strNombreTienda').value=tiendaJson.mNombreTienda;
      }
      if(tiendaJson.mHorarioTienda != "" && tiendaJson.mHorarioTienda != "None"){
        document.getElementById('strHorario').value=tiendaJson.mHorarioTienda;
      }
      if(tiendaJson.mDescripcionTienda != "" && tiendaJson.mDescripcionTienda != "None"){
        document.getElementById("strDescription").value = tiendaJson.mDescripcionTienda;
      }
    }
  }
  xmlhttp.open("GET",WSURL + "?EXECOP=STI&MOD=GT&GTKEY="+strDuenoEmail,true);
  xmlhttp.send();
}

function getEtiquetasTienda(){
  var useremail = getCookie("useremail");
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
      for (var i = 0;i < 5; i++) {
        var etiquetaJson = jQuery.parseJSON(mainJson.RETURNVALUE[i]);
        var etiquetaValue = etiquetaJson.mNombreEtiqueta;
        var strNumeroEtiqueta = i+1
        document.getElementById("strEtiqueta"+strNumeroEtiqueta).value = etiquetaValue;
      }
    }
  }
  xmlhttp.open("GET",WSURL + "?EXECOP=OEQ&MOD=GT&GTKEY="+useremail,true);
  xmlhttp.send();
}

function updateTienda(){
  var useremail = getCookie("useremail");
    var parametros = "EXECOP=UTI&MOD=GT&GTKEY="+useremail;
    var strGMNOM = "&GTNOM=" + document.getElementById("strNombreTienda").value;
    var strGMFIA = "&GTTIM=" + document.getElementById("strHorario").value;
    var strDESC  = "&GTDES=" + document.getElementById("strDescription").value;

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
        else if(mainJson.RETURNVALUE == "0"){ alert("Fallo Update"); window.location = "https://smemallcr.appspot.com/HTML/desktop.html"; }
        else { alert("Operacion desconocida por el servidor."); }
      }    
    }
    xmlhttp.open("GET",WSURL + "?"+ parametros + strGMNOM + strGMFIA + strDESC,true);
    xmlhttp.send();
    updateEtiqueta("1");
    updateEtiqueta("2");
    updateEtiqueta("3");
    updateEtiqueta("4");
    updateEtiqueta("5");
  }

  function updateEtiqueta(strNumeroEtiqueta){
    var etq1 = document.getElementById("strEtiqueta1").value;
    var etq2 = document.getElementById("strEtiqueta2").value;
    var etq3 = document.getElementById("strEtiqueta3").value;
    var etq4 = document.getElementById("strEtiqueta4").value;
    var etq5 = document.getElementById("strEtiqueta5").value;
    if (etq1 != "" && etq2 != "" && etq3 != "" && etq4 != "" && etq5 != ""){
      return;
    } else {
      var valorEtiqueta = document.getElementById("strEtiqueta"+strNumeroEtiqueta).value.toUpperCase();
      var useremail = getCookie("useremail");
        if(valorEtiqueta != ""){
          var parametros = "EXECOP=IEQ&MOD=GT&GTKEY="+useremail+"&GEKEY="+valorEtiqueta;
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
            if (mainJson.RETURNVALUE == "1"){ }
            else if(mainJson.RETURNVALUE == "0"){ alert("Fallo Update Etiqueta "+ strNumeroEtiqueta); }
          }    
        }
        xmlhttp.open("GET",WSURL + "?"+ parametros,true);
        xmlhttp.send();
      }
    }
  }