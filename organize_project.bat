@echo off
chcp 65001 > nul
echo ============================================================
echo プロジェクト構造の整理
echo ============================================================
echo.

echo [1/6] フォルダ作成中...
if not exist config mkdir config
if not exist docs mkdir docs
if not exist docs\guides mkdir docs\guides
if not exist docs\summaries mkdir docs\summaries  
if not exist docs\deployment mkdir docs\deployment
if not exist scripts mkdir scripts
if not exist scripts\setup mkdir scripts\setup
if not exist scripts\deployment mkdir scripts\deployment
if not exist scripts\utils mkdir scripts\utils
if not exist requirements mkdir requirements
echo ✓ フォルダ作成完了

echo.
echo [2/6] 設定ファイルを移動中...
move /Y google_drive_config.json.template config\ 2>nul
move /Y google_drive_security_config.json.template config\ 2>nul
move /Y env_template.txt config\ 2>nul
echo ✓ 設定ファイル移動完了

echo.
echo [3/6] ドキュメントを移動中...
REM ガイド類
move /Y *_GUIDE.md docs\guides\ 2>nul
move /Y *_SETUP.md docs\guides\ 2>nul
move /Y CHEAT_SHEET.md docs\guides\ 2>nul
move /Y FAQ.md docs\guides\ 2>nul
move /Y QUICK_START_FOR_USERS.md docs\guides\ 2>nul

REM サマリー類
move /Y *_SUMMARY.md docs\summaries\ 2>nul

REM デプロイ関連
move /Y *DEPLOYMENT*.md docs\deployment\ 2>nul
move /Y *DEPLOY*.md docs\deployment\ 2>nul

REM API関連
move /Y API_KEYS_REFERENCE.md docs\ 2>nul
move /Y API_KEYS_SETUP_GUIDE.md docs\guides\ 2>nul

echo ✓ ドキュメント移動完了

echo.
echo [4/6] スクリプトを移動中...
REM セットアップスクリプト
move /Y install_*.bat scripts\setup\ 2>nul
move /Y setup_*.py scripts\setup\ 2>nul
move /Y fix_*.bat scripts\setup\ 2>nul

REM デプロイスクリプト
move /Y deploy_*.bat scripts\deployment\ 2>nul
move /Y create_vectorstore*.bat scripts\deployment\ 2>nul
move /Y create_vectorstore*.py scripts\deployment\ 2>nul

REM ユーティリティスクリプト
move /Y switch_*.bat scripts\utils\ 2>nul
move /Y git_*.bat scripts\utils\ 2>nul
move /Y push_*.bat scripts\utils\ 2>nul
move /Y create_tag_only.bat scripts\utils\ 2>nul
move /Y start_app_web.bat scripts\utils\ 2>nul

echo ✓ スクリプト移動完了

echo.
echo [5/6] 依存関係ファイルを移動中...
move /Y requirements_*.txt requirements\ 2>nul
echo ✓ 依存関係ファイル移動完了

echo.
echo [6/6] テストスクリプトを移動中...
move /Y test_*.py scripts\utils\ 2>nul
echo ✓ テストスクリプト移動完了

echo.
echo ============================================================
echo ✅ プロジェクト整理完了！
echo ============================================================
echo.
echo 新しい構造:
echo   /config/          - 設定ファイル
echo   /docs/           - ドキュメント
echo   /scripts/        - スクリプト
echo   /requirements/   - 依存関係
echo   /assets/images/  - 画像ファイル
echo.
pause

