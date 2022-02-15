@echo off

echo Switch to Gitee ...

set DPP_GITEE_PATH=https://gitee.com/pear_studio/nonebot-dicepp.git
set DPP_PY_GITEE_PATH=https://gitee.com/pear_studio/dicepp-python-win64.git
set DPP_TOOL_GITEE_PATH=https://gitee.com/pear_studio/dicepp-tools-win64.git

cd ..
git remote set-url main %DPP_TOOL_GITEE_PATH%
cd ./Python
git remote set-url main %DPP_PY_GITEE_PATH%
cd ../DicePP 
git remote set-url master %DPP_GITEE_PATH%