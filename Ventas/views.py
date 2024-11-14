import ast
from datetime import datetime
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.contrib.auth import get_user_model
from django.contrib import messages


from Ventas.models import Carrito

def carrito(request, usuario):
    documento = usuario
    infocupon=[]
    total = 0
    totalcondescuento = 0
    valordescuento = 0
    porcentaje = 0
    carrito_dict=[]

    
    # Verificar si el carrito tiene ID_CUPON y ESTADO en NULL
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT ID_CUPON, ESTADO, ID_USUARIO_CAR
            FROM carritos 
            WHERE ID_USUARIO_CAR = %s 
        """, [usuario])
        carrito = cursor.fetchone()

        if carrito is not None:
            column_names = [col[0] for col in cursor.description]
            carrito_dict = dict(zip(column_names, carrito))
            if carrito_dict['ID_CUPON'] is not None:
                cursor.execute("""select * from cupones where id_cupon = %s""", [carrito_dict['ID_CUPON']])
                infocupon = cursor.fetchone()
           
            
    mostrar_campo_cupon = False

    
    if carrito and carrito[0] is None and carrito[1] is None:
        mostrar_campo_cupon = True

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM carritos WHERE id_usuario_car = %s", [documento])
        carrito = cursor.fetchone()
        if carrito is not None:
            column_names = [col[0] for col in cursor.description]
            carrito_dict = dict(zip(column_names, carrito))

        if carrito is None:
            productos_carrito = ["Vacio"]
            total = 0
        else:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM detalles_carritos WHERE id_carrito_dcar = %s", [carrito[0]])
                column_names = [col[0] for col in cursor.description]
                productos_carrito = [
                    dict(zip(column_names, row))
                    for row in cursor.fetchall()
                ]
                total = sum(producto['SUBTOTAL_DCAR'] for producto in productos_carrito)
                if mostrar_campo_cupon is False:
                    totalcondescuento = round(total-(total * infocupon[3]), 2)
                    valordescuento=round((total * infocupon[3]), 2)
                    porcentaje = int(infocupon[3] * 100)


    
    print(carrito_dict)
    # Pasar la variable mostrar_campo_cupon al template
    return render(request, 'Carrito.html', {
        'carrito': productos_carrito, 
        'total': total, 
        'totalcondescuento':totalcondescuento,
        'valordescuento':valordescuento,
        'porcentaje':porcentaje,
        'info_carrito': carrito_dict,
        'mostrar_campo_cupon': mostrar_campo_cupon,
        'infocupon':infocupon # Pasar la variable aquí
    
    })



@login_required
def validar_cupon(request, usuario):
    documento = usuario

    if request.method == 'POST':
        cod = request.POST.get('cod')

        # Verificar si el código de cupón existe en la tabla 'cupones'
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT ID_CUPON, ESTADO, CANT
                FROM cupones 
                WHERE COD = %s
            """, [cod])
            cupon = cursor.fetchone()

        if cupon:
            id_cupon, estado, cant = cupon

            # Verificar si la cantidad del cupón es 0
            if cant == 0:
                messages.error(request, "Cupón agotado.")
            else:
                messages.success(request, "Cupón válido, puedes continuar.")
                
                # Verificar si el carrito del usuario tiene ID_CUPON y ESTADO en NULL
                with connection.cursor() as cursor:
                    cursor.execute("""
                        SELECT ID_CARRITO_CAR 
                        FROM carritos 
                        WHERE ID_USUARIO_CAR = %s AND ID_CUPON IS NULL AND ESTADO IS NULL
                    """, [usuario])
                    carrito = cursor.fetchone()

                if carrito:
                    # Si el carrito existe, actualizar la tabla 'carritos' con el ID_CUPON y ESTADO
                    carrito_id = carrito[0]
                    with connection.cursor() as cursor:
                        cursor.execute("""
                            UPDATE carritos 
                            SET ID_CUPON = %s, ESTADO = %s 
                            WHERE ID_CARRITO_CAR = %s
                        """, [id_cupon, estado, carrito_id])

                    # Confirmar los cambios en la base de datos
                    connection.commit()
                    return redirect('carrito', usuario=usuario)
                else:
                    messages.error(request, "No se ha encontrado un carrito válido para este usuario.")
        else:
            messages.error(request, "El código de cupón no es válido.")

    return redirect('carrito', usuario=usuario)





