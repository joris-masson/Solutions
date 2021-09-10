@echo off
cd %cd%/../src
java -cp ../build;../lib/geometrytests.jar geometry.Main
pause