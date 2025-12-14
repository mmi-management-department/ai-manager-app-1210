@echo off
chcp 65001 > nul
echo ============================================================
echo dataフォルダとdata_backupフォルダの統合
echo ============================================================
echo.

echo [1/5] 統合フォルダ構造を作成中...
mkdir data_integrated 2>nul
mkdir "data_integrated\01_会社情報" 2>nul
mkdir "data_integrated\02_事業・サービス" 2>nul
mkdir "data_integrated\03_MTG議事録" 2>nul
mkdir "data_integrated\03_MTG議事録\社内会議" 2>nul
mkdir "data_integrated\03_MTG議事録\顧客会議" 2>nul
mkdir "data_integrated\04_社内規程・ルール" 2>nul
mkdir "data_integrated\05_顧客情報" 2>nul
mkdir "data_integrated\06_管理資料" 2>nul
echo 完了: フォルダ構造を作成しました
echo.

echo [2/5] 会社情報をコピー中...
xcopy "data\会社について" "data_integrated\01_会社情報\" /E /I /Y /Q
echo 完了: 会社情報をコピーしました
echo.

echo [3/5] 事業・サービス情報をコピー中...
xcopy "data\メディアについて" "data_integrated\02_事業・サービス\" /E /I /Y /Q
echo 完了: 事業・サービス情報をコピーしました
echo.

echo [4/5] MTG議事録をコピー中...
xcopy "data\MTG議事録" "data_integrated\03_MTG議事録\社内会議\" /E /I /Y /Q
xcopy "data_backup\MTG議事録_顧客" "data_integrated\03_MTG議事録\顧客会議\" /E /I /Y /Q
echo 完了: MTG議事録をコピーしました
echo.

echo [5/5] 社内規程・ルールと管理資料をコピー中...
xcopy "data_backup\規則規程について" "data_integrated\04_社内規程・ルール\規則規程\" /E /I /Y /Q
xcopy "data_backup\既読規程以外の社内ルールについて" "data_integrated\04_社内規程・ルール\その他ルール\" /E /I /Y /Q
xcopy "data\顧客について" "data_integrated\05_顧客情報\" /E /I /Y /Q
xcopy "data_backup\ファイルについて" "data_integrated\06_管理資料\" /E /I /Y /Q
echo 完了: 社内規程・ルールと管理資料をコピーしました
echo.

echo ============================================================
echo 統合完了！
echo ============================================================
echo.
echo 新しいフォルダ構造:
echo   data_integrated\
echo   ├── 01_会社情報\
echo   ├── 02_事業・サービス\
echo   ├── 03_MTG議事録\
echo   │   ├── 社内会議\
echo   │   └── 顧客会議\
echo   ├── 04_社内規程・ルール\
echo   │   ├── 規則規程\
echo   │   └── その他ルール\
echo   ├── 05_顧客情報\
echo   └── 06_管理資料\
echo.
echo 次のステップ:
echo 1. data_integratedフォルダの内容を確認
echo 2. 問題なければ、以下を実行:
echo    - 古いdataフォルダをdata_oldにリネーム
echo    - data_integratedをdataにリネーム
echo    - data_backupフォルダを削除またはアーカイブ
echo.
pause

