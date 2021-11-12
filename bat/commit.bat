@echo off
D:

for /d %%i in (D:\work\gitee\document\*) do (
cd %%i
IF EXIST .git (
echo %%i
git add .
git commit -m "bat commit ..."
git push origin master
echo.
)
cd ..
) 
pause
exit



