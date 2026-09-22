@echo off
chcp 65001 >nul
setlocal EnableExtensions

rem Source auto-detect: v2 extracted, warna v1 wala folder bhi chalega
set "SRC1=F:\Downloads\muskan-birthday-surprise-v2\muskan-birthday"
set "SRC2=F:\Downloads\muskan-birthday-surprise\muskan-birthday"
if exist "%SRC1%\docs\index.html" (
  set "SRC=%SRC1%"
) else (
  set "SRC=%SRC2%"
)
set "REPO=F:\Desktop\Birthday Wish\Birthday-s-wish"

echo.
echo  ============================================
echo   Step 1/4 : Purani files delete ho rahi hain
echo  ============================================
if not exist "%REPO%\.git" (
  echo  GALTI! "%REPO%" me .git nahi mila - yeh repo ka folder nahi lagta.
  echo  Pehle repo clone karo: git clone https://github.com/Sumitrajput-1234/Birthday-s-wish.git
  pause
  exit /b 1
)
rd /s /q "%REPO%\c" 2>nul
rd /s /q "%REPO%\c++" 2>nul
rd /s /q "%REPO%\.vscode" 2>nul
echo  Purana junk (c, c++, .vscode) clear ho gaya.

echo.
echo  ============================================
echo   Step 2/4 : Naya birthday site code copy ho raha hai
echo  ============================================
if not exist "%SRC%\docs\index.html" (
  echo  GALTI! Source folder nahi mila. Yeh dono jagah dekh gaya:
  echo    %SRC1%
  echo    %SRC2%
  echo  Zip F:\Downloads\ me extract karna zaroori hai.
  pause
  exit /b 1
)
robocopy "%SRC%" "%REPO%" /E /NFL /NDL /NJH /NJS
rem robocopy exit 0,1,2 = sab theek. 4 ya upar = fail.
if errorlevel 4 (
  echo  ROBOCOPY FAIL! Upar error dekho.
  pause
  exit /b 1
)
echo  Naya code copy ho gaya (docs + .github).

echo.
echo  ============================================
echo   Step 3/4 : Git commit
echo  ============================================
cd /d "%REPO%"
git add .
git commit -m "Muskan's interactive birthday surprise"
if errorlevel 1 (
  echo  Commit me dikkat aayi - neeche ka message dekho.
  pause
  exit /b 1
)

echo.
echo  ============================================
echo   Step 4/4 : GitHub pe push
echo  ============================================
git push
if errorlevel 1 (
  echo  PUSH FAIL! Git credentials ka issue ho sakta hai -
  echo  ek baar manually "git push" karke password/token daal do.
  pause
  exit /b 1
)

echo.
echo  ============================================
echo   DONE! Ab ek baar ka kaam:
echo   GitHub repo -^> Settings -^> Pages -^> Source: GitHub Actions
echo   ~1 min me site live:
echo   https://sumitrajput-1234.github.io/Birthday-s-wish/
echo  ============================================
pause
