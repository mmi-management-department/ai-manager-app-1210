# 📁 プロジェクト構造ガイド

このドキュメントでは、プロジェクトのフォルダ構造と各ファイルの役割を説明します。

---

## 🌳 フォルダ構造

```
プロジェクトルート/
├── assets/                    # アセット（静的ファイル）
│   └── images/               # 画像専用フォルダ ✨
│       ├── company_logo.svg        # 会社ロゴ（使用中）
│       ├── ai_manager_avatar.png   # AI管理部長アバター（使用中）
│       ├── backups/                # オリジナル画像のバックアップ
│       └── README.md               # 画像管理ガイド
│
├── config/                    # 設定ファイル
│   ├── google_drive_config.json.template         # Google Drive設定テンプレート
│   ├── google_drive_security_config.json.template # セキュリティ設定テンプレート
│   └── env_template.txt                          # 環境変数テンプレート
│
├── docs/                      # ドキュメント
│   ├── guides/               # 各種ガイド
│   │   ├── ADMIN_GUIDE.md              # 管理者向けガイド
│   │   ├── USER_GUIDE.md               # ユーザー向けガイド
│   │   ├── DEPLOYMENT_GUIDE.md         # デプロイガイド
│   │   ├── SECURITY_GUIDE.md           # セキュリティガイド
│   │   ├── LIBRARY_GUIDE.md            # ライブラリガイド
│   │   ├── LANGCHAIN_GUIDE.md          # LangChainガイド
│   │   ├── API_KEYS_SETUP_GUIDE.md     # APIキー設定ガイド
│   │   ├── VECTORSTORE_SETUP_GUIDE.md  # ベクターストア設定ガイド
│   │   ├── FAQ.md                      # よくある質問
│   │   ├── TROUBLESHOOTING.md          # トラブルシューティング
│   │   └── ...その他のガイド
│   │
│   ├── summaries/            # 各種サマリー
│   │   ├── WEB_DEPLOYMENT_SUMMARY.md         # WEBデプロイサマリー
│   │   ├── SECURITY_SUMMARY.md               # セキュリティサマリー
│   │   ├── LANGCHAIN_SUMMARY.md              # LangChainサマリー
│   │   ├── COMPLETE_FREE_SETUP_SUMMARY.md    # 完全無料セットアップサマリー
│   │   └── ...その他のサマリー
│   │
│   ├── deployment/           # デプロイ関連ドキュメント
│   │   ├── DEPLOYMENT_COMPLETED_NEXT_STEPS.md
│   │   ├── STREAMLIT_DEPLOY_STEP_BY_STEP.md
│   │   ├── WEB_DEPLOYMENT_CHECKLIST.md
│   │   └── WEB_DEPLOYMENT_WITH_GOOGLE_DRIVE.md
│   │
│   ├── API_KEYS_REFERENCE.md       # APIキークイックリファレンス
│   ├── SECURITY_CHECKLIST.md       # セキュリティチェックリスト
│   ├── SETUP_CHECKLIST.md          # セットアップチェックリスト
│   └── PROJECT_STRUCTURE.md        # このファイル
│
├── scripts/                   # スクリプト
│   ├── setup/                # セットアップスクリプト
│   │   ├── install_extended.bat          # 拡張機能インストール
│   │   ├── install_google_drive.bat      # Google Driveインストール
│   │   ├── install_langchain_openai.bat  # LangChain OpenAIインストール
│   │   ├── install_lightweight.bat       # 軽量版インストール
│   │   ├── install_media_vpn.bat         # メディアVPNインストール
│   │   ├── setup_google_account.py       # Google アカウントセットアップ
│   │   └── fix_numpy.bat                 # NumPy互換性修正
│   │
│   ├── deployment/           # デプロイスクリプト
│   │   ├── deploy_streamlit.bat            # Streamlitデプロイ
│   │   ├── create_vectorstore.bat          # ベクターストア作成（Gemini）
│   │   ├── create_vectorstore_openai.bat   # ベクターストア作成（OpenAI）
│   │   ├── create_vectorstore_local.py     # ローカルベクターストア作成
│   │   └── create_vectorstore_openai.py    # OpenAIベクターストア作成
│   │
│   └── utils/                # ユーティリティスクリプト
│       ├── switch_to_free.bat           # 完全無料版に切り替え
│       ├── switch_to_gemini.bat         # Gemini APIに切り替え
│       ├── switch_to_openai.bat         # OpenAI APIに切り替え
│       ├── git_commit_version.bat       # Gitコミット＆バージョンタグ
│       ├── push_to_github.bat           # GitHubプッシュ
│       ├── create_tag_only.bat          # タグ作成のみ
│       ├── start_app_web.bat            # WEBアプリ起動
│       └── test_google_drive.py         # Google Drive テスト
│
├── requirements/              # 依存関係ファイル
│   ├── requirements_extended.txt        # 拡張機能用
│   ├── requirements_google_drive.txt    # Google Drive用
│   ├── requirements_lightweight_*.txt   # 軽量版用（分割インストール）
│   ├── requirements_mac.txt             # Mac用
│   ├── requirements_windows.txt         # Windows用
│   ├── requirements_media_basic.txt     # メディア基本機能用
│   └── requirements_media_vpn.txt       # メディアVPN用
│
├── data/                      # データフォルダ（アプリが参照）
│   ├── MTG議事録/            # 会議議事録
│   ├── メディア/             # メディア情報
│   ├── メディアについて/     # メディア詳細情報
│   ├── 会社について/         # 会社情報
│   └── 顧客について/         # 顧客情報
│
├── data_backup/              # バックアップデータ
│   ├── MTG議事録_顧客/       # 顧客会議議事録
│   ├── ファイルについて/     # ファイル情報
│   ├── 既読規程以外の社内ルールについて/  # 社内ルール
│   └── 規則規程について/     # 規則規程
│
├── openai_version/           # OpenAIバージョン（代替実装）
│   ├── initialize_openai.py       # OpenAI初期化処理
│   ├── utils_openai.py            # OpenAIユーティリティ
│   ├── requirements_openai.txt    # OpenAI用依存関係
│   ├── env_openai_template.txt    # OpenAI環境変数テンプレート
│   ├── README_OPENAI.md           # OpenAIバージョンREADME
│   └── SWITCH_GUIDE.md            # 切り替えガイド
│
├── .streamlit/               # Streamlit設定
│   ├── config.toml                  # Streamlit設定
│   └── secrets.toml.template        # Secrets テンプレート
│
├── main.py                   # メインアプリ（エントリーポイント）
├── initialize.py             # 初期化処理（データ読み込み、ベクターストア設定）
├── auth.py                   # 認証・アクセス制御
├── components.py             # UIコンポーネント（表示部品）
├── utils.py                  # ユーティリティ関数（AI回答生成など）
├── constants.py              # 定数定義
├── feedback.py               # ユーザーフィードバック機能
├── avatar_manager.py         # ロゴ・アバター管理
├── langchain_enhanced.py     # LangChain拡張機能
├── security_utils.py         # セキュリティユーティリティ
├── google_drive_manager.py   # Google Drive管理
├── google_drive_security.py  # Google Driveセキュリティ
├── google_drive_service_account.py  # サービスアカウント管理
├── media_viewer.py           # メディアビューアー
├── vpn_manager.py            # VPNマネージャー
│
├── requirements.txt          # メイン依存関係（Streamlit Cloud用）
├── runtime.txt               # Pythonバージョン指定
├── .python-version           # Pythonバージョン指定（代替）
├── .gitignore                # Git除外設定
├── README.md                 # プロジェクトメインREADME
└── API_KEYS_ACTUAL.md        # 実際のAPIキー（機密、Gitignore対象）
```

