@echo off
set FILEPATH = %~dp0
sc start mariaDB

cd %FILEPATH%
cd AllDayLong\src\frontend
call npm install
npm run serve
pause