@echo off

set GIT_EXE=.\PortableGit\bin\git.exe

echo Pull Tools ...
%GIT_EXE% pull origin main

pause