-- Crea una restricción de clave primaria en la columna id_categoria_cat de la tabla categorias
ALTER TABLE categorias
ADD CONSTRAINT categorias_pk PRIMARY KEY (id_categoria_cat);

-- Asegura que el valor de id_categoria_cat en la tabla categorias siempre sea mayor que 0
ALTER TABLE categorias
ADD CONSTRAINT categorias_check CHECK (id_categoria_cat > 0);

-- Crea una restricción de clave primaria en la columna id_producto_pro de la tabla productos
ALTER TABLE productos
ADD CONSTRAINT productos_pk PRIMARY KEY (id_producto_pro);

-- Asegura que el valor de id_producto_pro en la tabla productos siempre sea mayor que 0
ALTER TABLE productos
ADD CONSTRAINT productos_check CHECK (id_producto_pro > 0);

-- Crea una restricción de clave foránea en la columna categoria_pro_id de la tabla productos que hace referencia a id_categoria_cat en la tabla categorias
ALTER TABLE productos
ADD CONSTRAINT fk_categorias FOREIGN KEY (categoria_pro_id) REFERENCES categorias(id_categoria_cat);

-- Crea una restricción de clave primaria en la columna id_usuario_usu de la tabla usuarios
ALTER TABLE usuarios
ADD CONSTRAINT usuarios_pk PRIMARY KEY (id_usuario_usu);

-- Asegura que el valor de id_usuario_usu en la tabla usuarios siempre sea mayor que 0
ALTER TABLE usuarios
ADD CONSTRAINT usuarios_check CHECK (id_usuario_usu > 0);

-- Asegura que el valor de correo_usu en la tabla usuarios siempre sea único
ALTER TABLE usuarios
ADD CONSTRAINT usuarios_unique UNIQUE (correo_usu);

-- Crea una restricción de clave primaria en la columna id_orden_ord de la tabla ordenes
ALTER TABLE ordenes
ADD CONSTRAINT ordenes_pk PRIMARY KEY (id_orden_ord);

-- Asegura que el valor de id_orden_ord en la tabla ordenes siempre sea mayor que 0
ALTER TABLE ordenes
ADD CONSTRAINT ordenes_check CHECK (id_orden_ord > 0);

-- Crea una restricción de clave foránea en la columna id_usuario_ord de la tabla ordenes que hace referencia a id_usuario_usu en la tabla usuarios
ALTER TABLE ordenes
ADD CONSTRAINT fk_usuarios FOREIGN KEY (id_usuario_ord) REFERENCES usuarios(id_usuario_usu);

-- Crea una restricción de clave primaria en la columna id_detalle_det de la tabla detalles_ordenes
ALTER TABLE detalles_ordenes
ADD CONSTRAINT detalles_ordenes_pk PRIMARY KEY (id_detalle_det);

-- Asegura que el valor de id_detalle_det en la tabla detalles_ordenes siempre sea mayor que 0
ALTER TABLE detalles_ordenes
ADD CONSTRAINT detalles_ordenes_check CHECK (id_detalle_det > 0);

-- Crea una restricción de clave foránea en la columna id_producto_det_id de la tabla detalles_ordenes que hace referencia a id_producto_pro en la tabla productos
ALTER TABLE detalles_ordenes
ADD CONSTRAINT fk_productos FOREIGN KEY (id_producto_det_id) REFERENCES productos(id_producto_pro);

-- Crea una restricción de clave foránea en la columna id_orden_det_id de la tabla detalles_ordenes que hace referencia a id_orden_ord en la tabla ordenes
ALTER TABLE detalles_ordenes
ADD CONSTRAINT fk_ordenes FOREIGN KEY (id_orden_det_id) REFERENCES ordenes(id_orden_ord);

-- Crea una restricción de clave primaria en la columna id_carrito_car de la tabla carritos
ALTER TABLE carritos
ADD CONSTRAINT carritos_pk PRIMARY KEY (id_carrito_car);

-- Asegura que el valor de id_carrito_car en la tabla carritos siempre sea mayor que 0
ALTER TABLE carritos
ADD CONSTRAINT carritos_check CHECK (id_carrito_car > 0);

-- Crea una restricción de clave foránea en la columna id_usuario_car de la tabla carritos que hace referencia a id_usuario_usu en la tabla usuarios
ALTER TABLE carritos
ADD CONSTRAINT fk_usuarios_car FOREIGN KEY (id_usuario_car) REFERENCES usuarios(id_usuario_usu);

-- Asegura que el valor de id del usuario en la tabla carrito siempre sea único
ALTER TABLE carritos
ADD CONSTRAINT carritosUsuario_unique UNIQUE (id_usuario_car);

-- Crea una restricción de clave primaria en la columna id_detalle_dcar de la tabla detalles_carritos
ALTER TABLE detalles_carritos
ADD CONSTRAINT detalles_carritos_pk PRIMARY KEY (id_detalle_dcar);

-- Asegura que el valor de id_detalle_dcar en la tabla detalles_carritos siempre sea mayor que 0
ALTER TABLE detalles_carritos
ADD CONSTRAINT detalles_carritos_check CHECK (id_detalle_dcar > 0);

-- Crea una restricción de clave foránea en la columna id_producto_dcar_id de la tabla detalles_carritos que hace referencia a id_producto_pro en la tabla productos
ALTER TABLE detalles_carritos
ADD CONSTRAINT fk_productos_dcar FOREIGN KEY (id_producto_dcar) REFERENCES productos(id_producto_pro);

-- Crea una restricción de clave foránea en la columna id_carrito_det_id de la tabla detalles_carrito que hace referencia a id_carrito en la tabla carrito
ALTER TABLE detalles_carritos
ADD CONSTRAINT fk_carrito FOREIGN KEY (id_carrito_dcar) REFERENCES carritos(id_carrito_car);

-- Crea una restricción de clave primaria en la columna id_resena_re de la tabla resenas
ALTER TABLE resenas
ADD CONSTRAINT pk_resenas PRIMARY KEY (id_resena_re);

-- Crea una restricción de clave foránea en la columna id_producto_re de la tabla resenas que hace referencia a id_producto_pro en la tabla productos
ALTER TABLE resenas
ADD CONSTRAINT fk_productos_resenas FOREIGN KEY (id_producto_re) REFERENCES productos(id_producto_pro);

-- Crea una restricción de clave foránea en la columna id_usuario_re de la tabla resenas que hace referencia a id_usuario_usu en la tabla usuarios
ALTER TABLE resenas
ADD CONSTRAINT fk_usuarios_resenas FOREIGN KEY (id_usuario_re) REFERENCES usuarios(id_usuario_usu);
