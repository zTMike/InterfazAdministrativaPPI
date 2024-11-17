DROP TABLE detalles_carritos;
DROP TABLE detalles_ordenes;
DROP TABLE carritos;
DROP TABLE ordenes;
DROP TABLE productos;
DROP TABLE categorias;
DROP TABLE usuarios;


CREATE TABLE categorias (
  id_categoria_cat NUMBER(10) NOT NULL,
  nombre_cat VARCHAR2(50) NOT NULL,
  descripcion_cat VARCHAR2(255) NOT NULL
) TABLESPACE lamarquesabd;

CREATE TABLE productos ( 
  id_producto_pro NUMBER(10) NOT NULL,
  nombre_pro VARCHAR2(50) NOT NULL,
  descripcion_pro VARCHAR2(255) NOT NULL,
  existencia_pro NUMBER(10) NOT NULL,
  precio_pro NUMBER(10, 2) NOT NULL,
  foto_pro VARCHAR2(75) NOT NULL,
  estado_pro NUMBER(1) NOT NULL,
  categoria_pro_id NUMBER(10) NOT NULL
) TABLESPACE lamarquesabd;

CREATE TABLE usuarios (
  id_usuario_usu NUMBER(15) NOT NULL,
  nombre_usu VARCHAR2(50) NOT NULL,
  apellido_usu VARCHAR2(50) NOT NULL,
  correo_usu VARCHAR2(50) NOT NULL,
  telefono_usu VARCHAR2(15),
  password VARCHAR2(128) NOT NULL,
  last_login DATE,
  is_active NUMBER(1) NOT NULL,
  is_staff NUMBER(1) NOT NULL
) TABLESPACE lamarquesabd;

CREATE TABLE ordenes (
  id_orden_ord NUMBER(10) NOT NULL,
  fecha_ord DATE NOT NULL,
  total_ord NUMBER(10),
  estado_ord VARCHAR2(1) NOT NULL,
  id_usuario_ord NUMBER(10) NOT NULL
) TABLESPACE lamarquesabd;



CREATE TABLE detalles_ordenes (
  id_detalle_det NUMBER(10) NOT NULL,
  cantidad_det NUMBER(10) NOT NULL,
  cantidad_entregada_det NUMBER(10) NOT NULL,
  precio_det NUMBER(10, 2) NOT NULL,
  subtotal_det NUMBER(10, 2) NOT NULL,
  id_producto_det_id NUMBER(10) NOT NULL,
  id_orden_det_id NUMBER(10) NOT NULL
) TABLESPACE lamarquesabd;

CREATE TABLE carritos (
  id_carrito_car NUMBER(10) NOT NULL,
  total_car NUMBER(10),
  id_usuario_car NUMBER(10) NOT NULL
) TABLESPACE lamarquesabd;

ALTER TABLE carritos 
    ADD(id_cupon NUMBER(10),
     estado NUMBER(1));

ALTER TABLE ordenes
 ADD(PRECIO_DESCUENTO NUMBER(10, 2),
      porcentaje  DECIMAL(5, 4));


CREATE TABLE detalles_carritos (
  id_detalle_dcar NUMBER(10) NOT NULL,
  cantidad_dcar NUMBER(10) NOT NULL,
  precio_dcar NUMBER(10, 2) NOT NULL,
  subtotal_dcar NUMBER(10, 2) NOT NULL,
  id_producto_dcar NUMBER(10) NOT NULL,
  id_carrito_dcar NUMBER(10) NOT NULL,
  nombre_producto_dcar VARCHAR2(50) NOT NULL
) TABLESPACE lamarquesabd;


CREATE TABLE resenas (
  id_resena_re NUMBER(10) NOT NULL,
  id_producto_re NUMBER(10) NOT NULL,
  id_usuario_re NUMBER(10) NOT NULL,
  resena_re VARCHAR2(255) NOT NULL
) TABLESPACE lamarquesabd;

CREATE TABLE favoritos (
  id_favoritos NUMBER(10) NOT NULL,
  id_producto_fa NUMBER(10) NOT NULL,
  id_usuario_fa NUMBER(10) NOT NULL
) TABLESPACE lamarquesabd;

CREATE TABLE cupones (
  id_cupon NUMBER(10) NOT NULL PRIMARY KEY,
  cod VARCHAR2(20) UNIQUE NOT NULL,
  cant NUMBER(10) NOT NULL,
  porcentaje  DECIMAL(5, 4) NOT NULL,
  estado NUMBER(1)
)