def eliminar_del_carrito(request, item_id):
    user_id = request.user.id_usuario_usu
    carrito_id = request.POST.get('carrito_id')
    
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM detalles_carritos WHERE ID_DETALLE_DCAR = %s", [item_id])
        
        cursor.execute("SELECT COUNT(*) FROM detalles_carritos WHERE ID_CARRITO_DCAR = %s", [carrito_id])
        detalles_restantes = cursor.fetchone()[0]
        
        if detalles_restantes == 0:
            cursor.execute("DELETE FROM carritos WHERE ID_CARRITO_CAR = %s", [carrito_id])
        
    return redirect('carrito', usuario=user_id)

@login_required
def agregar_carrito(request):
    documento = request.POST.get('usuario')
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM carritos WHERE id_usuario_car = %s", [documento])
        carrito = cursor.fetchone()
        

        if carrito is None:
            # No existe un carrito para este usuario, puedes crear uno nuevo aquí
            cursor.execute("SELECT MAX(ID_CARRITO_CAR) FROM carritos")
            max_id = cursor.fetchone()[0]
            id_carrito_car = 1 if max_id is None else max_id + 1

            # Inserta el nuevo carrito aquí
            cursor.execute("INSERT INTO carritos (ID_CARRITO_CAR, id_usuario_car, total_car) VALUES (%s, %s, %s)", [id_carrito_car, documento, 0])

            # Inserta el nuevo detalle de carrito aquí
            cursor.execute("SELECT MAX(id_detalle_dcar) FROM detalles_carritos")
            max_id_detalle = cursor.fetchone()[0]
            id_detalle_dcar = 1 if max_id_detalle is None else max_id_detalle + 1

            cantidad_dcar = request.POST.get('cantidad')
            precio_dcar = request.POST.get('precio').replace(',', '.')
            subtotal_dcar = int(cantidad_dcar) * float(precio_dcar)
            id_producto_dcar_id = request.POST.get('producto')
            nombre_producto = request.POST.get('nombre')

           
            cursor.execute("INSERT INTO detalles_carritos (id_detalle_dcar, cantidad_dcar, precio_dcar, subtotal_dcar, id_producto_dcar, id_carrito_dcar, nombre_producto_dcar) VALUES (%s, %s, %s, %s, %s, %s, %s)", [id_detalle_dcar, cantidad_dcar, precio_dcar, subtotal_dcar, id_producto_dcar_id, id_carrito_car, nombre_producto])
            
            
        else:
            cantidad_dcar = request.POST.get('cantidad')
            precio_dcar = request.POST.get('precio').replace(',', '.')
            subtotal_dcar = int(cantidad_dcar) * float(precio_dcar)
            id_producto_dcar_id = request.POST.get('producto')
            nombre_producto = request.POST.get('nombre')
            
            cursor.execute("SELECT * FROM detalles_carritos WHERE id_carrito_dcar = %s AND id_producto_dcar = %s", [carrito[0], id_producto_dcar_id])
            detalle_carrito = cursor.fetchone()
            
            
            if detalle_carrito is not None:
                cantidad_dcar = detalle_carrito[1] + int(cantidad_dcar)
                subtotal_dcar = cantidad_dcar * float(precio_dcar)
                cursor.execute("UPDATE detalles_carritos SET cantidad_dcar = %s, subtotal_dcar = %s WHERE id_detalle_dcar = %s", [cantidad_dcar, subtotal_dcar, detalle_carrito[0]])
            else:
                id_carrito_car = carrito[0]
                # Inserta el nuevo detalle de carrito aquí
                cursor.execute("SELECT MAX(id_detalle_dcar) FROM detalles_carritos")
                max_id_detalle = cursor.fetchone()[0]
                id_detalle_dcar = 1 if max_id_detalle is None else max_id_detalle + 1
                cursor.execute("INSERT INTO detalles_carritos (id_detalle_dcar, cantidad_dcar, precio_dcar, subtotal_dcar, id_producto_dcar, id_carrito_dcar, nombre_producto_dcar) VALUES (%s, %s, %s, %s, %s, %s, %s)", [id_detalle_dcar, cantidad_dcar, precio_dcar, subtotal_dcar, id_producto_dcar_id, id_carrito_car, nombre_producto])

    return redirect('carrito', usuario=documento)

from decimal import Decimal

