from django.shortcuts import render,redirect
from .views import *
from django.db import connection
from django.contrib import messages
from django.http import Http404,JsonResponse
from django.conf import settings
import os
from django.contrib.auth.decorators import login_required
from django.db import connection, IntegrityError
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import HttpResponseForbidden
from django.db import IntegrityError
from django.http import HttpResponseBadRequest



@login_required
def agregar_resena(request):
    
    if request.method == 'POST':
        
        resena= request.POST.get('resena')
        producto = request.POST.get('producto')
        usuario = request.POST.get('usuario')
        with connection.cursor() as cursor:
        
            cursor.execute("SELECT MAX(ID_RESENA_RE) FROM resenas")
            max_id = cursor.fetchone()[0]

           
            next_id = 1 if max_id is None else max_id + 1

            id_resena_re = next_id
            
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO resenas (id_resena_re,id_producto_re, id_usuario_re,resena_re)
                    VALUES (%s, %s, %s, %s)
                """, [id_resena_re,producto,usuario,resena])
                connection.commit()
    return redirect('productos')

@login_required
def eliminar_cupon(request, id_cupon):
    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM cupones WHERE id_cupon = %s", [id_cupon])
        
        messages.success(request, 'Cupón eliminado exitosamente.')
    except Exception as e:
        messages.error(request, f'Error al eliminar el cupón: {str(e)}')
    
    return redirect('cuponessadmin')  

@login_required
def cuponessadmin(request):
    cupones = []
    with connection.cursor() as cursor:
        cursor.execute("SELECT id_cupon, cod, cant, porcentaje, estado FROM cupones")
        rows = cursor.fetchall()
        
        for row in rows:
            cupon = {
                'ID_CUPON': row[0],
                'COD': row[1],
                'CANT': row[2],
                'PORCENTAJE': round(row[3] * 100, 0),
                'ESTADO': row[4]
            }
            cupones.append(cupon)
            print(cupones)

    return render(request, 'AdminCupones.html', {'cupones': cupones})


@login_required
def crearcupon(request):
    if request.method == 'POST':
        try:
            codigo_cupon = request.POST.get('codigo_cupon')
            cantidad = int(request.POST.get('cantidad'))
            if cantidad <= 0:
                messages.error(request, 'La cantidad debe ser mayor que 0.')
                return redirect('crearcupon')
            porcentaje = float(request.POST.get('porcentaje'))
            porcentaje = round(porcentaje / 100, 2)
            activo = request.POST.get('activo') == 'True'

            with connection.cursor() as cursor:
                # Obtener el siguiente ID disponible para id_cupon
                cursor.execute("SELECT NVL(MAX(id_cupon), 0) + 1 FROM cupones")
                next_id = cursor.fetchone()[0]

                # Insertar el nuevo cupón
                cursor.execute("""
                    DECLARE
                        v_id_cupon NUMBER := :next_id;
                        v_cod VARCHAR2(20) := :codigo_cupon;
                        v_cant NUMBER := :cantidad;
                        v_porcentaje NUMBER := :porcentaje;
                        v_estado NUMBER(1) := :activo;
                    BEGIN
                        INSERT INTO cupones (id_cupon, cod, cant, porcentaje, estado)
                        VALUES (v_id_cupon, v_cod, v_cant, v_porcentaje, v_estado);
                    END;
                """, {
                    'next_id': next_id,
                    'codigo_cupon': codigo_cupon,
                    'cantidad': cantidad,
                    'porcentaje': porcentaje,
                    'activo': 1 if activo else 0
                })

                messages.success(request, 'Cupón creado exitosamente.')
                return redirect('cuponessadmin')
        except ValueError as e:
            print(e)
    return render(request, 'CrearCupones.html')



@login_required
def eliminar_resena(request, id_resena_re):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id_usuario_re FROM resenas WHERE id_resena_re = %s", [id_resena_re])
        resena = cursor.fetchone()
    
    if resena is None:
        return HttpResponseForbidden("Reseña no encontrada.")
    
    id_usuario_re = resena[0]
    
    if request.user.is_superuser or request.user.id_usuario_usu == id_usuario_re:
        if request.method == 'POST':
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM resenas WHERE id_resena_re = %s", [id_resena_re])
                connection.commit()
        return redirect('productos')
    else:
        return HttpResponseForbidden("No tienes permiso para eliminar esta reseña.")
@login_required
def agregar_favoritos(request, id_producto_pro):
    
    if request.method == 'POST':
        id_usuario=0
        id_usuario = request.user
        with connection.cursor() as cursor:
            cursor.execute("SELECT id_favoritos FROM favoritos WHERE id_usuario_fa = %s AND id_producto_fa = %s", [id_usuario, id_producto_pro])
            favorito = cursor.fetchone()
            
           
            

            if favorito:
                # Si el favorito ya existe, eliminarlo
                cursor.execute("DELETE FROM favoritos WHERE id_favoritos = %s", [favorito[0]])
                is_favorite = False
            elif favorito is None:
                # Si el favorito no existe, crearlo
                cursor.execute("SELECT MAX(ID_FAVORITOS) FROM favoritos")
                max_id = cursor.fetchone()[0]
                id = 1 if max_id is None else max_id + 1
                cursor.execute("""
                        INSERT INTO favoritos (id_favoritos,id_producto_fa,id_usuario_fa)
                        VALUES (%s,%s, %s)
                    """, [id,id_producto_pro, id_usuario])
                is_favorite = True

            connection.commit()

    return redirect('productos')

# Mostrar Productos
def productos(request):
    if request.user.is_authenticated:
        user_id = request.user.id_usuario_usu 
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM favoritos where id_usuario_fa = %s",[user_id])
            column_names = [col[0] for col in cursor.description]
            favoritos = [
                dict(zip(column_names, row))
                for row in cursor.fetchall()
            ]
    else:
        user_id = None  # Manejar el caso de usuario anónimo
        favoritos = []
    

    with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM productos where estado_pro = 1")
            column_names = [col[0] for col in cursor.description]
            productos = [
                dict(zip(column_names, row))
                for row in cursor.fetchall()
            ] 
            cursor.execute("SELECT resenas.id_resena_re,resenas.id_producto_re,resenas.resena_re,usuarios.nombre_usu FROM resenas inner join usuarios on resenas.id_usuario_re = usuarios.id_usuario_usu")
            column_names = [col[0] for col in cursor.description]
            resenas = [
                dict(zip(column_names, row))
                for row in cursor.fetchall()
            ]
            
        
    return render(request, 'Productos.html', {'productosquerry': productos,'resenasquerry':resenas,'favoritosquerry':favoritos,'user_id':user_id})
#Administrar Productos
def crearproducto(request):
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.execute("SELECT MAX(ID_PRODUCTO_PRO) FROM productos")
            max_id = cursor.fetchone()[0]
            id_producto = 1 if max_id is None else max_id + 1


        nombre = request.POST.get('nombre_pro')
        descripcion = request.POST.get('descripcion_pro')
        precio = request.POST.get('precio_pro')
        cantidad = request.POST.get('stock_pro')
        estado = request.POST.get('estado_pro')
        foto = request.FILES.get('foto_pro')
        categoria = request.POST.get('categoria_pro')
        
        

        # Validar que todos los campos obligatorios tengan contenido
        if not id_producto or not nombre or not precio or not cantidad or not foto or not estado or not categoria or not descripcion:
            messages.error(request, f'Todos los campos son obligatorios')
            print("Mensaje de error: Todos los campos son obligatorios")
            return redirect('crearproducto')

        try:
            # Intenta convertir precios y cantidades
            precio = int(float(precio.replace(',', '.')))
            cantidad = int(cantidad)
            estado = int(estado)
        except ValueError:
            messages.error(request, 'Formato de número incorrecto')
            print("Mensaje de error: Formato de número incorrecto")
            return redirect('crearproducto')

        try:
            # Guardar la imagen y crear el producto
            foto_path = default_storage.save(os.path.join('productos', foto.name), ContentFile(foto.read()))
            print(f"Foto guardada en: {foto_path}")

            # Verificar si el producto ya existe
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM productos WHERE id_producto_pro = %s", [id_producto])
                row = cursor.fetchone()
                if row is not None:
                    messages.error(request, 'Producto Ya existe')
                    print("Mensaje de error: Producto Ya existe")
                    return redirect('crearproducto')

                # Insertar el nuevo producto
                cursor.execute(""" 
                    INSERT INTO productos (id_producto_pro, nombre_pro, descripcion_pro, precio_pro, existencia_pro, foto_pro, estado_pro, categoria_pro_id) 
                    VALUES (%s, %s, %s, %s, %s ,%s, %s ,%s)
                """, [id_producto, nombre, descripcion, precio, cantidad, foto_path, estado, categoria])
                connection.commit()

            messages.success(request, 'Producto Creado Correctamente')
            print("Mensaje de éxito: Producto Creado Correctamente")
            return redirect('productosadmin')

        except IntegrityError as e:
            messages.error(request, f'Error al crear el producto')
            print("Mensaje de error: Error al crear el producto")
            return redirect('crearproducto')
        except Exception as e:
            messages.error(request, f'Error al crear el producto')
            print("Mensaje de error: Error al crear el producto")
            return redirect('crearproducto')
    elif request.method == 'GET':
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM categorias")
            column_names = [col[0] for col in cursor.description]

            categoria = [
                dict(zip(column_names, row))
                for row in cursor.fetchall()
            ]
   
    return render(request, 'CrearProductos.html', {'categorias': categoria})

def productosadmin(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM productos ORDER BY id_producto_pro")
        column_names = [col[0] for col in cursor.description]
        productos = [
            dict(zip(column_names, row))
            for row in cursor.fetchall()
        ]
        cursor.execute("SELECT * FROM categorias")
        column_names = [col[0] for col in cursor.description]
    
        categoria =[
            dict(zip(column_names, row))
            for row in cursor.fetchall()
        ]
        
        print(productos)
        print(categoria)

        return render(request, 'AdminProductos.html', {'productos': productos,'categoria':categoria})
def producto_detalles(request, id_producto_pro):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM productos WHERE id_producto_pro = %s", [id_producto_pro])
        row = cursor.fetchone()
        if row is None:
            raise Http404("Producto no existe")
        producto = {
            'id_producto_pro': row[0],
            'nombre_pro': row[1],
            'descripcion_pro': row[2],
            'existencia_pro': row[3],
            'precio_pro': row[4],
            'foto_pro': row[5],
            'estado_pro': row[6],
            'categoria_pro': row[7]

        }
        cursor.execute("SELECT * FROM categorias")
        column_names = [col[0] for col in cursor.description]
    
        categoria =[
            dict(zip(column_names, row))
            for row in cursor.fetchall()
        ]
        
    producto['estado_pro'] = bool(int(producto['estado_pro']))
       
    
        

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'Actualizar':
            
            id_producto_pro = request.POST.get('id_producto')
            nombre = request.POST.get('nombre_pro')
            descripcion = request.POST.get('descripcion_pro')
            precio = int(request.POST.get('precio_pro').split(',')[0])
            existencias = int(request.POST.get('existencia_pro'))
            categoriainput = request.POST.get('categoria_pro')
            estado = 1 if request.POST.get('estado_pro') == 'on' else 0
            foto = request.FILES.get('foto_pro')  # Obtener el archivo subido
            
              # Iterar sobre cada diccionario en la lista
            # Encontrar el elemento en la lista de categorías que coincide con categoriainput
            categoria_encontrada = next((item for item in categoria if item['NOMBRE_CAT'] == categoriainput), None)


            print(id_producto_pro,nombre, descripcion, precio, existencias, categoria_encontrada, estado, foto)


            if categoria_encontrada:
                valor = categoria_encontrada['ID_CATEGORIA_CAT']
                print("Soy un valor", valor)
            else:
                print("Categoría no encontrada")
                
            if foto is None:
                
                with connection.cursor() as cursor:
                    cursor.execute("""
                        UPDATE productos
                        SET nombre_pro = %s,
                        descripcion_pro = %s,
                        precio_pro = %s,
                        existencia_pro = %s,
                        categoria_pro_id = %s,
                        estado_pro = %s
                        WHERE id_producto_pro = %s
                    """, [nombre, descripcion, precio, existencias, valor, estado, id_producto_pro])
                    print("Producto Actualizado Correctamente")
                    connection.commit()
                
                
                with connection.cursor() as cursor:
                    cursor.execute("SELECT * FROM productos WHERE id_producto_pro = %s", [id_producto_pro])
                    row = cursor.fetchone()
                    if row is None:
                        messages.error(request, 'Producto no encontrado')
                    producto = {
                        'id_producto_pro': row[0],
                        'nombre_pro': row[1],
                        'descripcion_pro': row[2],
                        'existencia_pro': row[3],
                        'precio_pro': row[4],
                        'foto_pro': row[5],
                        'estado_pro': row[6],
                        'categoria_pro': row[7]
                    }

               
                producto['estado_pro'] = bool(int(producto['estado_pro']))
                
                return render(request, 'ProductoDetalles.html', {'producto': producto,'categoria':categoria})
            else:
                ruta_foto = os.path.join(settings.BASE_DIR, 'Media', 'productos', foto.name)
                with open(ruta_foto, 'wb+') as destination:
                    for chunk in foto.chunks():
                        destination.write(chunk)
                foto_path = f'productos/{foto.name}'
                print (foto.name)
                with connection.cursor() as cursor:
                    cursor.execute("""
                        UPDATE productos
                        SET nombre_pro = %s,
                        descripcion_pro = %s,
                        precio_pro = %s,
                        existencia_pro = %s,
                        categoria_pro_id = %s,
                        estado_pro = %s,
                        foto_pro = %s
                        WHERE id_producto_pro = %s
                    """, [nombre, descripcion, precio, existencias, valor, estado, foto_path, id_producto_pro])
                    connection.commit()
              
                
                with connection.cursor() as cursor:
                    cursor.execute("SELECT * FROM productos WHERE id_producto_pro = %s", [id_producto_pro])
                    row = cursor.fetchone()

                    print(row)
                    if row is None:
                        messages.error(request, 'Producto no encontrado')

                    producto = {
                        'id_producto_pro': row[0],
                        'nombre_pro': row[1],
                        'descripcion_pro': row[2],
                        'existencia_pro': row[3],
                        'precio_pro': row[4],
                        'foto_pro': row[5],
                        'estado_pro': row[6],
                        'categoria_pro': row[7]
                    }

                return render(request, 'ProductoDetalles.html', {'producto': producto,'categoria':categoria})
        elif action == 'Eliminar':
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM productos WHERE id_producto_pro = %s", [id_producto_pro])
                connection.commit()

            return redirect('productosadmin')
    return render(request, 'ProductoDetalles.html', {'producto': producto,'categoria':categoria})
#Administrar Categorias
def categoriasadmin(request):
    
   with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM categorias")
        column_names = [col[0] for col in cursor.description]
        categorias = [
            dict(zip(column_names, row))
            for row in cursor.fetchall()
        ]
        return render(request, 'CategoriasAdmin.html', {'categorias': categorias})
def categoria_detalles(request, id_categoria_cat):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM categorias WHERE id_categoria_cat = %s", [id_categoria_cat])
        row = cursor.fetchone()
        if row is None:
            raise Http404("Categoria no existe")
        categoria = {
            'id_categoria_cat': row[0],
            'nombre_cat': row[1],
            'descripcion_cat': row[2]
            # Añade aquí los demás campos de tu tabla de categorías
        }
        

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'Actualizar':
            nombre = request.POST.get('nombre_cat')
            descripcion = request.POST.get('descripcion_cat')
            # Recoge aquí los demás campos de tu formulario de categorías

            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE categorias
                    SET nombre_cat = %s,
                    descripcion_cat = %s
                    WHERE id_categoria_cat = %s
                """, [nombre,descripcion, id_categoria_cat])
                connection.commit()
                messages.error(request, 'Categoria Actualizada Correctamente')

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM categorias WHERE id_categoria_cat = %s", [id_categoria_cat])
                row = cursor.fetchone()
                if row is None:
                    messages.error(request, 'Categoria Actualizada Correctamente')
                categoria = {
                    'id_categoria_cat': row[0],
                    'nombre_cat': row[1],
                    'descripcion_cat': row[2]
                    # Añade aquí los demás campos de tu tabla de categorías
                }
            return render(request, 'CategoriaDetalles.html', {'categoria': categoria})

        elif action == 'Eliminar':
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM categorias WHERE id_categoria_cat = %s", [id_categoria_cat])
                connection.commit()

            return redirect('categoriasadmin')

    return render(request, 'CategoriaDetalles.html', {'categoria': categoria})


def crearcategoria(request):
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.execute("SELECT MAX(ID_CATEGORIA_CAT) FROM categorias")
            max_id = cursor.fetchone()[0]
            next_id = 1 if max_id is None else max_id + 1

        nombre = request.POST.get('nombre_cat')
        descripcion = request.POST.get('descripcion_cat')

        if not nombre or not descripcion:
            messages.error(request, 'Todos los campos son obligatorios')
            print("Todos los campos son obligatorios")
            return redirect('crearcategoria')
        

        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO categorias (id_categoria_cat, nombre_cat, descripcion_cat)
                    VALUES (%s, %s, %s)
                """, [next_id, nombre, descripcion])
                connection.commit()
            messages.success(request, 'Categoria Creada Correctamente')
            return redirect('categoriasadmin')
        except IntegrityError as e:
            if 'ORA-00001' in str(e):
                messages.error(request, 'La categoría ya existe')
            else:
                messages.error(request, f'Error al crear la categoría')
            return redirect('crearcategoria')
        except Exception as e:
            messages.error(request, f'Error al crear la categoría')
            return redirect('crearcategoria')

    return render(request, 'CrearCategoria.html')
