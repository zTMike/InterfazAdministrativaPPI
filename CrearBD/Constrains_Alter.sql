-- Agregar Foreign Key a la tabla productos
ALTER TABLE productos
ADD CONSTRAINT fk_categorias
FOREIGN KEY (categoria_pro_id) REFERENCES categorias(id_categoria_cat);

-- Agregar Foreign Key a la tabla ordenes
ALTER TABLE ordenes
ADD CONSTRAINT fk_usuarios
FOREIGN KEY (id_usuario_ord) REFERENCES usuarios(id_usuario_usu);

-- Agregar Foreign Keys a la tabla detalles_ordenes
ALTER TABLE detalles_ordenes
ADD CONSTRAINT fk_productos
FOREIGN KEY (id_producto_det_id) REFERENCES productos(id_producto_pro);

ALTER TABLE detalles_ordenes
ADD CONSTRAINT fk_ordenes
FOREIGN KEY (id_orden_det_id) REFERENCES ordenes(id_orden_ord);