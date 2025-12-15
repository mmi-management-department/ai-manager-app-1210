# デプロイチェックリスト ✅

このチェックリストを使用して、WEB公開の準備が整っているか確認してください。

## 📋 デプロイ前の確認事項

### 1. コードとファイルの準備

- [ ] すべての機能が正常に動作することを確認
- [ ] ローカル環境でテスト済み（http://localhost:8501）
- [ ] エラーログを確認（`logs/application.log`）
- [ ] 不要なファイルを削除
- [ ] コメントとドキュメントを整理

### 2. セキュリティチェック

- [ ] `.gitignore`に機密情報が含まれていることを確認
  - [ ] `.env`
  - [ ] `.streamlit/secrets.toml`
  - [ ] `API_KEYS_ACTUAL.md`
  - [ ] `data/03_社内規程・ルール/`（機密情報）
  - [ ] `data/04_管理資料/`（機密情報）
  - [ ] `logs/`
- [ ] APIキーが直接コードに含まれていないことを確認
- [ ] パスワードが強力であることを確認
- [ ] 認証機能が有効であることを確認

### 3. 依存関係の確認

- [ ] `requirements.txt`が最新であることを確認
- [ ] すべての依存関係がインストール可能であることを確認
- [ ] `runtime.txt`でPythonバージョンを指定（python-3.11）

### 4. ベクターストアの準備

- [ ] ベクターストアを作成済み（`vectorstore/`フォルダ）
- [ ] ベクターストアのサイズを確認（大きすぎる場合は最適化）
- [ ] 公開情報のみが含まれていることを確認

### 5. 設定ファイルの確認

- [ ] `.streamlit/config.toml`が適切に設定されている
- [ ] `.streamlit/secrets.toml.template`が用意されている
- [ ] `Procfile`が作成されている（Heroku用）
- [ ] `packages.txt`が作成されている（Streamlit Cloud用）

---

## 🚀 Streamlit Cloudデプロイ手順

### ステップ 1: GitHubリポジトリの準備

```bash
# 1. Gitリポジトリを初期化（まだの場合）
git init

# 2. すべてのファイルをステージング
git add .

# 3. コミット
git commit -m "Prepare for web deployment"

# 4. GitHubリポジトリを作成（ブラウザで）
# https://github.com/new

# 5. リモートリポジトリを追加
git remote add origin https://github.com/your-username/your-repo-name.git

# 6. プッシュ
git push -u origin main
```

**⚠️ 重要**: リポジトリは**プライベート**に設定してください！

### ステップ 2: Streamlit Cloudでデプロイ

1. **Streamlit Cloudにアクセス**: https://share.streamlit.io/
2. **GitHubでサインイン**
3. **「New app」をクリック**
4. **リポジトリ情報を入力**:
   ```
   Repository: your-username/your-repo-name
   Branch: main
   Main file path: main.py
   ```
5. **「Advanced settings」をクリック**
6. **Python version**: 3.11を選択
7. **「Deploy」をクリック**

### ステップ 3: Secretsの設定

1. デプロイしたアプリの**Settings** → **Secrets**に移動
2. 以下の内容を貼り付け（実際のAPIキーに置き換え）:

```toml
# Google Gemini API Key（必須）
GOOGLE_API_KEY = "AIzaSyCVOryUeFaYf1n8Oun9wAh9RxGYD4MkKuY"

# OpenAI API Key（オプション）
OPENAI_API_KEY = "your-openai-api-key-here"

# 認証設定（必須）
[auth]
password = "your_secure_password_here"
session_timeout_minutes = 60
max_login_attempts = 3
```

3. **Save**をクリック

### ステップ 4: デプロイ完了の確認

- [ ] アプリが正常に起動
- [ ] ログイン画面が表示される
- [ ] パスワード認証が機能する
- [ ] 検索機能が正常に動作する
- [ ] ソース表示が正常に動作する

---

## 🏢 社内ネットワークでの公開（現在の状態）

### 現在のアクセスURL

アプリは既に以下のURLでアクセス可能です：

- **ローカル**: http://localhost:8501
- **社内ネットワーク**: http://192.168.3.178:8501
- **外部**: http://36.240.126.113:8501

### 社内ユーザーへの共有方法

1. **URLを共有**: http://192.168.3.178:8501
2. **パスワードを共有**（安全な方法で）
3. **使い方ガイドを共有**（`docs/guides/`フォルダ内）

### ファイアウォール設定（必要な場合）

```powershell
# PowerShellを管理者として実行
New-NetFirewallRule -DisplayName "Streamlit App" -Direction Inbound -Protocol TCP -LocalPort 8501 -Action Allow
```