def total_carrito(request):
    diccionario = request.POST.get("carrito")
    diccionario = diccionario.replace("Decimal('", "").replace("')", "")  # Eliminar "Decimal(' " y " ')"
    lista = ast.literal_eval(diccionario)

    id_carro = lista[0]['ID_CARRITO_DCAR']
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT id_usuario_car FROM carritos WHERE ID_CARRITO_CAR = %s", [id_carro])
        usuario = cursor.fetchone()[0]
        
        cursor.execute("SELECT MAX(id_orden_ord) FROM ORDENES")
        max_id = cursor.fetchone()[0]
        id_orden_ord = 1 if max_id is None else max_id + 1
        fecha_ord = datetime.now()
        estado_ord = 'P'  
        total = 0
        
        for diccionario in lista:
            total += diccionario['SUBTOTAL_DCAR']
        
        cursor.execute("""
            SELECT ID_CUPON
            FROM carritos
            WHERE ID_CARRITO_CAR = %s
        """, [id_carro])
        id_cupon = cursor.fetchone()

        if id_cupon and id_cupon[0] is not None:
            cursor.execute("""
                SELECT PORCENTAJE, CANT
                FROM cupones
                WHERE ID_CUPON = %s
            """, [id_cupon[0]])
            cupon = cursor.fetchone()
            
            if cupon:
                porcentaje = cupon[0]
                precio_descuento = Decimal(total) * porcentaje  # Convertir total a Decimal
                cant = cupon[1] - 1


                cursor.execute("""
                    UPDATE cupones
                    SET CANT = %s
                    WHERE ID_CUPON = %s
                """, [cant, id_cupon[0]])
                        
                cursor.execute("""
                    INSERT INTO ordenes (ID_ORDEN_ORD, ID_USUARIO_ORD, FECHA_ORD, ESTADO_ORD, TOTAL_ORD, PRECIO_DESCUENTO, PORCENTAJE)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, [id_orden_ord, usuario, fecha_ord, estado_ord, total, precio_descuento, porcentaje])
                
            else:
                cursor.execute("""
                    INSERT INTO ordenes (ID_ORDEN_ORD, ID_USUARIO_ORD, FECHA_ORD, ESTADO_ORD, TOTAL_ORD)
                    VALUES (%s, %s, %s, %s, %s)
                """, [id_orden_ord, usuario, fecha_ord, estado_ord, total])
        else:
            cursor.execute("""
                INSERT INTO ordenes (ID_ORDEN_ORD, ID_USUARIO_ORD, FECHA_ORD, ESTADO_ORD, TOTAL_ORD)
                VALUES (%s, %s, %s, %s, %s)
            """, [id_orden_ord, usuario, fecha_ord, estado_ord, total])
        
        for diccionario in lista:
            cursor.execute("SELECT MAX(id_detalle_det) FROM DETALLES_ORDENES")
            max_id_det = cursor.fetchone()[0]
            id_detalle_det = 1 if max_id_det is None else max_id_det + 1
            
            cursor.execute("""
                INSERT INTO detalles_ordenes (ID_DETALLE_DET, CANTIDAD_DET, CANTIDAD_ENTREGADA_DET, PRECIO_DET, SUBTOTAL_DET, ID_PRODUCTO_DET_ID, ID_ORDEN_DET_ID)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, [id_detalle_det, diccionario['CANTIDAD_DCAR'], 0, diccionario['PRECIO_DCAR'], diccionario['SUBTOTAL_DCAR'], diccionario['ID_PRODUCTO_DCAR'], id_orden_ord])
            
            cursor.execute("""
                UPDATE productos SET existencia_pro = existencia_pro - %s WHERE id_producto_pro = %s
            """, [diccionario['CANTIDAD_DCAR'], diccionario['ID_PRODUCTO_DCAR']])
        
        cursor.execute("""
            DELETE FROM detalles_carritos WHERE ID_CARRITO_DCAR = %s
        """, [diccionario['ID_CARRITO_DCAR']])
        
        cursor.execute("""
            DELETE FROM carritos WHERE ID_CARRITO_CAR = %s
        """, [diccionario['ID_CARRITO_DCAR']])

    return redirect('ordenes')  



