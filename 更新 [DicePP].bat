@echo off

set GIT_EXE=..\PortableGit\bin\git.exe

echo Pull DicePP ...
cd ./DicePP
%GIT_EXE% pull origin master

pause