//FUNCION QUE TOMA INFORMACION DE LA BASE DE DATOS Y COMPLETA EL MODAL
function generarPedido(id){

  $.post("http://127.0.0.1:8000/pedido/",
      {
        id: id,
        csrfmiddlewaretoken: '{{ csrf_token }}' //LINEA SUPER IMPORTANTE
      },
      function(data, status){
         producto=JSON.parse(data)
            $("#nombre_producto").text("Pedido: "+producto.nombre);
            $("#tipo").text(producto.tipo);
            $("#precio").text("$"+producto.precio);
            $("#pk").val(id);           
            $("#modal").modal("show");
              
            
        });
}

// FUNCION QUE TOMA LOS DATOS INGRESADOS ERN EL MODAL Y LOS GUARDA EN LA BASE DE DATOS
$("#pedido").click(function(){
        var nombre=$("#nombre").val();
        var apellido=$("#apellido").val();
        var contacto=$("#contacto").val();
        var direccion=$("#direccion").val();
        var id_producto=$("#pk").val();
        var cantidad=$("#cantidad").val();


        $.post("http://127.0.0.1:8000/realizarpedido/",
          {
            id:id_producto,
            nombre: nombre,
            apellido:apellido,
            contacto:contacto,
            direccion:direccion,
            cantidad:cantidad,
            csrfmiddlewaretoken: '{{ csrf_token }}' //LINEA SUPER IMPORTANTE
          },
          function(data, status){
            $("#modal").modal("hide");
            if(data){
                alert("Su pedido fue realizado con Exito")
            }
        
            
        });
 })


