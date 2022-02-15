@echo off

echo Switch to Gitee ...

set GIT_EXE=.\PortableGit\bin\git.exe

set DPP_GITEE_PATH=https://github.com/pear-studio/nonebot-dicepp.git
set DPP_PY_GITEE_PATH=https://github.com/pear-studio/dicepp-python-win64.git
set DPP_TOOL_GITEE_PATH=https://github.com/pear-studio/dicepp-tools-win64.git

echo Change Tool Repo
cd ..
%GIT_EXE% remote set-url origin %DPP_TOOL_GITEE_PATH%

set GIT_EXE=..\PortableGit\bin\git.exe

echo Change Python Repo
cd ./Python
%GIT_EXE% remote set-url origin %DPP_PY_GITEE_PATH%

echo Change DicePP Repo
cd ../DicePP 
%GIT_EXE% remote set-url origin %DPP_GITEE_PATH%

pause