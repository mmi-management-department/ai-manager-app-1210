@echo off
chcp 65001 > nul
echo ========================================
echo Google Cloud Runへのデプロイ
echo ========================================
echo.

REM プロジェクトIDを設定（必要に応じて変更してください）
set PROJECT_ID=ai-manager-app-2024
set REGION=asia-northeast1
set SERVICE_NAME=ai-manager-app

echo プロジェクトID: %PROJECT_ID%
echo リージョン: %REGION%
echo サービス名: %SERVICE_NAME%
echo.

echo ステップ1: Google Cloudにログイン
echo.
gcloud auth login
if errorlevel 1 (
    echo エラー: ログインに失敗しました
    pause
    exit /b 1
)

echo.
echo ステップ2: プロジェクトの作成（既に存在する場合はスキップされます）
echo.
gcloud projects create %PROJECT_ID% --set-as-default
gcloud config set project %PROJECT_ID%

echo.
echo ステップ3: 必要なAPIの有効化
echo.
gcloud services enable run.googleapis.com
gcloud services enable containerregistry.googleapis.com
gcloud services enable artifactregistry.googleapis.com
gcloud services enable cloudbuild.googleapis.com

echo.
echo ステップ4: Artifact Registryリポジトリの作成
echo.
gcloud artifacts repositories create ai-manager-repo ^
  --repository-format=docker ^
  --location=%REGION% ^
  --description="AI Manager App Repository"

echo.
echo ステップ5: Docker認証の設定
echo.
gcloud auth configure-docker %REGION%-docker.pkg.dev

echo.
echo ステップ6: Cloud Buildを使用してイメージをビルド＆デプロイ
echo （これには5〜10分かかる場合があります）
echo.
gcloud run deploy %SERVICE_NAME% ^
  --source . ^
  --platform managed ^
  --region %REGION% ^
  --allow-unauthenticated ^
  --port 8501 ^
  --memory 2Gi ^
  --cpu 2 ^
  --timeout 300 ^
  --env-vars-file env.yaml

if errorlevel 1 (
    echo.
    echo エラー: デプロイに失敗しました
    echo ログを確認してください
    pause
    exit /b 1
)

echo.
echo ========================================
echo デプロイが完了しました！
echo ========================================
echo.
echo サービスURLを確認しています...
gcloud run services describe %SERVICE_NAME% --region %REGION% --format "value(status.url)"
echo.
echo 上記のURLにアクセスしてアプリを使用できます
echo.
pause

