@echo off

echo Switch to Gitee ...

set GIT_EXE=..\PortableGit\bin\git.exe

set DPP_GITEE_PATH=https://gitee.com/pear_studio/nonebot-dicepp.git
set DPP_PY_GITEE_PATH=https://gitee.com/pear_studio/dicepp-python-win64.git
set DPP_TOOL_GITEE_PATH=https://gitee.com/pear_studio/dicepp-tools-win64.git

cd ..
%GIT_EXE% remote set-url origin %DPP_TOOL_GITEE_PATH%
cd ./Python
%GIT_EXE% remote set-url origin %DPP_PY_GITEE_PATH%
cd ../DicePP 
%GIT_EXE% remote set-url origin %DPP_GITEE_PATH%

pause