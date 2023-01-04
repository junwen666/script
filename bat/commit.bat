@echo off

for /d %%i in (*) do (
	cd %%i
	IF EXIST .git (
		echo %%i
		git add .
		git commit -m "auto commit ..."
		git push origin master
		echo.
	)
	cd ..
) 
pause
exit



