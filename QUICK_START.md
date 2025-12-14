# 🚀 クイックスタート

このアプリを**5分で起動**する方法を説明します。

---

## ⚡ 3つのステップ

### **ステップ1: 環境変数の設定（1分）**

1. **`config/env_template.txt` をコピーして `.env` を作成**

```bash
copy config\env_template.txt .env
```

2. **`.env` ファイルを開いて、APIキーを確認**
   - Google Gemini API キーは既に設定済み ✅
   - OpenAI API キーは `API_KEYS_ACTUAL.md` を参照

---

### **ステップ2: 依存関係のインストール（2分）**

```bash
# 仮想環境を作成
python -m venv env

# 仮想環境を有効化
env\Scripts\activate

# 依存関係をインストール
pip install -r requirements.txt
```

---

### **ステップ3: アプリを起動（1分）**

```bash
streamlit run main.py
```

ブラウザが自動的に開きます：`http://localhost:8501`

---

## 🔐 ログイン

**パスワード**: `mmi8686`

---

## 🧪 動作テスト

質問を入力してテスト：

```
就業規則について教えてください
```

---

## 🌐 WEBにデプロイ

詳細は以下を参照：
- `docs/deployment/STREAMLIT_DEPLOY_STEP_BY_STEP.md`
- `docs/guides/STREAMLIT_SECRETS_QUICK_SETUP.md`

**簡易手順:**

1. GitHub にプッシュ:
   ```bash
   scripts\utils\push_to_github.bat
   ```

2. Streamlit Cloud でデプロイ:
   - https://share.streamlit.io/
   - Settings → Secrets で APIキーを設定

---

## 📚 詳細ガイド

| 目的 | ドキュメント |
|------|------------|
| プロジェクト構造を理解したい | `docs/PROJECT_STRUCTURE.md` |
| ユーザーガイド | `docs/guides/USER_GUIDE.md` |
| 管理者ガイド | `docs/guides/ADMIN_GUIDE.md` |
| トラブルシューティング | `docs/guides/TROUBLESHOOTING.md` |
| よくある質問 | `docs/guides/FAQ.md` |

---

## 💰 完全無料で運用

**現在の構成:**
- LLM: Google Gemini API（無料）
- Embeddings: OpenAI（読み込み時のみ、約0.01円）
- **月間コスト: 実質無料**

**完全無料にする方法:**
```bash
# Google Gemini Embeddings に切り替え
scripts\utils\switch_to_free.bat
```

詳細: `docs/summaries/COMPLETE_FREE_SETUP_SUMMARY.md`

---

## ⚠️ トラブルシューティング

### **エラー: `GOOGLE_API_KEY が設定されていません`**

**対処法:**
1. `.env` ファイルが存在するか確認
2. `GOOGLE_API_KEY=` の後にスペースがないか確認
3. アプリを再起動

---

### **エラー: `ModuleNotFoundError`**

**対処法:**
```bash
pip install -r requirements.txt
```

---

## 📞 サポート

**お問い合わせ:**
リアルの管理部長までキントーンでお問い合わせください！

---

*最終更新：2025年12月14日*  
*株式会社エムエムインターナショナル*



