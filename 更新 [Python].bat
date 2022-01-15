@echo off

set GIT_EXE=..\PortableGit\bin\git.exe

echo Pull Python ...
cd ../Python
%GIT_EXE% pull origin main

pause