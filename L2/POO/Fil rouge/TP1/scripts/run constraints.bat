@echo off
cd %cd%/../src
java -cp ../build;../lib/constraintstests.jar constraints.Main
pause