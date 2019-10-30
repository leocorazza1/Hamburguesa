function ocultarRegistro(){

    $("#registro").hide();
    $("#sesion").show();
    $("#titulo").text("Iniciar Sesion");
    $("#botonR").hide();
    $("#botonI").show();
    $("#tengoCuenta").hide();
    $("#volver").show();
    };
    
  $("#volver").click(function(){
        $("#titulo").text("REGISTRARSE");
        $("#sesion").hide();
        $("#registro").show();
        $("#botonR").show();
        $("#tengoCuenta").show();
        $("#volver").hide();
        $("#botonI").hide();
    });

    

function cancelarpedido(id)
        { 
            $.post("http://127.0.0.1:8000/cancelar/",
              {
                id: id,
                csrfmiddlewaretoken: '{{ csrf_token }}' //LINEA SUPER IMPORTANTE
              },
              function(data, status){
                if(data){
                    var URLactual = jQuery(location).attr('href');
                    window.location.href=URLactual;
                      /*Lobibox.notify('info', {
                        position: 'top right',
                        title: 'Notificacion',
                        msg: 'SU PEDIDO HA SIDO CANCELADO!'
                    });
    
                   $("#"+id).css("display","none");*/
                
                }
                else
                    {
                        alert("Error al cancelar Pedido , intente nuevamente!");
    
                    }
    
            });
    
        }
    
function addcarrito(id)
        { 
            $.post("http://127.0.0.1:8000/addcarrito/",
              {
                id: id,
                csrfmiddlewaretoken: '{{ csrf_token }}' //LINEA SUPER IMPORTANTE
              },
              function(data, status){
                if(data=='True'){
                    //var URLactual = jQuery(location).attr('href');
                    //window.location.href=URLactual;
                    Lobibox.notify('success', {
                        position: 'top right',
                        title: 'Notificacion',
                        msg: 'AÑADIDO AL CARRITO CON EXITO'
                    });
    
                   
                }
                else
                    {
                        Lobibox.notify('info', {
                        position: 'top right',
                        title: 'Notificacion',
                        msg: 'Este elemento ya se añadio al carrito'
                    });
    
                    }
    
            });
    
        }
    
function eliminardelcarrito(id){
    
        $.post("http://127.0.0.1:8000/delcarrito/",
              {
                id: id,
                csrfmiddlewaretoken: '{{ csrf_token }}' //LINEA SUPER IMPORTANTE
              },
              function(data, status){
                if(data){
                    var URLactual = jQuery(location).attr('href');
                    window.location.href=URLactual;
                   
                }
                else
                    {
                        alert("Error al eliminar del Carrito , intente nuevamente");
    
                    }
    
            });
    
    }