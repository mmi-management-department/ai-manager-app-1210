# クイックスタート - WEB公開 🚀

このガイドでは、最速でアプリをWEB公開する方法を説明します。

## 🎯 現在の状態

✅ **アプリは既に起動しています！**

以下のURLでアクセス可能です：

- **ローカル**: http://localhost:8501
- **社内ネットワーク**: http://192.168.3.178:8501

## 🏢 社内ネットワークで共有（最も簡単）

### 手順

1. **URLを社内メンバーに共有**:
   ```
   http://192.168.3.178:8501
   ```

2. **パスワードを共有**（安全な方法で）

3. **完了！** 同じネットワーク内のユーザーがアクセスできます

### 注意事項

- 同じWi-Fiネットワークに接続している必要があります
- PCがシャットダウンするとアクセスできなくなります
- ファイアウォールでポート8501が開放されている必要があります

---

## ☁️ Streamlit Cloudで公開（推奨）

### 5分でデプロイ！

#### ステップ 1: GitHubにプッシュ

```bash
# 1. コミット
git add .
git commit -m "Prepare for web deployment"

# 2. GitHubリポジトリを作成（ブラウザで）
# https://github.com/new
# リポジトリ名: ai-search-app
# プライベートリポジトリを選択

# 3. プッシュ
git remote add origin https://github.com/your-username/ai-search-app.git
git push -u origin main
```

#### ステップ 2: Streamlit Cloudでデプロイ

1. **https://share.streamlit.io/** にアクセス
2. **GitHubでサインイン**
3. **「New app」をクリック**
4. **情報を入力**:
   - Repository: `your-username/ai-search-app`
   - Branch: `main`
   - Main file path: `main.py`
5. **「Deploy」をクリック**

#### ステップ 3: APIキーを設定

1. **Settings** → **Secrets**に移動
2. 以下を貼り付け:

```toml
GOOGLE_API_KEY = "AIzaSyCVOryUeFaYf1n8Oun9wAh9RxGYD4MkKuY"

[auth]
password = "your_secure_password_here"
```

3. **Save**をクリック

#### ステップ 4: 完了！

アプリが自動的にデプロイされます。URLは以下の形式になります：

```
https://your-app-name.streamlit.app
```

---

## 🔒 セキュリティ設定

### パスワードの変更

`.streamlit/secrets.toml`または Streamlit Cloud Secretsで設定:

```toml
[auth]
password = "新しい強力なパスワード"
session_timeout_minutes = 60
max_login_attempts = 3
```

### 推奨パスワード

- 12文字以上
- 大文字、小文字、数字、記号を含む
- 辞書にない単語

---

## 📊 動作確認

### テスト項目

1. **ログイン**: パスワードを入力してログイン
2. **検索**: 「JINNY」で検索
3. **ソース確認**: 検索結果のソースが表示される
4. **ログアウト**: サイドバーからログアウト

---

## 🆘 トラブルシューティング

### アプリが起動しない

```bash
# ログを確認
cat logs/application.log

# 再起動
start_streamlit.bat
```

### 接続できない（ERR_CONNECTION_REFUSED）

**原因**: アプリが起動していない

**解決方法**:
```bash
# アプリを起動
start_streamlit.bat
```

### メモリ不足エラー（Streamlit Cloud）

**解決方法**:
- ベクターストアのサイズを削減
- 不要なファイルを削除

---

## 📞 詳細ガイド

より詳しい情報は以下を参照してください：

- **完全ガイド**: `WEB_DEPLOYMENT_GUIDE.md`
- **チェックリスト**: `DEPLOY_CHECKLIST.md`
- **メインREADME**: `README.md`

---

## ✅ 次のステップ

- [ ] 社内メンバーにURLを共有
- [ ] パスワードを安全に共有
- [ ] 使い方ガイドを共有
- [ ] フィードバックを収集

---

**最終更新**: 2025-12-15

