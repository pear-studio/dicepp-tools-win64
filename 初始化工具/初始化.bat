@echo off
set GIT_EXE=..\PortableGit\bin\git.exe
if not exist %GIT_EXE% (
    echo Need %GIT_EXE% !
    goto end
)

rem set GIT_PYTHON_GIT_EXECUTABLE %GIT_EXE%
set GIT_PYTHON_REFRESH=quiet
set PYTHON_EXE=..\Python\python.exe
if not exist %PYTHON_EXE% (
    echo Need %PYTHON_EXE% !
    goto end
)

%PYTHON_EXE% dicepp_build_tool.py

:end
pause