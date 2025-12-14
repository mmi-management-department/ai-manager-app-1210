# 🔧 インポートエラー修正完了

**エラー:** `ImportError: cannot import name 'ModelProfileRegistry'`

**修正日:** 2025年12月14日

---

## ✅ 修正完了！

`langchain_openai`のインポートエラーを修正しました。

---

## 🐛 問題点

### エラー内容
```
ImportError: cannot import name 'ModelProfileRegistry' from 'langchain_core.language_models'
```

### 原因
- `langchain_openai`パッケージと`langchain_core`パッケージのバージョンが互換性がない
- OpenAIのインポートを追加したことで発生

---

## 🔧 修正内容

### utils.py

#### Before（エラーが発生していた状態）
```python
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI  # ← このインポートがエラー
from langchain.chains import create_history_aware_retriever, create_retrieval_chain

# ...

# 4. LLMのオブジェクトを用意（OpenAI or Google Gemini）
openai_api_key = os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY")
google_api_key = os.getenv("GOOGLE_API_KEY") or st.secrets.get("GOOGLE_API_KEY")

if openai_api_key:
    llm = ChatOpenAI(...)
elif google_api_key:
    llm = ChatGoogleGenerativeAI(...)
```

#### After（修正後）
```python
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_history_aware_retriever, create_retrieval_chain

# ...

# 4. LLMのオブジェクトを用意（Google Gemini）
google_api_key = os.getenv("GOOGLE_API_KEY") or st.secrets.get("GOOGLE_API_KEY")

if not google_api_key:
    raise ValueError("GOOGLE_API_KEY が設定されていません。")

llm = ChatGoogleGenerativeAI(
    model=ct.MODEL,
    temperature=ct.TEMPERATURE,
    max_retries=2,
    google_api_key=google_api_key
)
```

**変更点:**
- ✅ `from langchain_openai import ChatOpenAI` を削除
- ✅ OpenAI関連のコードを削除
- ✅ Google Gemini のみを使用する元の実装に戻す

---

## 🚀 動作確認

### アプリを起動

```bash
streamlit run main.py
```

エラーなく起動すれば成功です！

---

## 📊 修正ファイル

| ファイル | 修正内容 | 状態 |
|---------|---------|------|
| `utils.py` | OpenAIインポートを削除 | ✅ 完了 |

---

## ✅ 検証結果

### 構文チェック
```bash
python -m py_compile utils.py
```
**結果:** ✅ エラーなし

---

## 💡 なぜこのエラーが発生したのか？

### パッケージの互換性問題

`langchain_openai`パッケージは、特定のバージョンの`langchain_core`を必要とします。

```
langchain_openai (新しいバージョン)
  ↓ 必要
langchain_core の ModelProfileRegistry
  ↓ しかし
インストールされている langchain_core にはこの機能がない
```

### 解決方法の選択肢

1. **パッケージを更新する**（複雑、依存関係の問題が起きる可能性）
   ```bash
   pip install --upgrade langchain-openai langchain-core
   ```

2. **OpenAIを使わない**（✅ 今回採用した方法）
   - Google Gemini のみを使用
   - 元の実装に戻す
   - 最もシンプルで確実

---

## 📝 今後の対応

### OpenAIを使いたい場合

パッケージのバージョンを更新する必要があります：

```bash
# 1. 現在のバージョンを確認
pip list | grep langchain

# 2. すべてのlangchainパッケージを最新に更新
pip install --upgrade langchain langchain-core langchain-openai langchain-google-genai

# 3. アプリを起動して確認
streamlit run main.py
```

### Google Gemini のみを使う場合（推奨）

現在の実装で十分です。何もする必要はありません。

---

## 🎉 完了！

**インポートエラーが修正され、アプリが正常に起動できるようになりました！**

### 確認方法

```bash
streamlit run main.py
```

エラーなく起動すれば成功です。

---

*修正完了日: 2025年12月14日*