def ordenes(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM ordenes ORDER BY ID_ORDEN_ORD")
        column_names = [col[0] for col in cursor.description]
        ordenes = [
            dict(zip(column_names, row))
            for row in cursor.fetchall()
        ]
    print(ordenes)
    # Perform the required operations
    for orden in ordenes:
        precio_descuento = orden.get('PRECIO_DESCUENTO', 0) or 0
        total_ord = orden.get('TOTAL_ORD', 0) or 0
        
        # Calculate values
        valor_descuento =  precio_descuento
        total_con_descuento =  total_ord - precio_descuento
        total_sin_descuento = total_ord
        porcentaje_descuento = (valor_descuento / total_ord) * 100 if total_ord != 0 else 0

        # Add new keys to the dictionary
        orden['VALOR_DESCUENTO'] = round(valor_descuento, 2)
        orden['TOTAL_CON_DESCUENTO'] = round(total_con_descuento, 2)
        orden['TOTAL_SIN_DESCUENTO'] = round(total_sin_descuento, 2)
        orden['PORCENTAJE_DESCUENTO'] = round(porcentaje_descuento)
    print(ordenes)
    return render(request, 'AdminOrdenes.html', {'ordenes': ordenes})


def ordenes_detalles(request, id_orden):
    # Consulta para los detalles de la orden
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT detalles_ordenes.*, productos.NOMBRE_PRO, ordenes.ESTADO_ORD
            FROM detalles_ordenes 
            INNER JOIN productos ON detalles_ordenes.ID_PRODUCTO_DET_ID = productos.ID_PRODUCTO_PRO
            INNER JOIN ordenes ON detalles_ordenes.ID_ORDEN_DET_ID = ordenes.ID_ORDEN_ORD
            WHERE detalles_ordenes.ID_ORDEN_DET_ID = %s
        """, [id_orden])
        column_names = [col[0] for col in cursor.description]
        detalles = [dict(zip(column_names, row)) for row in cursor.fetchall()]

    # Consulta los valores de descuento y total de la orden
    with connection.cursor() as cursor:
        cursor.execute("SELECT PRECIO_DESCUENTO, TOTAL_ORD FROM ordenes WHERE ID_ORDEN_ORD = %s", [id_orden])
        result = cursor.fetchone()
        if result:
            precio_descuento, total_ord = result
            precio_descuento = precio_descuento or 0
            total_ord = total_ord or 0

            valor_descuento = precio_descuento
            total_con_descuento = total_ord - precio_descuento
            total_sin_descuento = total_ord
            porcentaje_descuento = (valor_descuento / total_ord) * 100 if total_ord != 0 else 0

            descuentos = {
                'VALOR_DESCUENTO': round(valor_descuento, 2),
                'TOTAL_CON_DESCUENTO': round(total_con_descuento, 2),
                'TOTAL_SIN_DESCUENTO': round(total_sin_descuento, 2),
                'PORCENTAJE_DESCUENTO': round(porcentaje_descuento)
            }
        else:
            descuentos = {}

    return render(request, 'OrdenesDetalles.html', {'detalles': detalles, 'descuentos': descuentos})

    
def actualizar_orden(request):
    id_orden = request.POST.get('id_orden')
    estado = request.POST.get('estado')
    
    if estado == 'Pendiente':
        estado = 'P'
    elif estado == 'Aprobado':
        estado = 'A'
    elif estado == 'Cancelado':
        estado = 'C'
    elif estado == 'Entregado':
        estado = 'E'
    
    with connection.cursor() as cursor:
        cursor.execute("UPDATE ordenes SET ESTADO_ORD = %s WHERE ID_ORDEN_ORD = %s", [estado, id_orden])
    return redirect('ordenes')

def detalles_del_detalle(request,id_orden):
    
    with connection.cursor() as cursor:
        cursor.execute("""SELECT * FROM detalles_ordenes WHERE ID_DETALLE_DET = %s""", [id_orden])
        column_names = [col[0] for col in cursor.description]
        detalle = [
            dict(zip(column_names, row))
            for row in cursor.fetchall()
        ]
        return render(request, 'DetallesDetalles.html', {'detalle': detalle})

def actualizar_cantidad_entregada(request, id_detalle):
    nueva_cantidad_entregada = request.POST.get('nueva_cantidad_entregada')

    with connection.cursor() as cursor:
        cursor.execute("""
            UPDATE detalles_ordenes 
            SET CANTIDAD_ENTREGADA_DET = %s 
            WHERE ID_DETALLE_DET = %s
        """, [nueva_cantidad_entregada, id_detalle])

    return redirect('Detalles_detalles_orden', id_orden=id_detalle)


def cancelarpedido(request, id_orden):
    

    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM detalles_ordenes WHERE ID_ORDEN_DET_ID = %s", [id_orden])
        column_names = [col[0] for col in cursor.description]
        detalles = [
            dict(zip(column_names, row))
            for row in cursor.fetchall()
        ]
        for detalle in detalles:
            cursor.execute("UPDATE productos SET existencia_pro = existencia_pro + %s WHERE id_producto_pro = %s", [detalle['CANTIDAD_DET'], detalle['ID_PRODUCTO_DET_ID']])
        cursor.execute("UPDATE ordenes SET ESTADO_ORD = 'C' WHERE ID_ORDEN_ORD = %s", [id_orden])
    return redirect('perfil')