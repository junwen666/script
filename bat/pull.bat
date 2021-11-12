@echo off
D:
for /d %%i in (D:\work\gitee\document\*) do (
cd %%i
IF EXIST .git (
echo %%i
git pull
echo.
)
cd ..
) 
pause
exit