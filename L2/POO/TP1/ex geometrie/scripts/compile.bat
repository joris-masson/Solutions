@echo off
cd %cd%/../src
javac -d ../build -cp .;../lib/geometrytests.jar geometry/*.java
pause