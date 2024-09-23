connect system/0000

show con_name

ALTER SESSION SET CONTAINER=CDB$ROOT;
ALTER DATABASE OPEN;

DROP TABLESPACE lamarquesabd INCLUDING CONTENTS and DATAFILES;
    
CREATE TABLESPACE lamarquesabd LOGGING
DATAFILE 'C:\Users\zTMike\Desktop\Semestre3\BaseDeDatos\Bases\lamarquesa.dbf' size 50M
extent management local segment space management auto; 
 
alter session set "_ORACLE_SCRIPT"=true; 
 
drop user adminmarquesa cascade;
SELECT tablespace_name FROM dba_tablespaces WHERE tablespace_name = 'LAMARQUESABD';
    
CREATE user adminmarquesa profile 
default identified by 31415926
default tablespace lamarquesabd 
temporary tablespace temp 
account unlock;     

--privilegios
grant connect, resource,dba to adminmarquesa; 

connect adminmarquesa/31415926

show user

