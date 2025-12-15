@echo off
chcp 65001 > nul
echo ========================================
echo Google Cloud SDK インストール
echo ========================================
echo.

echo Google Cloud SDKのインストーラーをダウンロードします...
echo.
echo ブラウザで以下のURLが開きます：
echo https://cloud.google.com/sdk/docs/install
echo.
echo インストール手順：
echo 1. "Windows用のインストーラー"をダウンロード
echo 2. インストーラーを実行
echo 3. すべてデフォルト設定でOK
echo 4. インストール完了後、PowerShellを再起動
echo.

start https://cloud.google.com/sdk/docs/install

echo.
echo インストーラーのダウンロードページを開きました。
echo インストール後、このウィンドウを閉じてください。
echo.
pause

