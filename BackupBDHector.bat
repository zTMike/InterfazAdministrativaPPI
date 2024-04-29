@echo off
setlocal
set DB_USER=UsuarioSQL
set DB_PASS=ClaveSQL
set DB_NAME=NombreDelaBD
set BACKUP_PATH=RutaDondeTienesGaardadoElProyecto
set TIMESTAMP=%date:~-4,4%%date:~-10,2%%date:~-7,2%_%time:~0,2%%time:~3,2%%time:~6,2%
set USERNAME=%USERNAME%
echo BorraEstaLinea pero abajo debes poner ese archivo. exe debes de buscarlo en tu pc en mi caso estaba en esa ruta 
"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysqldump.exe" -u%DB_USER% -p%DB_PASS% %DB_NAME% > "%BACKUP_PATH%\%DB_NAME%_%TIMESTAMP%_%USERNAME%.sql"
endlocal