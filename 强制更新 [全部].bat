@echo off

set GIT_EXE=.\PortableGit\bin\git.exe

echo Pull Tools ...
%GIT_EXE% stash
%GIT_EXE% pull origin main

set GIT_EXE=..\PortableGit\bin\git.exe

echo Pull DicePP ...
cd ./DicePP
%GIT_EXE% stash
%GIT_EXE% pull origin master

echo Pull Python ...
cd ../Python
%GIT_EXE% stash
%GIT_EXE% pull origin main

pause