---

## 🔧 Herokuデプロイ手順

### 事前準備

- [ ] Herokuアカウントを作成
- [ ] Heroku CLIをインストール

### デプロイ手順

```bash
# 1. Herokuにログイン
heroku login

# 2. Herokuアプリを作成
heroku create your-app-name

# 3. 環境変数を設定
heroku config:set GOOGLE_API_KEY="your-google-api-key"
heroku config:set OPENAI_API_KEY="your-openai-api-key"

# 4. デプロイ
git push heroku main

# 5. アプリを開く
heroku open
```

---

## 🐳 Dockerデプロイ手順

### Dockerfileの作成

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# 依存関係をインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリをコピー
COPY . .

# ポートを公開
EXPOSE 8501

# Streamlitを起動
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### ビルドと実行

```bash
# 1. Dockerイメージをビルド
docker build -t ai-search-app .

# 2. コンテナを実行
docker run -p 8501:8501 \
  -e GOOGLE_API_KEY="your-google-api-key" \
  -e OPENAI_API_KEY="your-openai-api-key" \
  ai-search-app

# 3. ブラウザで確認
# http://localhost:8501
```

---

## 📊 デプロイ後の確認事項

### 機能テスト

- [ ] ログイン機能
- [ ] 検索機能（複数のキーワードでテスト）
- [ ] ソース表示
- [ ] ファイルタイプの表示
- [ ] 管理画面（アクセス権限がある場合）
- [ ] ログアウト機能

### パフォーマンステスト

- [ ] 初回読み込み速度
- [ ] 検索レスポンス時間
- [ ] 複数ユーザーの同時アクセス
- [ ] メモリ使用量

### セキュリティテスト

- [ ] 未認証アクセスのブロック
- [ ] ログイン試行回数制限
- [ ] セッションタイムアウト
- [ ] HTTPS接続（本番環境）

---

## 🆘 トラブルシューティング

### よくある問題と解決方法

#### 1. アプリが起動しない

**原因**: 依存関係の問題

**解決方法**:
```bash
pip install -r requirements.txt --force-reinstall
```

#### 2. メモリ不足エラー

**原因**: ベクターストアが大きすぎる

**解決方法**:
- ベクターストアのサイズを削減
- `constants.py`で`CHUNK_SIZE`を調整
- 不要なファイルを`data/`から削除

#### 3. 認証エラー

**原因**: Secretsが正しく設定されていない

**解決方法**:
- Streamlit CloudのSecretsを確認
- パスワードが正しく設定されているか確認

#### 4. 検索結果が表示されない

**原因**: ベクターストアが読み込まれていない

**解決方法**:
- ベクターストアを再作成
- ログを確認（`logs/application.log`）

#### 5. ファイルが表示されない

**原因**: ファイルパスの問題

**解決方法**:
- `data/`フォルダの構造を確認
- ファイルがGitHubにプッシュされているか確認

---

## 📞 サポート

### ドキュメント

- **メインガイド**: `WEB_DEPLOYMENT_GUIDE.md`
- **クイックスタート**: `QUICK_START.md`
- **セキュリティ**: `docs/SECURITY_CHECKLIST.md`

### ログの確認

```bash
# アプリケーションログ
cat logs/application.log

# アクセスログ
cat logs/access_log.json
```

### Streamlit公式リソース

- **公式ドキュメント**: https://docs.streamlit.io/
- **コミュニティフォーラム**: https://discuss.streamlit.io/
- **GitHub**: https://github.com/streamlit/streamlit

---

## ✅ 最終チェックリスト

デプロイ前に、すべての項目をチェックしてください：

### コード

- [ ] すべての機能が動作する
- [ ] エラーがない
- [ ] ログが適切に出力される

### セキュリティ

- [ ] 機密情報が除外されている
- [ ] 認証が有効
- [ ] HTTPSが有効（本番環境）

### デプロイ

- [ ] GitHubにプッシュ済み
- [ ] Streamlit Cloudでデプロイ済み
- [ ] Secretsが設定済み

### テスト

- [ ] ログイン機能
- [ ] 検索機能
- [ ] パフォーマンス
- [ ] セキュリティ

### ドキュメント

- [ ] README.mdが最新
- [ ] デプロイガイドが用意されている
- [ ] ユーザーガイドが用意されている

---

**デプロイ日**: _______________

**デプロイ担当者**: _______________

**URL**: _______________

**パスワード**: _______________（安全に保管）

---

**最終更新**: 2025-12-15

