# 社内情報特化型生成AI検索アプリ

社内文書を検索・問い合わせできるRAG（Retrieval-Augmented Generation）ベースのStreamlitアプリケーションです。

## 機能

- **社内文書検索モード**: 入力内容と関連性が高い社内文書を検索
- **社内問い合わせモード**: 質問に対してAIが回答を生成し、参照文書を表示
- **パスワード認証**: 社内限定アクセス制御
- **アバター表示**: AI管理部長の動くアバター
- **Google Drive連携**: Google Driveからのファイル参照（オプション）

## 📁 プロジェクト構造

```
プロジェクトルート/
├── assets/images/        # 画像ファイル（ロゴ、アバター）
├── config/               # 設定ファイルテンプレート
├── docs/                 # ドキュメント
│   ├── guides/          # 各種ガイド
│   ├── summaries/       # 各種サマリー
│   └── deployment/      # デプロイ関連
├── scripts/              # スクリプト
│   ├── setup/           # セットアップスクリプト
│   ├── deployment/      # デプロイスクリプト
│   └── utils/           # ユーティリティスクリプト
├── requirements/         # 依存関係ファイル
├── data/                 # アプリが参照するデータ
└── *.py                  # メインPythonファイル
```

詳細は `docs/PROJECT_STRUCTURE.md` を参照してください。

## 技術スタック

- **フレームワーク**: Streamlit
- **LLM**: Google Gemini（無料版: gemini-1.5-flash）
- **ベクターストア**: ChromaDB
- **ドキュメント処理**: LangChain
- **対応ファイル形式**: PDF, DOCX, CSV, TXT

## ローカル環境でのセットアップ

### 前提条件

- Python 3.9以上
- Google Gemini APIキー（無料で取得可能）

### インストール手順

1. **リポジトリのクローン**

```bash
git clone <repository-url>
cd 社内情報特化型生成AI検索アプリ
```

2. **仮想環境の作成と有効化**

```bash
# Windows
python -m venv env
env\Scripts\activate

# Mac/Linux
python3 -m venv env
source env/bin/activate
```

3. **依存パッケージのインストール**

```bash
# Windows
pip install -r requirements/requirements_windows.txt

# Mac
pip install -r requirements_mac.txt

# または汎用版
pip install -r requirements.txt
```

4. **環境変数の設定**

`env.template` をコピーして `.env` ファイルを作成し、Google Gemini APIキーを設定します。

```bash
# Windowsの場合
copy env.template .env

# Mac/Linuxの場合
cp env.template .env
```

`.env` ファイルを編集して、実際のAPIキーを設定してください：

```
GOOGLE_API_KEY=your-actual-google-gemini-api-key-here
```

5. **データの配置**

`data/` ディレクトリに検索対象の文書を配置します。以下の構造を推奨：

```
data/
├── MTG議事録/
├── サービスについて/
├── 会社について/
└── 顧客について/
```

6. **アプリケーションの起動**

```bash
streamlit run main.py
```

ブラウザで `http://localhost:8501` が自動的に開きます。

## 🌐 WEB公開

### 🎯 現在の状態

アプリは既に起動しており、以下のURLでアクセス可能です：

- **ローカル**: http://localhost:8501
- **社内ネットワーク**: http://192.168.3.178:8501
- **外部**: http://36.240.126.113:8501（ポートフォワーディング設定が必要）

### 📚 詳細ガイド

- **クイックスタート**: `QUICK_START_WEB.md` - 最速でWEB公開する方法
- **完全ガイド**: `WEB_DEPLOYMENT_GUIDE.md` - すべてのデプロイオプション
- **チェックリスト**: `DEPLOY_CHECKLIST.md` - デプロイ前の確認事項

### 🏢 社内ネットワークで共有（最も簡単）

同じネットワーク内のユーザーに以下のURLを共有するだけです：

```
http://192.168.3.178:8501
```

**注意**: 
- 同じWi-Fiネットワークに接続している必要があります
- PCがシャットダウンするとアクセスできなくなります

### ☁️ Streamlit Cloudでデプロイ（推奨）

#### クイックスタート（5分）

1. **GitHubにプッシュ**
```bash
git add .
git commit -m "Prepare for web deployment"
git push -u origin main
```

2. **Streamlit Cloudでデプロイ**
   - https://share.streamlit.io/ にアクセス
   - GitHubでサインイン
   - "New app" をクリック
   - リポジトリ情報を入力して "Deploy"

3. **Secretsを設定**
   - Settings → Secrets に移動
   - 以下を貼り付け:
```toml
GOOGLE_API_KEY = "AIzaSyCVOryUeFaYf1n8Oun9wAh9RxGYD4MkKuY"

[auth]
password = "your_secure_password_here"
```

4. **完了！** アプリが自動的にデプロイされます

⚠️ **重要**: リポジトリは**プライベート**に設定してください

### 🐳 Dockerでデプロイ

```bash
# ビルド
docker build -t ai-search-app .

# 実行
docker run -p 8501:8501 \
  -e GOOGLE_API_KEY="your-api-key" \
  ai-search-app

# または Docker Compose
docker-compose up -d
```

### 🔧 その他のデプロイオプション

#### Heroku

```bash
heroku login
heroku create your-app-name
git push heroku main
```

#### AWS EC2

```bash
# EC2インスタンスでStreamlitを起動
streamlit run main.py --server.port 8501 --server.address 0.0.0.0
```

#### Google Cloud Run

```bash
gcloud run deploy --source .
```

### 🔒 セキュリティ機能

アプリには以下のセキュリティ機能が実装されています：

- ✅ パスワード認証
- ✅ ログイン試行回数制限（6時間以内に3回まで）
- ✅ セッションタイムアウト（デフォルト: 60分）
- ✅ アクセスログ記録
- ✅ XSRF保護
- ✅ IPホワイトリスト（オプション）

## トラブルシューティング

### ローカル環境

**問題**: `ModuleNotFoundError`が発生する
- **解決**: 仮想環境が有効化されているか確認し、`pip install -r requirements.txt`を再実行

**問題**: Google Gemini APIエラー
- **解決**: `.env`ファイルのAPIキーが正しいか確認（https://aistudio.google.com/app/apikey で取得）

**問題**: 文字化けが発生する
- **解決**: Windowsの場合、`initialize.py`の`adjust_string`関数が自動的に対応します

### デプロイ環境

**問題**: アプリが起動しない
- **解決**: Streamlit Cloudのログを確認し、依存パッケージのバージョンを確認

**問題**: データが読み込めない
- **解決**: `data/`ディレクトリが正しく配置されているか確認

**問題**: APIキーエラー
- **解決**: Streamlit Cloudの"Secrets"設定を確認

## ライセンス

社内利用限定

## サポート

問題が発生した場合は、開発チームまでお問い合わせください。

