@echo off
setlocal
set DB_USER=root
set DB_PASS=0000
set DB_NAME=ppi_lamarqueza
set BACKUP_PATH=C:\Users\zTMike\Desktop\Semestre3\ConstruccionWeb\InterfazAdministrativa2
set TIMESTAMP=%date:~-4,4%%date:~-10,2%%date:~-7,2%_%time:~0,2%%time:~3,2%%time:~6,2%
set USERNAME=%USERNAME%
"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysqldump.exe" -u%DB_USER% -p%DB_PASS% %DB_NAME% > "%BACKUP_PATH%\%DB_NAME%_%TIMESTAMP%_%USERNAME%.sql"
endlocal