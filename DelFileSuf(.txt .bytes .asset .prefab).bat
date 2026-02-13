@echo off
setlocal enabledelayedexpansion

echo ================================================
echo [INFO] Delete .txt .bytes .asset .prefab suffixes
echo ================================================

REM process multiple extensions
for %%E in (txt bytes asset prefab) do (
    for /r %%F in (*.%%E) do (
        set "FULLPATH=%%~fF"
        set "DIR=%%~dpF"
        set "NAME=%%~nF"

        echo [RENAME] %%~nxF ^> !NAME!
        ren "%%F" "!NAME!"
    )
)

echo ================================================
echo [DONE] All specified suffixes were removed!
pause