---

## 📝 主要ファイルの説明

### **コアファイル**

| ファイル名 | 役割 | 重要度 |
|-----------|------|--------|
| `main.py` | アプリのメインエントリーポイント | ★★★★★ |
| `initialize.py` | 初期化処理（データ読み込み、ベクターストア設定） | ★★★★★ |
| `auth.py` | 認証・アクセス制御（パスワード保護） | ★★★★☆ |
| `components.py` | UI表示部品（タイトル、会話ログなど） | ★★★★☆ |
| `utils.py` | ユーティリティ関数（AI回答生成） | ★★★★★ |
| `constants.py` | 定数定義（設定値） | ★★★★☆ |

### **設定ファイル**

| ファイル名 | 役割 |
|-----------|------|
| `requirements.txt` | メイン依存関係（Streamlit Cloud自動検出） |
| `runtime.txt` | Pythonバージョン指定（3.11） |
| `.streamlit/secrets.toml.template` | Streamlit Secretsテンプレート |
| `config/env_template.txt` | ローカル環境変数テンプレート |

---

## 🎯 よく使うファイル・フォルダ

### **開発時:**
- `main.py` - メインアプリコード
- `initialize.py` - 初期化処理
- `utils.py` - ユーティリティ関数
- `components.py` - UI部品
- `requirements.txt` - 依存関係

