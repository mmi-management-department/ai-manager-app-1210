# WEB公開ガイド 🌐

このドキュメントでは、社内情報特化型生成AI検索アプリをWEBで公開する方法を説明します。

## 📋 目次

1. [現在の状態](#現在の状態)
2. [ローカルネットワークでの公開](#ローカルネットワークでの公開)
3. [Streamlit Cloudでの公開](#streamlit-cloudでの公開)
4. [その他のデプロイオプション](#その他のデプロイオプション)
5. [セキュリティ設定](#セキュリティ設定)

---

## 🎯 現在の状態

アプリは既に起動しており、以下のURLでアクセス可能です：

- **ローカル**: http://localhost:8501
- **社内ネットワーク**: http://192.168.3.178:8501
- **外部アクセス**: http://36.240.126.113:8501

### ⚠️ 注意事項

- 外部URLは、ルーターのポートフォワーディング設定が必要です
- 社内ネットワークURLは、同じネットワーク内のユーザーのみアクセス可能です
- セキュリティのため、認証機能が有効になっています

---

## 🏢 ローカルネットワークでの公開

### 現在の設定

アプリは既に社内ネットワークで公開されています：

```
Network URL: http://192.168.3.178:8501
```

### 社内の他のユーザーがアクセスする方法

1. 同じWi-Fiネットワークに接続
2. ブラウザで `http://192.168.3.178:8501` にアクセス
3. パスワードを入力してログイン

### ファイアウォール設定（必要な場合）

Windowsファイアウォールでポート8501を開放する必要がある場合：

```powershell
# PowerShellを管理者として実行
New-NetFirewallRule -DisplayName "Streamlit App" -Direction Inbound -Protocol TCP -LocalPort 8501 -Action Allow
```

---

## ☁️ Streamlit Cloudでの公開

Streamlit Cloudは、Streamlitアプリを無料で公開できるサービスです。

### 📝 事前準備

1. **GitHubアカウント**が必要です
2. **プロジェクトをGitHubにプッシュ**する必要があります
3. **APIキー**を準備します

### 🚀 デプロイ手順

#### ステップ 1: GitHubリポジトリの準備

```bash
# 既にGitリポジトリがある場合はスキップ
git init
git add .
git commit -m "Initial commit for web deployment"

# GitHubにプッシュ
git remote add origin https://github.com/your-username/your-repo-name.git
git push -u origin main
```

#### ステップ 2: 機密情報の除外確認

`.gitignore`ファイルで以下が除外されていることを確認してください：

```
.env
.streamlit/secrets.toml
API_KEYS_ACTUAL.md
data/03_社内規程・ルール/
data/04_管理資料/
vectorstore/
logs/
```

#### ステップ 3: Streamlit Cloudでのデプロイ

1. **Streamlit Cloudにアクセス**: https://share.streamlit.io/
2. **GitHubアカウントでサインイン**
3. **「New app」をクリック**
4. **リポジトリ情報を入力**:
   - Repository: `your-username/your-repo-name`
   - Branch: `main`
   - Main file path: `main.py`
5. **「Deploy」をクリック**

#### ステップ 4: Secrets（APIキー）の設定

1. デプロイしたアプリの**Settings**に移動
2. **Secrets**セクションを開く
3. 以下の内容をコピー＆ペースト（実際のAPIキーに置き換え）:

```toml
# Google Gemini API Key（必須）
GOOGLE_API_KEY = "AIzaSyCVOryUeFaYf1n8Oun9wAh9RxGYD4MkKuY"

# OpenAI API Key（オプション）
OPENAI_API_KEY = "your-openai-api-key-here"

# 認証設定
[auth]
password = "your_secure_password_here"
session_timeout_minutes = 60
max_login_attempts = 3
```

4. **Save**をクリック

#### ステップ 5: ベクターストアのアップロード

Streamlit Cloudでは、ベクターストアを事前に作成してGitHubにプッシュする必要があります：

```bash
# ベクターストアを作成
scripts\deployment\create_vectorstore_openai.bat

# .gitignoreからvectorstoreを一時的に削除
# vectorstore/をコミット
git add vectorstore/
git commit -m "Add vectorstore for deployment"
git push
```

**⚠️ 注意**: ベクターストアには社内情報が含まれる可能性があるため、プライベートリポジトリを使用してください。

---

## 🔧 その他のデプロイオプション

### オプション 1: Heroku

Herokuは、Pythonアプリケーションをホスティングできるプラットフォームです。

**必要なファイル**:
- `Procfile`
- `runtime.txt`（既に存在）
- `requirements.txt`（既に存在）

**Procfile**を作成:

```
web: streamlit run main.py --server.port=$PORT --server.address=0.0.0.0
```

**デプロイコマンド**:

```bash
heroku login
heroku create your-app-name
git push heroku main
```

### オプション 2: AWS EC2

AWS EC2インスタンスでアプリをホスティングできます。

**手順**:
1. EC2インスタンスを作成（Ubuntu推奨）
2. Python環境をセットアップ
3. アプリをクローン
4. 依存関係をインストール
5. Streamlitを起動

**起動スクリプト**:

```bash
#!/bin/bash
cd /path/to/app
source env/bin/activate
streamlit run main.py --server.port=8501 --server.address=0.0.0.0
```

### オプション 3: Docker

Dockerコンテナでアプリをデプロイできます。

**Dockerfile**を作成:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

**ビルドと実行**:

```bash
docker build -t ai-search-app .
docker run -p 8501:8501 ai-search-app
```

---

## 🔒 セキュリティ設定

### 認証機能

アプリには強化された認証機能が実装されています：

- ✅ パスワード認証
- ✅ ログイン試行回数制限（6時間以内に3回まで）
- ✅ セッションタイムアウト（デフォルト: 60分）
- ✅ アクセスログ記録
- ✅ XSRF保護

### パスワードの変更

`.streamlit/secrets.toml`または環境変数で設定:

```toml
[auth]
password = "新しい強力なパスワード"
```

### IPホワイトリスト（オプション）

特定のIPアドレスからのみアクセスを許可:

```toml
[auth]
ip_whitelist = "192.168.1.1,192.168.1.2,203.0.113.0"
```

### HTTPS化

本番環境では、必ずHTTPSを使用してください：

- **Streamlit Cloud**: 自動的にHTTPSが有効
- **Heroku**: 自動的にHTTPSが有効
- **独自サーバー**: Nginx + Let's Encryptを使用

**Nginx設定例**:

```nginx
server {
    listen 80;
    server_name your-domain.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl;
    server_name your-domain.com;

    ssl_certificate /etc/letsencrypt/live/your-domain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/your-domain.com/privkey.pem;

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
    }
}
```

---

## 📊 監視とメンテナンス

### ログの確認

アプリのログは以下の場所に保存されます：

- `logs/application.log` - アプリケーションログ
- `logs/access_log.json` - アクセスログ

### パフォーマンス監視

Streamlit Cloudでは、ダッシュボードでパフォーマンスを監視できます：

- メモリ使用量
- CPU使用量
- リクエスト数
- エラー率

### 定期的なメンテナンス

- **週次**: ログファイルのサイズを確認
- **月次**: 依存関係の更新を確認
- **四半期**: セキュリティ監査

---

## 🆘 トラブルシューティング

### アプリが起動しない

```bash
# ログを確認
cat logs/application.log

# 依存関係を再インストール
pip install -r requirements.txt --force-reinstall
```

### メモリ不足エラー

Streamlit Cloudの無料プランはメモリ制限があります：

- ベクターストアのサイズを削減
- チャンクサイズを調整
- 不要なファイルを削除

### 接続エラー

- ファイアウォール設定を確認
- ポート8501が開放されているか確認
- ネットワーク設定を確認

---

## 📞 サポート

問題が発生した場合：

1. **ログを確認**: `logs/application.log`
2. **ドキュメントを参照**: `docs/`フォルダ内のガイド
3. **Streamlit公式ドキュメント**: https://docs.streamlit.io/

---

## ✅ デプロイチェックリスト

- [ ] GitHubリポジトリを作成
- [ ] 機密情報を`.gitignore`に追加
- [ ] ベクターストアを作成
- [ ] `requirements.txt`を確認
- [ ] Streamlit Cloudにデプロイ
- [ ] Secretsを設定
- [ ] 認証機能をテスト
- [ ] 本番環境でテスト
- [ ] HTTPSを確認
- [ ] ログ監視を設定

---

**最終更新**: 2025-12-15

