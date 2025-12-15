@echo off
chcp 65001 > nul
cd /d "%~dp0\..\..\"
echo ==========================================
echo デプロイ準備状況チェック
echo ==========================================
echo.
env\Scripts\python.exe scripts\utils\check_deployment_ready.py
echo.
pause

