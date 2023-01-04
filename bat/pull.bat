@echo off

for /d %%i in (*) do (
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