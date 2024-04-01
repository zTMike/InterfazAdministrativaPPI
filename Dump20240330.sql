-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: ppi_lamarqueza
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add detalle_orden',7,'add_detalle_orden'),(26,'Can change detalle_orden',7,'change_detalle_orden'),(27,'Can delete detalle_orden',7,'delete_detalle_orden'),(28,'Can view detalle_orden',7,'view_detalle_orden'),(29,'Can add orde_venta',8,'add_orde_venta'),(30,'Can change orde_venta',8,'change_orde_venta'),(31,'Can delete orde_venta',8,'delete_orde_venta'),(32,'Can view orde_venta',8,'view_orde_venta'),(33,'Can add producto',9,'add_producto'),(34,'Can change producto',9,'change_producto'),(35,'Can delete producto',9,'delete_producto'),(36,'Can view producto',9,'view_producto'),(37,'Can add categoria',10,'add_categoria'),(38,'Can change categoria',10,'change_categoria'),(39,'Can delete categoria',10,'delete_categoria'),(40,'Can view categoria',10,'view_categoria'),(41,'Can add tipo usuario',11,'add_tipousuario'),(42,'Can change tipo usuario',11,'change_tipousuario'),(43,'Can delete tipo usuario',11,'delete_tipousuario'),(44,'Can view tipo usuario',11,'view_tipousuario'),(45,'Can add usuario',12,'add_usuario'),(46,'Can change usuario',12,'change_usuario'),(47,'Can delete usuario',12,'delete_usuario'),(48,'Can view usuario',12,'view_usuario');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$720000$ewEruPbvdgPo4eCme4TyBp$wVCu6QtDCMndlZJrIuyjbGBc8L6KXtog85fXVRHCHdU=','2024-03-30 17:47:58.448629',1,'ztmike','','','ztmike.yt@gmail.com',1,1,'2024-03-29 15:05:39.142958'),(2,'pbkdf2_sha256$720000$zMOAivj18CLvT7ZGB5be0T$+g8uh74CRTdzzWzFcOVfO8JPfc0azl4Ur7UEyVooLnA=',NULL,0,'he.fa.g.i@hotmail.com','','','he.fa.g.i@hotmail.com',0,1,'2024-03-30 16:06:19.431198');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2024-03-29 15:28:39.338563','1','Administrador',1,'[{\"added\": {}}]',11,1),(2,'2024-03-29 15:29:07.133988','1','Hector Fabio',1,'[{\"added\": {}}]',12,1),(3,'2024-03-29 15:32:22.041429','4','Fertilizantes',1,'[{\"added\": {}}]',10,1),(4,'2024-03-29 15:34:59.476290','1','Abono AAA 50Kg',1,'[{\"added\": {}}]',9,1),(5,'2024-03-29 15:41:52.854998','2','2',1,'[{\"added\": {}}]',8,1),(6,'2024-03-29 16:26:51.074068','1234991936','1234991936',2,'[{\"changed\": {\"fields\": [\"Id usuario usu\"]}}]',12,1),(7,'2024-03-29 16:32:28.884924','2','2',2,'[{\"changed\": {\"fields\": [\"Estado ven\"]}}]',8,1),(8,'2024-03-29 16:33:09.017818','3','3',1,'[{\"added\": {}}]',8,1),(9,'2024-03-29 16:36:43.726319','1','1',1,'[{\"added\": {}}]',7,1),(10,'2024-03-29 16:37:05.184609','1','1',2,'[{\"changed\": {\"fields\": [\"Cantidad ven\"]}}]',7,1),(11,'2024-03-29 16:38:11.727317','1','1',2,'[{\"changed\": {\"fields\": [\"Cantidad ven\"]}}]',7,1),(12,'2024-03-29 16:38:19.633290','1','1',2,'[{\"changed\": {\"fields\": [\"Cantidad ven\"]}}]',7,1),(13,'2024-03-29 20:28:02.618689','3','3',2,'[{\"changed\": {\"fields\": [\"Estado ord\"]}}]',8,1),(14,'2024-03-30 01:57:50.834247','2','Usuario',1,'[{\"added\": {}}]',11,1),(15,'2024-03-30 03:54:42.257485','1','Abono AAA 50Kg',2,'[{\"changed\": {\"fields\": [\"Foto\"]}}]',9,1),(16,'2024-03-30 12:51:25.233211','1','Abono AAA 50Kg',2,'[{\"changed\": {\"fields\": [\"Foto\"]}}]',9,1),(17,'2024-03-30 12:51:42.099507','1','Abono AAA 50Kg',2,'[{\"changed\": {\"fields\": [\"Foto\"]}}]',9,1),(18,'2024-03-30 13:42:54.647772','1','Abono AAA 50Kg',2,'[{\"changed\": {\"fields\": [\"Estado\"]}}]',9,1),(19,'2024-03-30 13:43:34.697832','1','Abono AAA 50Kg',2,'[{\"changed\": {\"fields\": [\"Estado\"]}}]',9,1),(20,'2024-03-30 15:19:47.131606','1','Abono AAA 25Kg',2,'[{\"changed\": {\"fields\": [\"Nombre pro\", \"Descripcion pro\", \"Precio pro\", \"Foto\"]}}]',9,1),(21,'2024-03-30 15:19:59.412825','1','Abono AAA 25Kg',2,'[{\"changed\": {\"fields\": [\"Foto\"]}}]',9,1),(22,'2024-03-30 15:20:12.032247','1','Abono AAA 25Kg',2,'[{\"changed\": {\"fields\": [\"Estado\"]}}]',9,1),(23,'2024-03-30 15:20:40.815706','1','Abono AAA 25Kg',2,'[{\"changed\": {\"fields\": [\"Estado\"]}}]',9,1),(24,'2024-03-30 15:22:13.586234','2','Abono AAA 50Kg',1,'[{\"added\": {}}]',9,1),(25,'2024-03-30 15:24:51.891046','2','Abono AAA 50Kg',2,'[{\"changed\": {\"fields\": [\"Estado\"]}}]',9,1),(26,'2024-03-30 15:25:00.451621','2','Abono AAA 50Kg',2,'[{\"changed\": {\"fields\": [\"Estado\"]}}]',9,1),(27,'2024-03-30 15:27:05.882521','1','Abono AAA 25Kg',2,'[{\"changed\": {\"fields\": [\"Estado\"]}}]',9,1),(28,'2024-03-30 15:27:09.585939','2','Abono AAA 50Kg',2,'[{\"changed\": {\"fields\": [\"Estado\"]}}]',9,1),(29,'2024-03-30 15:28:29.399545','1','Abono AAA 25Kg',2,'[{\"changed\": {\"fields\": [\"Estado\"]}}]',9,1),(30,'2024-03-30 15:28:29.402548','2','Abono AAA 50Kg',2,'[{\"changed\": {\"fields\": [\"Estado\"]}}]',9,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(10,'Productos','categoria'),(9,'Productos','producto'),(6,'sessions','session'),(11,'Usuarios','tipousuario'),(12,'Usuarios','usuario'),(7,'Ventas','detalle_orden'),(8,'Ventas','orde_venta');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-03-29 15:05:02.261643'),(2,'auth','0001_initial','2024-03-29 15:05:03.193404'),(3,'admin','0001_initial','2024-03-29 15:05:03.376226'),(4,'admin','0002_logentry_remove_auto_add','2024-03-29 15:05:03.391856'),(5,'admin','0003_logentry_add_action_flag_choices','2024-03-29 15:05:03.411007'),(6,'contenttypes','0002_remove_content_type_name','2024-03-29 15:05:03.521222'),(7,'auth','0002_alter_permission_name_max_length','2024-03-29 15:05:03.595886'),(8,'auth','0003_alter_user_email_max_length','2024-03-29 15:05:03.628991'),(9,'auth','0004_alter_user_username_opts','2024-03-29 15:05:03.647539'),(10,'auth','0005_alter_user_last_login_null','2024-03-29 15:05:03.747326'),(11,'auth','0006_require_contenttypes_0002','2024-03-29 15:05:03.751340'),(12,'auth','0007_alter_validators_add_error_messages','2024-03-29 15:05:03.759674'),(13,'auth','0008_alter_user_username_max_length','2024-03-29 15:05:03.878479'),(14,'auth','0009_alter_user_last_name_max_length','2024-03-29 15:05:03.989575'),(15,'auth','0010_alter_group_name_max_length','2024-03-29 15:05:04.017373'),(16,'auth','0011_update_proxy_permissions','2024-03-29 15:05:04.027665'),(17,'auth','0012_alter_user_first_name_max_length','2024-03-29 15:05:04.119301'),(18,'sessions','0001_initial','2024-03-29 15:05:04.184070'),(19,'Productos','0001_initial','2024-03-29 15:18:39.352166'),(20,'Usuarios','0001_initial','2024-03-29 15:18:39.492135'),(21,'Ventas','0001_initial','2024-03-29 15:18:39.916153'),(22,'Productos','0002_alter_producto_precio_pro','2024-03-29 15:33:45.936363'),(23,'Ventas','0002_alter_orde_venta_estado_ven_and_more','2024-03-29 15:40:48.482674'),(24,'Usuarios','0002_alter_usuario_id_usuario_usu','2024-03-29 20:10:39.175004'),(25,'Ventas','0003_alter_orde_venta_estado_ven','2024-03-29 20:10:39.267709'),(26,'Productos','0003_alter_producto_precio_pro','2024-03-29 20:24:52.908907'),(27,'Ventas','0004_rename_cantidad_ven_detalle_orden_cantidad_det_and_more','2024-03-29 20:24:53.493745'),(28,'Productos','0004_producto_foto','2024-03-30 03:54:05.572175'),(29,'Productos','0005_producto_estado','2024-03-30 13:02:26.503260');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('7lk1q9u71d1szi6nbj9qubf5y0mnqr27','.eJxVjDsOgzAQRO_iOrJs1j9SpucM1trrjUkikDBUUe4ekCiSaqR5b-YtIm5rjVsrSxxJXIUWl98uYX6W6QD0wOk-yzxP6zImeSjypE0OM5XX7XT_Diq2uq_ZdeQtcc9EoNBazQaSyQY5G_bc6Zyd61JvEPqiIHjcIwAkUCmgFp8v_u04Lg:1rqNtF:8EcOTsDdo3EJDCYYxwyRQW-yAMCy9C6yajs1Tc3KwaE','2024-04-13 01:52:13.579472'),('kq472v3z59t1xueczaoycp6nj793rmt4','.eJxVjDsOgzAQRO_iOrJs1j9SpucM1trrjUkikDBUUe4ekCiSaqR5b-YtIm5rjVsrSxxJXIUWl98uYX6W6QD0wOk-yzxP6zImeSjypE0OM5XX7XT_Diq2uq_ZdeQtcc9EoNBazQaSyQY5G_bc6Zyd61JvEPqiIHjcIwAkUCmgFp8v_u04Lg:1rqIn6:PGWQb5_wDzsRwhB6OcyXHwVaVChbvStPLvi3m0mFK7o','2024-04-12 20:25:32.984662'),('v17owcfjvs8z8h9hoae1rf10nkwe0zvw','.eJxVjDsOgzAQRO_iOrJs1j9SpucM1trrjUkikDBUUe4ekCiSaqR5b-YtIm5rjVsrSxxJXIUWl98uYX6W6QD0wOk-yzxP6zImeSjypE0OM5XX7XT_Diq2uq_ZdeQtcc9EoNBazQaSyQY5G_bc6Zyd61JvEPqiIHjcIwAkUCmgFp8v_u04Lg:1rqPmQ:HNcrXlHtPhHKb7E8aLikuHBX14UjDRkLUzmUD22MFBM','2024-04-13 03:53:18.295722');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productos_categoria`
--

DROP TABLE IF EXISTS `productos_categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productos_categoria` (
  `id_categoria_cat` int NOT NULL AUTO_INCREMENT,
  `nombre_cat` varchar(50) NOT NULL,
  `descripcion_cat` longtext NOT NULL,
  PRIMARY KEY (`id_categoria_cat`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos_categoria`
--

LOCK TABLES `productos_categoria` WRITE;
/*!40000 ALTER TABLE `productos_categoria` DISABLE KEYS */;
INSERT INTO `productos_categoria` VALUES (4,'Fertilizantes','Productos para enriquecer la tierra');
/*!40000 ALTER TABLE `productos_categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productos_producto`
--

DROP TABLE IF EXISTS `productos_producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productos_producto` (
  `id_producto_pro` int NOT NULL AUTO_INCREMENT,
  `nombre_pro` varchar(50) NOT NULL,
  `descripcion_pro` longtext NOT NULL,
  `existencia_pro` int NOT NULL,
  `precio_pro` int NOT NULL,
  `categoria_pro_id` int NOT NULL,
  `foto` varchar(100) DEFAULT NULL,
  `estado` tinyint(1) NOT NULL,
  PRIMARY KEY (`id_producto_pro`),
  KEY `Productos_producto_categoria_pro_id_1f0eb3e3_fk_Productos` (`categoria_pro_id`),
  CONSTRAINT `Productos_producto_categoria_pro_id_1f0eb3e3_fk_Productos` FOREIGN KEY (`categoria_pro_id`) REFERENCES `productos_categoria` (`id_categoria_cat`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos_producto`
--

LOCK TABLES `productos_producto` WRITE;
/*!40000 ALTER TABLE `productos_producto` DISABLE KEYS */;
INSERT INTO `productos_producto` VALUES (1,'Abono AAA 25Kg','abono AAA 25kg Plantas y arboles',200,22000,4,'productos/Semillas.jpg',1),(2,'Abono AAA 50Kg','Abono AAA 50Kg Fertiliza tu tierra',20,40000,4,'productos/Fertilizante_5FDhmkc.jpg',1);
/*!40000 ALTER TABLE `productos_producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios_tipousuario`
--

DROP TABLE IF EXISTS `usuarios_tipousuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios_tipousuario` (
  `id_tipoUsuario_tus` int NOT NULL AUTO_INCREMENT,
  `nombre_tus` varchar(50) NOT NULL,
  `descripcion_tus` longtext NOT NULL,
  PRIMARY KEY (`id_tipoUsuario_tus`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios_tipousuario`
--

LOCK TABLES `usuarios_tipousuario` WRITE;
/*!40000 ALTER TABLE `usuarios_tipousuario` DISABLE KEYS */;
INSERT INTO `usuarios_tipousuario` VALUES (1,'Administrador','Control total sobre la base de datos'),(2,'Usuario','Perfil que solo puede registrar productos y realizar compras');
/*!40000 ALTER TABLE `usuarios_tipousuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios_usuario`
--

DROP TABLE IF EXISTS `usuarios_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios_usuario` (
  `id_usuario_usu` int NOT NULL,
  `nombre_usu` varchar(50) NOT NULL,
  `apellido_usu` varchar(50) NOT NULL,
  `correo_usu` varchar(50) NOT NULL,
  `contrasena_usu` varchar(50) NOT NULL,
  `tipoUsuario_usu_id` int NOT NULL,
  PRIMARY KEY (`id_usuario_usu`),
  KEY `Usuarios_usuario_tipoUsuario_usu_id_bb082741_fk_Usuarios_` (`tipoUsuario_usu_id`),
  CONSTRAINT `Usuarios_usuario_tipoUsuario_usu_id_bb082741_fk_Usuarios_` FOREIGN KEY (`tipoUsuario_usu_id`) REFERENCES `usuarios_tipousuario` (`id_tipoUsuario_tus`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios_usuario`
--

LOCK TABLES `usuarios_usuario` WRITE;
/*!40000 ALTER TABLE `usuarios_usuario` DISABLE KEYS */;
INSERT INTO `usuarios_usuario` VALUES (1,'Hector Fabio','Garcia Isaza','ztmike.yt@gmail.com','1234991936',1),(1234991936,'Hector Fabio','Garcia Isaza','ztmike.yt@gmail.com','1234991936',1);
/*!40000 ALTER TABLE `usuarios_usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ventas_detalle_orden`
--

DROP TABLE IF EXISTS `ventas_detalle_orden`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ventas_detalle_orden` (
  `id_detalle_det` int NOT NULL AUTO_INCREMENT,
  `cantidad_det` int NOT NULL,
  `precio_det` decimal(9,2) NOT NULL,
  `subtotal_det` decimal(9,2) NOT NULL,
  `id_producto_det_id` int NOT NULL,
  `id_orden_det_id` int NOT NULL,
  PRIMARY KEY (`id_detalle_det`),
  KEY `Ventas_detalle_orden_id_orden_det_id_07dcb862_fk_Ventas_or` (`id_orden_det_id`),
  KEY `Ventas_detalle_orden_id_producto_det_id_de0f0ba8_fk_Productos` (`id_producto_det_id`),
  CONSTRAINT `Ventas_detalle_orden_id_orden_det_id_07dcb862_fk_Ventas_or` FOREIGN KEY (`id_orden_det_id`) REFERENCES `ventas_orde_venta` (`id_orden_ord`),
  CONSTRAINT `Ventas_detalle_orden_id_producto_det_id_de0f0ba8_fk_Productos` FOREIGN KEY (`id_producto_det_id`) REFERENCES `productos_producto` (`id_producto_pro`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ventas_detalle_orden`
--

LOCK TABLES `ventas_detalle_orden` WRITE;
/*!40000 ALTER TABLE `ventas_detalle_orden` DISABLE KEYS */;
INSERT INTO `ventas_detalle_orden` VALUES (1,1,20500.00,20500.00,1,3);
/*!40000 ALTER TABLE `ventas_detalle_orden` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ventas_orde_venta`
--

DROP TABLE IF EXISTS `ventas_orde_venta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ventas_orde_venta` (
  `id_orden_ord` int NOT NULL AUTO_INCREMENT,
  `fecha_ord` date NOT NULL,
  `total_ord` decimal(9,2) NOT NULL,
  `estado_ord` varchar(1) NOT NULL,
  `id_usuario_ord_id` int NOT NULL,
  PRIMARY KEY (`id_orden_ord`),
  KEY `Ventas_orde_venta_id_usuario_ord_id_05227147_fk_Usuarios_` (`id_usuario_ord_id`),
  CONSTRAINT `Ventas_orde_venta_id_usuario_ord_id_05227147_fk_Usuarios_` FOREIGN KEY (`id_usuario_ord_id`) REFERENCES `usuarios_usuario` (`id_usuario_usu`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ventas_orde_venta`
--

LOCK TABLES `ventas_orde_venta` WRITE;
/*!40000 ALTER TABLE `ventas_orde_venta` DISABLE KEYS */;
INSERT INTO `ventas_orde_venta` VALUES (2,'2024-03-29',0.00,'P',1),(3,'2024-03-29',0.00,'R',1234991936);
/*!40000 ALTER TABLE `ventas_orde_venta` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-30 13:21:02
