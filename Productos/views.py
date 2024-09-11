from django.shortcuts import render,redirect
from .views import *
from django.db import connection
from django.contrib import messages
from django.http import Http404
from django.conf import settings
import os
from django.contrib.auth.decorators import login_required

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

# Mostrar Productos
def productos(request):

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

        


        
        

        return render(request, 'Productos.html', {'productosquerry': productos,'resenasquerry':resenas})
#Administrar Productos
def crearproducto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre_pro')
        descripcion = request.POST.get('descripcion_pro')
        precio = int(float(request.POST.get('precio_pro').replace(',', '.')))
        stock = request.POST.get('stock_pro')
        categoria = request.POST.get('categoria_pro')
        foto = request.FILES.get('foto_pro')  # Obtener el archivo subido
        estado = 1 if request.POST.get('estado_pro') == 'on' else 0
        
        with connection.cursor() as cursor:
        
            cursor.execute("SELECT MAX(ID_PRODUCTO_PRO) FROM productos")
            max_id = cursor.fetchone()[0]

           
            id_producto_pro = 1 if max_id is None else max_id + 1

        
        if not nombre or not descripcion or not precio or not stock or not categoria  or not foto:
            messages.error(request, 'Todos los campos son obligatorios')
            return redirect('crearproducto')
        else:
            # Guardar el archivo subido en el directorio \Media\productos de tu proyecto
            ruta_foto = os.path.join(settings.BASE_DIR, 'Media', 'productos', foto.name)
            with open(ruta_foto, 'wb+') as destination:
                for chunk in foto.chunks():
                    destination.write(chunk)

            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO productos (id_producto_pro,nombre_pro, descripcion_pro, precio_pro, existencia_pro, categoria_pro_id,estado_pro,foto_pro)
                    VALUES (%s,%s, %s, %s, %s, %s, %s, %s)
                """, [id_producto_pro,nombre, descripcion, precio, stock, categoria, estado, foto.name])  # Guardar solo el nombre de la foto en la base de datos
                connection.commit()
            messages.success(request, 'Producto Creado Correctamente')
            return redirect('productosadmin')
    
    # Obtener todas las categorías
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM categorias")
        column_names = [col[0] for col in cursor.description]
        categorias = [
            dict(zip(column_names, row))
            for row in cursor.fetchall()
        ]

    # Pasar las categorías a la plantilla
    return render(request, 'CrearProductos.html', {'categorias': categorias})
def productosadmin(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM productos ORDER BY id_producto_pro")
        column_names = [col[0] for col in cursor.description]
        productos = [
            dict(zip(column_names, row))
            for row in cursor.fetchall()
        ]
        
        return render(request, 'AdminProductos.html', {'productos': productos})
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
    producto['estado_pro'] = bool(int(producto['estado_pro']))
       
        

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'Actualizar':
            nombre = request.POST.get('nombre_pro')
            descripcion = request.POST.get('descripcion_pro')
            precio = int(request.POST.get('precio_pro').split(',')[0])
            existencias = int(request.POST.get('existencia_pro'))
            categoria = request.POST.get('categoria_pro')
            estado = 1 if request.POST.get('estado_pro') == 'on' else 0
            foto = request.FILES.get('foto_pro')  # Obtener el archivo subido
            
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
                    """, [nombre, descripcion, precio, existencias, categoria, estado, id_producto_pro])
                    connection.commit()
                messages.success(request, 'Producto Actualizado Correctamente')
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
                return render(request, 'ProductoDetalles.html', {'producto': producto})
            else:
                ruta_foto = os.path.join(settings.BASE_DIR, 'Media', 'productos', foto.name)
                with open(ruta_foto, 'wb+') as destination:
                    for chunk in foto.chunks():
                        destination.write(chunk)

                

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
                    """, [nombre, descripcion, precio, existencias, categoria, estado, foto.name, id_producto_pro])
                    connection.commit()
                messages.success(request, 'Producto Actualizado Correctamente')
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
                    producto['estado_pro'] = bool(int(request.POST.get('estado_pro')))
                return render(request, 'ProductoDetalles.html', {'producto': producto})
        elif action == 'Eliminar':
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM productos WHERE id_producto_pro = %s", [id_producto_pro])
                connection.commit()

            return redirect('productosadmin')

    return render(request, 'ProductoDetalles.html', {'producto': producto})
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
            return redirect('crearcategoria')
        else:
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO categorias (id_categoria_cat,nombre_cat, descripcion_cat)
                    VALUES (%s, %s, %s)
                """, [next_id,nombre, descripcion])
                connection.commit()
            messages.success(request, 'Categoria Creada Correctamente')
            return redirect('categoriasadmin')
    return render(request, 'CrearCategoria.html')






