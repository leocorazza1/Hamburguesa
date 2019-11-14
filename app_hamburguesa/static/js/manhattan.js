                        var path = "http://127.0.0.1:8000";

                        function ocultarRegistro() {
                            $("#registro").hide();
                            $("#sesion").show();
                            $("#titulo").text("Iniciar Sesion");
                            $("#botonR").hide();
                            $("#botonI").show();
                            $("#tengoCuenta").hide();
                            $("#volver").show();
                        };

                        $("#volver").click(function () {
                            $("#titulo").text("REGISTRARSE");
                            $("#sesion").hide();
                            $("#registro").show();
                            $("#botonR").show();
                            $("#tengoCuenta").show();
                            $("#volver").hide();
                            $("#botonI").hide();
                        });

                        function cancelarpedido(id) {
                            $.post(path + "/cancelar/",
                                {
                                    id: id,
                                    csrfmiddlewaretoken: '{{ csrf_token }}' //LINEA SUPER IMPORTANTE
                                },
                                function (data, status) {
                                    if (data) {
                                        var URLactual = jQuery(location).attr('href');
                                        window.location.href = URLactual;
                                        /*Lobibox.notify('info', {
                                          position: 'top right',
                                          title: 'Notificacion',
                                          msg: 'SU PEDIDO HA SIDO CANCELADO!'
                                      });
                      
                                     $("#"+id).css("display","none");*/

                                    }
                                    else {
                                        alert("Error al cancelar Pedido , intente nuevamente!");

                                    }

                                });

                        }

                        function addcarrito(id) {
                            $.post(path + "/addcarrito/",
                                {
                                    id: id,
                                    csrfmiddlewaretoken: '{{ csrf_token }}' //LINEA SUPER IMPORTANTE
                                },
                                function (data, status) {

                                    if(data=="True"){

                                        Lobibox.notify('success', {
                                            position: 'top right',
                                            title: 'Notificacion',
                                            msg: 'Elemento agregado al carrito!'
                                        });

                                    }
                                    else{

                                        Lobibox.notify('info', {
                                            position: 'top right',
                                            title: 'Notificacion',
                                            msg: '¡El elemento ya existe en el carrito!'
                                        });

                                    }

                                });

                        }

                        function eliminardelcarrito(id,all) {

                            $.post(path + "/delcarrito/",
                                {
                                    id: id,
                                    all:all,
                                    csrfmiddlewaretoken: '{{ csrf_token }}' //LINEA SUPER IMPORTANTE
                                },
                                function (data, status) {

                                }).done(function(){
                                    var URLactual = jQuery(location).attr('href');
                                    window.location.href = URLactual;
                                }).fail(function(){
                                    alert("Error al eliminar todos los elementos , intentelo nuevamente!")
                                })


                        }
                        function generarPedido(id) {

                            $.post(path + "/pedido/",
                                {
                                    id: id,
                                    csrfmiddlewaretoken: '{{ csrf_token }}' //LINEA SUPER IMPORTANTE
                                },
                                function (data, status) {

                                    producto = JSON.parse(data)
                                    $("#nombre_producto").text(producto.nombre_producto);
                                    $("#tipo").text(producto.tipo);
                                    $("#precio").text("$" + producto.precio);
                                    $("#pk").val(id);
                                    var imagen = document.getElementById("imagen");
                                    imagen.setAttribute("src", producto.imagen);
                                    $("#modal").modal("show");

                                });

                        }
                        $(document).ready(function () {
                            $('[data-toggle="popover"]').popover();
                        });

                            function pedir_todo() {

                            var form = $("#modalpedirtodo").find("form");// obtengo todos los formularios dentro del modal
                            var direccion = $("#direccion_carrito").val();
                            var referencia = $("#referencia_carrito").val();
                            $("#pedirtodo").css("display", "block");
                                form.each(function (index, element) {             // recorro cada formulario
                                    var cantidad = $(element).find("#cantidad_elementos").val(); //por cada formulario obtengo el id cantidad y el del producto
                                    var id_producto = $(element).find("#id_producto").val();
                                    $.post(path + "/realizarpedido/",
                                        {
                                            id: id_producto,
                                            cantidad: cantidad,
                                            direccion: direccion,
                                            referencia: referencia,
                                            csrfmiddlewaretoken: '{{ csrf_token }}' //LINEA SUPER IMPORTANTE
                                        },
                                        function (data, status) {

                                        }).done(function(){

                                            Lobibox.notify('success', {
                                                    position: 'top right',
                                                    title: 'Notificacion',
                                                    msg: 'Producto pedido con Exito, dirigite a "MIS PEDIDOS" para detalles'
                                                });
                                        }).fail(function(){

                                            Lobibox.notify('info', {
                                                    position: 'top right',
                                                    title: 'Notificacion',
                                                    msg: 'ERROR! No se pudo realizar el pedido con Exito! intentelo nuevamente!'
                                                });


                                        });

                                });
                         
                        }