### **セットアップ時:**
- `scripts/setup/` - セットアップスクリプト
- `config/` - 設定ファイルテンプレート
- `docs/guides/` - 各種ガイド

### **デプロイ時:**
- `scripts/deployment/` - デプロイスクリプト
- `docs/deployment/` - デプロイガイド
- `requirements.txt` - メイン依存関係

### **トラブルシューティング時:**
- `docs/guides/TROUBLESHOOTING.md` - トラブルシューティング
- `docs/guides/FAQ.md` - よくある質問

---

## 🔄 スクリプトの実行方法

### **セットアップ:**
```bash
# Google Drive機能のインストール
scripts\setup\install_google_drive.bat

# 拡張機能のインストール
scripts\setup\install_extended.bat
```

### **ベクターストア作成:**
```bash
# OpenAI APIで作成
scripts\deployment\create_vectorstore_openai.bat

# Google Gemini APIで作成（無料）
scripts\deployment\create_vectorstore.bat
```

### **デプロイ:**
```bash
# GitHubにプッシュ
scripts\utils\push_to_github.bat

# バージョンタグを作成してプッシュ
scripts\utils\git_commit_version.bat
```

---

## 📚 ドキュメントの探し方

### **目的別ガイド:**

| 目的 | ドキュメント |
|------|------------|
| アプリの使い方を知りたい | `docs/guides/USER_GUIDE.md` |
| 管理者としてアプリを管理したい | `docs/guides/ADMIN_GUIDE.md` |
| WEBにデプロイしたい | `docs/deployment/STREAMLIT_DEPLOY_STEP_BY_STEP.md` |
| APIキーを設定したい | `docs/guides/API_KEYS_SETUP_GUIDE.md` |
| セキュリティを強化したい | `docs/guides/SECURITY_GUIDE.md` |
| エラーを解決したい | `docs/guides/TROUBLESHOOTING.md` |
| よくある質問を見たい | `docs/guides/FAQ.md` |

### **機能別ガイド:**

| 機能 | ドキュメント |
|------|------------|
| Google Drive連携 | `docs/guides/GOOGLE_DRIVE_SETUP.md` |
| LangChain拡張機能 | `docs/guides/LANGCHAIN_GUIDE.md` |
| ベクターストア | `docs/guides/VECTORSTORE_SETUP_GUIDE.md` |
| 完全無料セットアップ | `docs/summaries/COMPLETE_FREE_SETUP_SUMMARY.md` |

---

## 🔒 機密情報の管理

### **Gitignore対象ファイル:**
- `API_KEYS_ACTUAL.md` - 実際のAPIキー
- `.env` - 環境変数
- `*.token.json` - 認証トークン
- `logs/` - ログファイル
- `vectorstore/` - ベクターストア（大容量）

### **テンプレートファイル:**
- `config/env_template.txt` - 環境変数テンプレート
- `config/google_drive_config.json.template` - Google Drive設定テンプレート
- `.streamlit/secrets.toml.template` - Streamlit Secretsテンプレート

---

## 🎨 画像ファイルの管理

### **使用中の画像:**
- `assets/images/company_logo.svg` - 会社ロゴ
- `assets/images/ai_manager_avatar.png` - AI管理部長アバター

### **バックアップ:**
- `assets/images/backups/` - オリジナル画像のバックアップ

### **画像の変更方法:**
1. 新しい画像を `assets/images/` に配置
2. `avatar_manager.py` のパスを更新（必要に応じて）
3. アプリを再起動

---

## 🆘 サポート

**質問・問題が発生した場合:**
1. `docs/guides/FAQ.md` を確認
2. `docs/guides/TROUBLESHOOTING.md` を確認
3. リアルの管理部長までキントーンでお問い合わせください

---

*最終更新：2025年12月14日*  
*株式会社エムエムインターナショナル*

