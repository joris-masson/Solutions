@echo off
cd %cd%/../src
javac -d ../build -cp .;../lib/constraintstests.jar constraints/*.java
pause