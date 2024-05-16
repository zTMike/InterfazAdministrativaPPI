DROP TABLE detalles_ordenes;
DROP TABLE ordenes;
DROP TABLE productos;
DROP TABLE categorias;
DROP TABLE usuarios;


-- Tabla productos_categoria
CREATE TABLE categorias (
  id_categoria_cat NUMBER(10) NOT NULL CHECK(id_categoria_cat > 0),
  nombre_cat VARCHAR2(50) NOT NULL,
  descripcion_cat VARCHAR2(255) NOT NULL,
  PRIMARY KEY (id_categoria_cat)
) TABLESPACE lamarquesabd;

-- Tabla productos_producto
CREATE TABLE productos (
  id_producto_pro NUMBER(10) NOT NULL CHECK(id_producto_pro > 0),
  nombre_pro VARCHAR2(50) NOT NULL,
  descripcion_pro VARCHAR2(255) NOT NULL,
  existencia_pro NUMBER(10) NOT NULL,
  precio_pro NUMBER(10, 2) NOT NULL,
  foto_pro VARCHAR2(75) NOT NULL,
  estado_pro VARCHAR2(1) NOT NULL,
  categoria_pro_id NUMBER(10) NOT NULL,
  PRIMARY KEY (id_producto_pro)
) TABLESPACE lamarquesabd;

-- Tabla usuarios_usuario
CREATE TABLE usuarios (
  id_usuario_usu NUMBER(10) NOT NULL CHECK(id_usuario_usu > 0),
  nombre_usu VARCHAR2(50) NOT NULL,
  apellido_usu VARCHAR2(50) NOT NULL,
  correo_usu VARCHAR2(50) NOT NULL UNIQUE,
  telefono_usu VARCHAR2(15),
  password VARCHAR2(128) NOT NULL,
  last_login DATE,
  is_active VARCHAR2(1) NOT NULL,
  is_staff VARCHAR2(1) NOT NULL,
  PRIMARY KEY (id_usuario_usu)
) TABLESPACE lamarquesabd;

-- Tabla ventas_orde_venta
CREATE TABLE ordenes (
  id_orden_ord NUMBER(10) NOT NULL CHECK(id_orden_ord > 0),
  fecha_ord DATE NOT NULL,
  total_ord NUMBER(10) NOT NULL,
  estado_ord VARCHAR2(1) NOT NULL,
  id_usuario_ord NUMBER(10) NOT NULL,
  PRIMARY KEY (id_orden_ord)
) TABLESPACE lamarquesabd;

-- Tabla ventas_detalle_orden
CREATE TABLE detalles_ordenes (
  id_detalle_det NUMBER(10) NOT NULL CHECK(id_detalle_det > 0),
  cantidad_det NUMBER(10) NOT NULL,
  cantidad_entregada_det NUMBER(10) NOT NULL,
  precio_det NUMBER(10, 2) NOT NULL,
  subtotal_det NUMBER(10, 2) NOT NULL,
  id_producto_det_id NUMBER(10) NOT NULL,
  id_orden_det_id NUMBER(10) NOT NULL,
  PRIMARY KEY (id_detalle_det)
) TABLESPACE lamarquesabd;