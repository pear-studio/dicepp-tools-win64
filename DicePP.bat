@echo off
cd .\DicePP
set PYTHON_EXE=..\Python\python.exe
set GIT_PYTHON_REFRESH=quiet
%PYTHON_EXE% bot.py
pause